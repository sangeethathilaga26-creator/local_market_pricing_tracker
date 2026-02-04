Agricultural Wages and Market Prices Analysis
📌 Project Overview
This project analyzes the relationship between agricultural wages and commodity prices (rice and wheat) in Tamil Nadu, India. Using official wage datasets and sample price data, the project demonstrates how Python can be applied to integrate, automate, and visualize real-world economic information.

🔹 Features
Data Integration: Merged multiple datasets (wages and prices) into a single structure.

Automation Workflow: Python scripts automate cleaning, merging, and updating CSV files.

Visualizations:

Wage trends for men vs women (gender disparity).

Dual-axis chart comparing wages with rice prices (purchasing power analysis).

Average wages by occupation (distribution of earnings).

Professional Organization: Clear folder structure with datasets, scripts, charts, and documentation.

🔹 Insights
Men consistently earn higher wages than women in agriculture.

Commodity prices do not always rise in sync with wages, affecting affordability.

Average wages vary across occupations, showing diversity in agricultural work.

🔹 Technologies Used
Python (pandas, matplotlib)

CSV files for structured datasets

Git & GitHub for version control and project sharing

📊 Project Structure
Code
PROJECT 4/
│
├── data_integration.py        # Script to merge datasets
├── clean_wages.py             # Script to clean wage data
├── chart_wages_vs_prices.py   # Visualization: wages vs prices
├── chart_dualaxis_wages_prices.py # Dual-axis chart
├── chart_wages_by_occupation.py   # Occupation-based wage chart
│
├── agricultural_wages_clean.csv   # Cleaned wage dataset
├── prices_data.csv                # Sample commodity price dataset
├── wages_prices.csv               # Integrated dataset
│
├── wages_trend.png                # Wage trend visualization
├── chart_dualaxis_wages_rice.png  # Dual-axis chart image
├── wages_by_occupation.png        # Occupation wage chart
│
└── README.md                      # Project documentation
🚀 How to Run
Clone the repository:


git clone https://github.com/your-username/agricultural-wages-prices.git
cd agricultural-wages-prices
Install required libraries:
pip install pandas matplotlib


Expand to more occupations and states.

Build interactive dashboards using Plotly or Streamlit.
