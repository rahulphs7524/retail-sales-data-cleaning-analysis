"""
Retail Sales Data Cleaning & Analysis
Beginner-friendly project based on Python topics covered in the learning files.
"""

import os
import pandas as pd
import numpy as np


DATA_FILE = os.path.join("data", "raw_sales_data.csv")
OUTPUT_DIR = "outputs"


def clean_text(value):
    """Remove extra spaces and standardize text to title case."""
    if pd.isna(value):
        return ""
    return str(value).strip().title()


def categorize_order(value):
    """Classify an order using the sales thresholds practised in the course."""
    if value >= 5000:
        return "High"
    elif value >= 2000:
        return "Medium"
    else:
        return "Low"


def load_data(file_path):
    """Read the raw CSV file."""
    if not os.path.exists(file_path):
        print("Input file not found:", file_path)
        return None

    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Clean text, numeric columns, dates and duplicate orders."""
    df = df.copy()

    # Clean text columns
    text_columns = [
        "Customer_Name", "City", "State", "Product_Category",
        "Product_Name", "Payment_Type"
    ]
    for column in text_columns:
        df[column] = df[column].apply(clean_text)

    # Convert numeric columns. Invalid values become missing values.
    numeric_columns = ["Quantity", "Unit_Price", "Discount"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Convert order date
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    # Keep a clear label for missing city values.
    df["City"] = df["City"].replace("", "Unknown")
    df["State"] = df["State"].replace("", "Unknown")

    # Missing discount means no discount in this sample dataset.
    df["Discount"] = df["Discount"].fillna(0)

    # Remove duplicate order IDs, keeping the first occurrence.
    rows_before = len(df)
    df = df.drop_duplicates(subset=["Order_ID"], keep="first")
    duplicate_count = rows_before - len(df)

    # Remove rows where essential numeric/date fields are invalid.
    rows_before_invalid = len(df)
    df = df.dropna(subset=["Quantity", "Unit_Price", "Order_Date"])
    invalid_rows_removed = rows_before_invalid - len(df)

    # Remove impossible non-positive quantities/prices.
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] > 0)]

    # Calculate sales after cleaning.
    df["Total_Sales"] = (
        df["Quantity"] * df["Unit_Price"]
    ) - df["Discount"]

    # Classify order value with a function and conditional statements.
    df["Order_Value_Category"] = df["Total_Sales"].apply(categorize_order)

    # Add order year and month for simple period-based summaries.
    df["Order_Year"] = df["Order_Date"].dt.year
    df["Order_Month"] = df["Order_Date"].dt.month

    cleaning_info = {
        "duplicate_orders_removed": duplicate_count,
        "invalid_rows_removed": invalid_rows_removed,
        "final_rows": len(df)
    }

    return df, cleaning_info


def create_summaries(df):
    """Create city-wise, category-wise and payment-wise reports."""
    sales_by_city = (
        df.groupby("City", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Total_Sales", ascending=False)
    )

    sales_by_category = (
        df.groupby("Product_Category", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Total_Sales", ascending=False)
    )

    orders_by_payment = (
        df.groupby("Payment_Type", as_index=False)["Order_ID"]
        .count()
        .rename(columns={"Order_ID": "Order_Count"})
        .sort_values("Order_Count", ascending=False)
    )

    sales_by_month = (
        df.groupby("Order_Month", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Order_Month")
    )

    category_stats = (
        df.groupby("Product_Category")["Total_Sales"]
        .agg(["min", "max", "count", "mean"])
        .sort_values("mean", ascending=False)
    )

    return sales_by_city, sales_by_category, orders_by_payment, sales_by_month, category_stats


def print_report(df, cleaning_info, summaries):
    """Display key business results in the terminal."""
    sales_by_city, sales_by_category, orders_by_payment, sales_by_month, category_stats = summaries

    total_sales = df["Total_Sales"].sum()
    average_order = df["Total_Sales"].mean()
    highest_order = df["Total_Sales"].max()
    lowest_order = df["Total_Sales"].min()

    # NumPy array and basic numerical calculations from the course.
    sales_array = np.array(df["Total_Sales"])
    print("\\n" + "=" * 58)
    print("             RETAIL SALES ANALYSIS REPORT")
    print("=" * 58)
    print("Orders analysed:", len(df))
    print("Duplicate orders removed:", cleaning_info["duplicate_orders_removed"])
    print("Invalid rows removed:", cleaning_info["invalid_rows_removed"])
    print("Total sales: Rs.", round(total_sales, 2))
    print("Average order value: Rs.", round(average_order, 2))
    print("Highest order value: Rs.", round(highest_order, 2))
    print("Lowest order value: Rs.", round(lowest_order, 2))
    print("Sales standard deviation:", round(float(sales_array.std()), 2))

    print("\\n--- SALES BY CITY ---")
    print(sales_by_city.to_string(index=False))

    print("\\n--- SALES BY PRODUCT CATEGORY ---")
    print(sales_by_category.to_string(index=False))

    print("\\n--- ORDERS BY PAYMENT TYPE ---")
    print(orders_by_payment.to_string(index=False))

    print("\\n--- MONTH-WISE SALES ---")
    print(sales_by_month.to_string(index=False))

    print("\\n--- PRODUCT CATEGORY STATISTICS ---")
    print(category_stats.to_string())


def export_reports(df, summaries, cleaning_info):
    """Save cleaned data and summary reports as CSV files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    sales_by_city, sales_by_category, orders_by_payment, sales_by_month, category_stats = summaries

    df.to_csv(os.path.join(OUTPUT_DIR, "cleaned_sales_data.csv"), index=False)
    sales_by_city.to_csv(os.path.join(OUTPUT_DIR, "sales_by_city.csv"), index=False)
    sales_by_category.to_csv(os.path.join(OUTPUT_DIR, "sales_by_category.csv"), index=False)
    orders_by_payment.to_csv(os.path.join(OUTPUT_DIR, "orders_by_payment.csv"), index=False)
    sales_by_month.to_csv(os.path.join(OUTPUT_DIR, "sales_by_month.csv"), index=False)
    category_stats.to_csv(os.path.join(OUTPUT_DIR, "category_statistics.csv"))

    cleaning_report = pd.DataFrame([cleaning_info])
    cleaning_report.to_csv(os.path.join(OUTPUT_DIR, "cleaning_summary.csv"), index=False)

    print("\\nAll cleaned data and summary reports were saved in the outputs folder.")


def main():
    print("Starting Retail Sales Data Cleaning & Analysis...")

    raw_data = load_data(DATA_FILE)
    if raw_data is None:
        return

    cleaned_data, cleaning_info = clean_data(raw_data)
    if cleaned_data.empty:
        print("No valid records available after cleaning.")
        return

    summaries = create_summaries(cleaned_data)
    print_report(cleaned_data, cleaning_info, summaries)
    export_reports(cleaned_data, summaries, cleaning_info)


if __name__ == "__main__":
    main()
