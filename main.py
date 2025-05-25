import subprocess

import enter


def convert_to_excel(path):
    import pandas as pd

    # Read the CSV file
    df = pd.read_csv(path)

    # Convert to Excel
    excel_file = path[:-4] + ".xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Successfully converted CSV to Excel: {excel_file}")


subprocess.run(["python", "grdp_per_capita.py"])
subprocess.run(["python", "region.py"])
convert_to_excel(enter.province_path)
