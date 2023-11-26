# Import necessary library
import pandas as pd

# Load the CSV dataset
csv_file_path = 'your_dataset.csv'  # Replace with your CSV file path
data = pd.read_csv(csv_file_path)

# Data Cleaning
data = data.dropna()  # Remove missing values
data.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)  # Rename a column

# Export to Excel
data.to_excel('cleaned_data.xlsx', index=False)

# Re-import from Excel
excel_data = pd.read_excel('cleaned_data.xlsx')

# Save a subset to JSON
subset = excel_data.head(5)  # Example: taking the first 5 rows
subset.to_json('subset_data.json', orient='records', lines=True)

print("Data import, cleaning, export, and re-import operations completed.")
