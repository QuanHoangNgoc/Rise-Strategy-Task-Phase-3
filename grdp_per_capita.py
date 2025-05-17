import pandas as pd

import enter

INPUT_PATH = enter.INPUT_DATA


def load_data():
    # Read the CSV file and strip whitespace from column names
    df = pd.read_csv(INPUT_PATH)
    df.columns = df.columns.str.strip()
    # Print column names to debug
    print("[+] Column names in the DataFrame:", df.columns.tolist())
    return df


def display_computed_df(df: pd.DataFrame, computed_col: str):
    # Sort by GRDP per capita in descending order
    df_sorted = df.sort_values(computed_col, ascending=False)

    # Display results
    print("\nGRDP per capita by province (sorted from highest to lowest):")
    print("=" * 80)
    print(f"{'Province':<30} {'GRDP per capita (BVnd)':<20}")
    print("-" * 80)

    for _, row in df_sorted.iterrows():
        print(f"{row['Name'].strip():<30} {row[computed_col]:,.2f}")

    # Calculate and display some statistics
    print("\nStatistics:")
    print("=" * 80)
    print(f"[+] Average GRDP per capita: {df[computed_col].mean():,.2f} BVnd")
    print(f"[+] Highest GRDP per capita: {df[computed_col].max():,.2f} BVnd")
    print(f"[+] Lowest GRDP per capita: {df[computed_col].min():,.2f} BVnd")


def rank_df(computed_df: pd.DataFrame, computed_col: str, num_rank=4):
    score_df = computed_df.sort_values(computed_col, ascending=True)

    bin_len = len(score_df) // num_rank
    if len(score_df) % num_rank != 0:
        bin_len += 1

    score_col = "score"
    score_df[score_col] = [i // bin_len + 1 for i in range(len(score_df))]
    return score_df, score_col


def rank_df_follow_minmax(computed_df: pd.DataFrame, computed_col: str, num_rank=4):
    score_df = computed_df.sort_values(computed_col, ascending=True)

    min_v, max_v = min(score_df[computed_col]), max(score_df[computed_col])

    score_col = "minmax_score"
    score_df[score_col] = (score_df[computed_col] -
                           min_v) / (max_v - min_v) * num_rank
    return score_df, score_col


if __name__ == "__main__":
    df = load_data()

    # Calculate GRDP per capita (GRDP per person)
    computed_col = 'GRDP_per_capita'
    df[computed_col] = df['Total_GRDP_BVnd'] / df['People']
    display_computed_df(df=df, computed_col=computed_col)

    score_df, score_col = rank_df(
        computed_df=df, computed_col=computed_col)
    if enter.USE_MINMAX_SCORE:
        tmp = rank_df_follow_minmax(computed_df=df, computed_col=computed_col)
        score_df[tmp[1]] = tmp[0][tmp[1]].copy()

    # Save the scored DataFrame to CSV
    output_path = enter.province_path
    score_df.drop(columns=['STT']).to_csv(output_path, index=False)
    print(f"\n[+] Saved scored provinces to: {output_path}")
