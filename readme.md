# Vietnam Provinces GRDP Analysis

## Overview

This project analyzes the Gross Regional Domestic Product (GRDP) per capita for provinces in Vietnam. It processes provincial economic data to calculate, rank, and score provinces based on their GRDP per capita values.

## Features

- Calculates GRDP per capita for each province
- Ranks provinces based on GRDP per capita
- Assigns score categories (1-4) to provinces
- Generates statistical analysis including average, highest, and lowest GRDP per capita
- Exports processed data to CSV format
- Visualize the output data by 'visualize.ipynb'

## Project Structure

├── grdp_per_capita.py # Main analysis script
├── enter.py # Configuration settings
├── craw_data/
│ └── input_data.csv # Input data file
└── output/
└── scored_provinces.csv # Output results

## Input Data Format

The input CSV file (`craw_data/input_data.csv`) should contain the following columns:

- `STT`: Serial number
- `Name`: Province name
- `Total_GRDP_BVnd`: Total GRDP in billion VND
- `People`: Population count

## Output

The script generates:

1. Console output showing:
   - GRDP per capita rankings
   - Statistical summary (average, highest, and lowest values)
2. CSV file (`output/scored_provinces.csv`) containing:
   - Province names
   - GRDP data
   - Calculated GRDP per capita
   - Score assignments (1-4)

## How to Use

1. Ensure your input data is in the correct format and placed in `craw_data/input_data.csv`
2. Run the script:
   ```bash
   python grdp_per_capita.py
   ```
3. Find the results in:
   - Console output for immediate analysis
   - `output/scored_provinces.csv` for detailed data

## Scoring Methodology

The provinces are scored using a quartile-based system:

- Provinces are sorted by GRDP per capita
- The data is divided into 4 equal groups
- Scores 1-4 are assigned (1 for lowest quartile, 4 for highest quartile)

## Dependencies

- Python 3.x
- pandas

## Configuration

Edit `enter.py` to modify:

- `INPUT_DATA`: Path to input CSV file
- `USE_MINMAX_SCORE`: Toggle between scoring methods (currently set to True)

## Output Format

The final CSV output excludes the `STT` column and includes:

- Province name
- GRDP data
- Calculated GRDP per capita
- Assigned score (1-4)
