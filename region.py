from ast import Name

import pandas as pd
from click import group
from narwhals import col

import enter
import grdp_per_capita


def compute_sum_by_region(root_df: pd.DataFrame):
    # Add region column
    df = root_df.copy()
    df['Region'] = df['Name'].map(enter.PROVICE_TO_REGION_MAP)
    grouped = df.groupby('Region').agg({
        'Total_GRDP_BVnd': 'sum',
        'People': 'sum'
    }).reset_index()
    print("\nSum of Total_GRDP_BVnd and People by Region:")
    print("=" * 80)
    print(f"{'Region':<30} {'Total_GRDP_BVnd':>20} {'People':>20}")
    print("-" * 80)
    for _, row in grouped.iterrows():
        print(
            f"{row['Region']:<30} {row['Total_GRDP_BVnd']:>20,.2f} {row['People']:>20,.0f}")

    grouped["Name"] = grouped["Region"]
    return grouped.drop(columns=["Region"])


if __name__ == "__main__":
    root_df = grdp_per_capita.load_data()

    # Group by region follow sum
    df = compute_sum_by_region(root_df=root_df)

    # Calculate GRDP per capita (GRDP per person)
    computed_col = 'GRDP_per_capita'
    df[computed_col] = df['Total_GRDP_BVnd'] / df['People']
    grdp_per_capita.display_computed_df(df=df, computed_col=computed_col)

    score_df, score_col = grdp_per_capita.rank_df(
        computed_df=df, computed_col=computed_col, num_rank=3)
    if enter.USE_MINMAX_SCORE:
        tmp = grdp_per_capita.rank_df_follow_minmax(
            computed_df=df, computed_col=computed_col, num_rank=3)
        score_df[tmp[1]] = tmp[0][tmp[1]].copy()

    # Save the scored DataFrame to CSV
    output_path = enter.region_path
    score_df.to_csv(output_path, index=False)
    print(f"\n[+] Saved scored REGIONS to: {output_path}")
