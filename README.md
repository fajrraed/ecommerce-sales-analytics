# E-Commerce Customer Behavior and Sales Analytics

An end-to-end data analytics and business intelligence project tracking retail transactional behavior. This project uses Python to simulate 1,500 comprehensive checkout records and compute high-level business indicators, which are then integrated into a fully interactive Power BI executive dashboard for performance tracking and reporting.

## Project Workspace Components
- ecommerce_sales.csv: The baseline retail transactions dataset.
- generate_sales_data.py: Script generating demographic and categorical datasets.
- analyze_sales.py: Script evaluating core revenue metrics ($913,431.80 total store sales).
- visualize_sales.py: Alternative charting script tracking metric trends.
- analytics_output.txt: Log file capturing finalized execution terminal output values.
- ecommerce_dashboard.pbix: Finished interactive Power BI dashboard tracking category distribution, seasonal monthly sales trends, and payment popularity.

## Requirements
Install processing dependencies using pip:
```bash
pip install pandas numpy matplotlib seaborn
```

## How to Interact
1. Run the processing analyzer to view console aggregates: python analyze_sales.py
2. Open the .pbix file inside Power BI Desktop to use the dynamic Customer Age slicer filter.
