# Project Interview Questions & Answers

These answers are based on the concepts used in this project and the Python topics covered in the learning files.

## 1. What is the objective of this project?

**Answer:** The objective is to clean retail order data, calculate total sales, analyse sales by city and product category, and export the results into CSV files.

## 2. Which Python libraries did you use?

**Answer:** I used Pandas to read, clean, filter, group and export tabular data. I used NumPy to create a numerical array and calculate a basic statistical value.

## 3. Why did you clean the text columns?

**Answer:** The raw file can contain extra spaces and inconsistent capitalization. I used `strip()` to remove extra spaces and `title()` to standardize names and city values.

## 4. What is type casting?

**Answer:** Type casting means converting a value from one data type to another. In this project, `pd.to_numeric()` converts quantity, unit price and discount columns into numeric values.

## 5. Why did you use `errors="coerce"`?

**Answer:** It converts invalid numeric or date values into missing values instead of stopping the program with a conversion error. Those records can then be handled during cleaning.

## 6. How did you remove duplicate orders?

**Answer:** I used `drop_duplicates()` with `Order_ID` as the subset and kept the first occurrence.

## 7. How is total sales calculated?

**Answer:** Total sales is calculated as quantity multiplied by unit price, minus discount.

## 8. What is the purpose of a function?

**Answer:** A function is a reusable block of code. I created `clean_text()` and `categorize_order()` so that the same logic can be used in different places.

## 9. What is the difference between a list, tuple, set and dictionary?

**Answer:** A list is an ordered collection that can be changed. A tuple is ordered but cannot be changed. A set stores unique values. A dictionary stores data as key-value pairs.

## 10. What is `groupby()` used for?

**Answer:** `groupby()` groups rows that share a value, such as city or product category, so that we can calculate summaries like total or average sales.

## 11. Why did you sort the city and category summaries?

**Answer:** Sorting in descending order makes it easier to identify the cities and product categories with the highest sales.

## 12. What is the difference between `read_csv()` and `to_csv()`?

**Answer:** `read_csv()` loads data from a CSV file into a Pandas DataFrame. `to_csv()` writes a DataFrame to a CSV file.

## 13. Why is data cleaning important before analysis?

**Answer:** Inconsistent text, duplicates, missing values and invalid numbers can lead to incorrect totals and misleading business reports. Cleaning improves the reliability of the analysis.

## 14. What does `isnull().sum()` do?

**Answer:** It counts missing values in each column. It is useful for checking data quality.

## 15. What does `ascending=False` mean in `sort_values()`?

**Answer:** It sorts values from highest to lowest.

## 16. Why is a missing discount treated as zero here?

**Answer:** For this sample project, a blank discount is assumed to mean no discount was applied. This is a documented business assumption; in a real company, I would confirm the rule with the data owner.

## 17. What happens to rows with invalid quantity, unit price or date?

**Answer:** After conversion, invalid values become missing values. The project removes those rows because they cannot be used reliably to calculate sales or analyse order dates.

## 18. Is this a real company's sales data?

**Answer:** No. The included dataset is synthetic and was created for practice and demonstration.

## 19. What improvements could be added later?

**Answer:** After learning more tools, I could add visualizations or a dashboard. Those features are not part of the current project because the focus is on the Python, Pandas and NumPy concepts I have already studied.

## 20. What did you learn by building this project?

**Answer:** I practised combining Python basics, functions, loops, string cleaning, CSV handling, NumPy and Pandas in one end-to-end data analysis task.
