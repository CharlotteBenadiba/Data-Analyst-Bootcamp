# Exercises 

## Exercise 1 : Import a file from Kaggle (easy)

- Import the titanic dataset.
- Print the first few rows of the DataFrame.

---

## Exercise 2 : Export a dataframe to excel format and JSON format (easy)

- Create a simple dataframe.
- Export the dataframe to an excel file.
- Export the dataframe to a JSON file.

---

## Exercise 3 : Export a dataframe to JSON with orient (easy)

- Export the dataFrame to JSON with different orientations using this data :
  ```python
  data = {
    'UserID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 
             'Frank', 'Grace', 'Hannah', 'Ian', 'Jane'],
    'Age': [25, 30, 35, 40, 29, 34, 28, 31, 36, 33],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}```

---

## Exercise 4 :  Export a dataframe from excel (easy)

- Take this dataframe :
  ```python
  data = pd.DataFrame({
    'Date': pd.date_range('20210101', periods=20),
    'Product': ['Product A', 'Product B', 'Product C'] * 6 + ['Product A', 'Product B'],
    'Quantity': [2, 3, 5, 7, 1] * 4,
    'Revenue': [210.50, 340.60, 450.30, 120.10, 150.75] * 4
})```

- Create a new Excel workbook and sheet.
- Add data to the sheet.
- Set number format for Revenue and Quantity.
- Apply a header formatting.
- Set number format for Revenue and Quantity.
- Auto-adjust columns' width using `column_dimensions`.

---

## Exercise 5 : Chunking Large Datasets (medium)

  - Import a large dataset in CSV format for example this [one](https://www.kaggle.com/competitions/riiid-test-answer-prediction/data)
  - Write a Python script using Pandas to read the dataset in chunks.
  - For each chunk, perform a basic operation (e.g., calculate the sum of a column).
  - Append each chunk's results to an output CSV file.
For example : 

  ```python
  for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    chunk.to_csv('output_chunk.csv', mode='a')
  ```

---
## Exercise 6 : Using Efficient File Formats (medium)

- Re-use the same large DataFrame in your Python environment from exercise 5.
- Export the DataFrame into a Parquet file.
- Note the difference in file size and read/write speeds compared to CSV format.

Code Example:
```python
large_df.to_parquet('large_data.parquet')
```

---

## Exercise 7 : Database Integration with SQL (Hard)

- Set up this SQL database [SQL Murder Mystery Database](https://www.kaggle.com/datasets/johnp47/sql-murder-mystery-database).
- Export the merged DataFrame to a SQL database, using an efficient bulk insert operation.
- Perform a SQL query to retrieve a subset of the data and export this subset back into a different file format (e.g., Excel).

Hint : [Getting Started with SQLAlchemy](https://medium.com/geekculture/getting-started-with-sqlalchemy-d132d04c940)


