import pandas as pd
import matplotlib.pyplot as plt
import os

# File names
wage_file = "agricultural_wages_clean.csv"
price_file = "prices_data.csv"
output_file = "wages_prices.csv"

# Step 1: Load and check files
if not os.path.exists(wage_file):
    print(f"Error: {wage_file} not found in the folder.")
elif not os.path.exists(price_file):
    print(f"Error: {price_file} not found in the folder.")
else:
    wages = pd.read_csv(wage_file)
    prices = pd.read_csv(price_file)

    # Step 2: Clean year column (take first 4 digits from ranges like "2022-2023")
    wages["year_clean"] = wages["year"].astype(str).str[:4]

    # Step 3: Build Date column in wages
    wages["Date"] = pd.to_datetime(
        wages["year_clean"] + "-" + wages["month"].astype(str) + "-01",
        format="%Y-%b-%d",
        errors="coerce"
    )

    # Step 4: Convert prices Date column to datetime
    prices["Date"] = pd.to_datetime(prices["Date"], format="%Y-%m-%d", errors="coerce")

    # Step 5: Merge datasets
    merged_data = pd.merge(wages, prices, on="Date", how="inner")
    merged_data.to_csv(output_file, index=False)
    print(f"\nIntegration successful! Merged file saved as {output_file}")

    # Step 6: Create average wage column
    merged_data["avg_wage"] = (merged_data["men"] + merged_data["women"]) / 2

    # -------------------------------
    # Chart 1: Multi-line (Wages vs Rice vs Wheat)
    plt.figure(figsize=(12,6))
    plt.plot(merged_data["Date"], merged_data["avg_wage"], label="Average Wage", color="blue", linewidth=2)
    plt.plot(merged_data[merged_data["Item"]=="Rice"]["Date"], merged_data[merged_data["Item"]=="Rice"]["Price"], label="Rice Price", color="green", linestyle="--")
    plt.plot(merged_data[merged_data["Item"]=="Wheat"]["Date"], merged_data[merged_data["Item"]=="Wheat"]["Price"], label="Wheat Price", color="orange", linestyle=":")
    plt.xlabel("Date"); plt.ylabel("Value"); plt.title("Wages vs Rice & Wheat Prices Over Time")
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig("chart_wages_vs_prices.png")
    plt.close()

    # Chart 2: Dual-axis (Wages vs Rice Price)
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax2 = ax1.twinx()
    ax1.plot(merged_data["Date"], merged_data["avg_wage"], color="blue", label="Average Wage")
    ax2.plot(merged_data[merged_data["Item"]=="Rice"]["Date"], merged_data[merged_data["Item"]=="Rice"]["Price"], color="green", label="Rice Price")
    ax1.set_xlabel("Date"); ax1.set_ylabel("Average Wage", color="blue"); ax2.set_ylabel("Rice Price", color="green")
    plt.title("Dual-Axis: Wages vs Rice Price")
    fig.tight_layout()
    plt.savefig("chart_dualaxis_wages_rice.png")
    plt.close()

    # Chart 3: Bar chart (Occupation vs Average Wage)
    occupation_avg = merged_data.groupby("occupation")["avg_wage"].mean().sort_values()
    plt.figure(figsize=(12,6))
    occupation_avg.plot(kind="bar", color="purple")
    plt.xlabel("Occupation"); plt.ylabel("Average Wage")
    plt.title("Average Wages by Occupation")
    plt.tight_layout()
    plt.savefig("chart_wages_by_occupation.png")
    plt.close()

    print("\nVisualization successful! Charts saved as:")
    print(" - chart_wages_vs_prices.png")
    print(" - chart_dualaxis_wages_rice.png")
    print(" - chart_wages_by_occupation.png")

