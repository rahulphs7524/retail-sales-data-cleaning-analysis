# Retail Sales Data Cleaning & Analysis

A beginner-to-intermediate Python data analysis project that cleans retail order data, calculates sales, groups results, and exports CSV reports.

## Project objective

Retail order files often contain inconsistent text, duplicate orders, missing values, and invalid numeric/date values. This project uses Python to prepare the data and produce useful sales summaries for a small retail business.

## Skills demonstrated

The project is intentionally limited to concepts covered in the uploaded Python learning files:

- Python variables, data types, type conversion and operators
- Strings, indexing, slicing and string methods (`strip`, `title`, `replace`)
- `if`, `elif`, `else`, `for` loops and functions
- Lists, dictionaries and basic collection handling
- Reading and writing CSV files
- NumPy arrays and basic numerical calculations
- Pandas CSV loading, text cleaning, numeric conversion, duplicate removal, filtering, sorting, `groupby`, aggregation and CSV export
- Basic date handling with Pandas

No web framework, database, machine learning model, dashboard framework or advanced architecture is required.

## Project structure

```text
retail_sales_analysis_project/
│
├── data/
│   └── raw_sales_data.csv
│
├── outputs/
│   └── (generated CSV reports appear here after running)
│
├── docs/
│   └── interview_questions.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

`data/raw_sales_data.csv` is a synthetic practice dataset containing retail orders. It deliberately includes data-quality issues such as:

- Extra spaces and inconsistent capitalization
- Duplicate order IDs
- Invalid numeric values
- Missing values
- Invalid date values

The data is fictional and is included only for learning and demonstration. It does not represent a real company.

## Requirements

- Python 3.9 or later
- pandas
- numpy

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Install the requirements.
4. Run:

```bash
python main.py
```

The program prints a sales report and creates CSV files in the `outputs/` folder.

## Data cleaning workflow

1. Load the raw CSV using Pandas.
2. Standardize text fields by removing extra spaces and applying title case.
3. Convert quantity, unit price and discount to numeric values.
4. Convert order dates to date values.
5. Replace blank city/state values with `Unknown`.
6. Treat a missing discount as zero for this sample dataset.
7. Remove duplicate orders using `Order_ID`.
8. Remove records with invalid quantity, unit price or order date.
9. Calculate `Total_Sales = Quantity × Unit_Price − Discount`.
10. Categorize orders as High, Medium or Low.
11. Create grouped summaries and export the results.

## Reports generated

| Output file | Description |
|---|---|
| `cleaned_sales_data.csv` | Cleaned orders with calculated sales and order categories |
| `sales_by_city.csv` | Total sales grouped by city |
| `sales_by_category.csv` | Total sales grouped by product category |
| `orders_by_payment.csv` | Number of orders for each payment type |
| `sales_by_month.csv` | Total sales grouped by order month |
| `category_statistics.csv` | Minimum, maximum, count and average sales by category |
| `cleaning_summary.csv` | Counts of duplicate and invalid rows removed |

## Business questions answered

1. What is the total sales value?
2. What is the average order value?
3. Which city generated the highest sales?
4. Which product category generated the highest sales?
5. How many orders used each payment type?
6. How do sales vary by month?
7. What are the minimum, maximum and average order values by product category?
8. How many duplicate and invalid records were removed during cleaning?

## Important assumptions

- The dataset is synthetic.
- A blank discount is treated as zero.
- Rows with invalid quantity, unit price or order date are excluded from the analysis.
- Duplicate `Order_ID` values are reduced to the first occurrence.
- Negative or zero quantities and unit prices are excluded.
- The High/Medium/Low order thresholds are project rules: High = 5,000 or more; Medium = 2,000 to below 5,000; Low = below 2,000.

## Resume description

**Retail Sales Data Cleaning & Analysis | Python, Pandas, NumPy, CSV**

Built a Python-based retail sales analysis project to clean raw order data, handle duplicates and invalid values, calculate order-level sales, and generate city-wise, category-wise, payment-wise and monthly sales reports. Used Pandas for data cleaning, filtering, grouping, aggregation and CSV exports, along with NumPy for numerical analysis.

## GitHub upload

Suggested repository name: `retail-sales-data-cleaning-analysis`

Suggested GitHub description:

`A beginner-friendly Python project for cleaning retail order data, calculating sales, and generating business summary reports using Pandas and NumPy.`

Before publishing, include the source code, synthetic input dataset, README and interview questions. The `outputs/` folder can contain generated sample reports if you want to show example results.
