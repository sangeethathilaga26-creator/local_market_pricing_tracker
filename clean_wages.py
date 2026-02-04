import pandas as pd
import glob
import matplotlib.pyplot as plt

# Step 1: Load all CSV files from your OneDrive Documents folder
csv_files = glob.glob("C:/Users/sange/OneDrive/Documents/*.csv")

print("CSV files found:", csv_files)  # Debug check

dataframes = []
for file in csv_files:
    df = pd.read_csv(file)

    # Step 2: Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Step 3: Replace '@' with NaN (missing values)
    df = df.replace("@", pd.NA)

    # Step 4: Clean numeric columns (men and women wages if present)
    if "men" in df.columns:
        df["men"] = pd.to_numeric(df["men"], errors="coerce")
    if "women" in df.columns:
        df["women"] = pd.to_numeric(df["women"], errors="coerce")
    if "wage" in df.columns:
        df["wage"] = pd.to_numeric(df["wage"], errors="coerce")

    dataframes.append(df)

# Step 5: Merge all CSVs into one master dataset
if dataframes:  # Only merge if files were found
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Step 6: Handle missing values (optional)
    if "men" in merged_df.columns and "women" in merged_df.columns:
        merged_df = merged_df.dropna(subset=["men", "women"], how="all")

    # Step 7: Quick analysis
    if "men" in merged_df.columns:
        print("Average male wage:", merged_df["men"].mean())
        print("Minimum male wage:", merged_df["men"].min())
        print("Maximum male wage:", merged_df["men"].max())

    if "women" in merged_df.columns:
        print("Average female wage:", merged_df["women"].mean())
        print("Minimum female wage:", merged_df["women"].min())
        print("Maximum female wage:", merged_df["women"].max())

    # Step 8: Remove unwanted 'unnamed' columns
    merged_df = merged_df.loc[:, ~merged_df.columns.str.contains("unnamed", case=False)]

    # Step 9: Save cleaned dataset
    merged_df.to_csv("agricultural_wages_clean.csv", index=False)
    print("Cleaned dataset saved as agricultural_wages_clean.csv")

    # Step 10: Visualization - Line chart of wages over years
    if "year" in merged_df.columns:
        merged_df["year"] = merged_df["year"].astype(str)

        plt.figure(figsize=(10,6))
        if "men" in merged_df.columns:
            plt.plot(merged_df["year"], merged_df["men"], label="Men", marker="o")
        if "women" in merged_df.columns:
            plt.plot(merged_df["year"], merged_df["women"], label="Women", marker="o")

        plt.title("Agricultural Wages in Tamil Nadu (Men vs Women)")
        plt.xlabel("Year")
        plt.ylabel("Wage")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("wages_trend.png")   # Save chart as PNG
        plt.close()

    # Step 11: Visualization - Bar chart by occupation
    if "occupation" in merged_df.columns:
        occupation_avg = merged_df.groupby("occupation")[["men","women"]].mean()

        occupation_avg.plot(kind="bar", figsize=(10,6))
        plt.title("Average Wages by Occupation")
        plt.xlabel("Occupation")
        plt.ylabel("Average Wage")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("wages_by_occupation.png")   # Save chart as PNG
        plt.close()

else:
    print("No CSV files found. Please check the folder path.")
