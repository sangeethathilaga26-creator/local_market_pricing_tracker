import pandas as pd
import os

# File names
wage_file = "agricultural_wages_clean.csv"
price_file = "prices_data.csv"
output_file = "wages_prices.csv"

# Check if files exist
if not os.path.exists(wage_file):
    print(f"Error: {wage_file} not found in the folder.")
elif not os.path.exists(price_file):
    print(f"Error: {price_file} not found in the folder.")
else:
    # Load the CSV files
    wages = pd.read_csv(wage_file)
    prices = pd.read_csv(price_file)

    # Clean the 'year' column: take only the first 4 digits (e.g., "2022-2023" → "2022")
    wages["year_clean"] = wages["year"].astype(str).str[:4]

    # Build a proper Date column from year + month
    wages["Date"] = pd.to_datetime(
        wages["year_clean"] + "-" + wages["month"].astype(str) + "-01",
        format="%Y-%b-%d",  # assumes month is like Jan, Feb, etc.
        errors="coerce"
    )

    # Convert prices Date column to datetime too
    prices["Date"] = pd.to_datetime(prices["Date"], format="%Y-%m-%d", errors="coerce")

    # Show samples
    print("Wages data sample with Date column:")
    print(wages[["year", "month", "Date"]].head())
    print("\nPrices data sample:")
    print(prices.head())

    # Merge on Date
    merged_data = pd.merge(wages, prices, on="Date", how="inner")

    # Save the merged dataset
    merged_data.to_csv(output_file, index=False)
    print(f"\nIntegration successful! Merged file saved as {output_file}")
