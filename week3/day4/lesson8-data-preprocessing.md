# Lesson 8 : Data Preprocessing

Data preprocessing is a fundamental step in any data science project. It involves preparing and cleaning raw data to make it suitable for analysis and modeling. 
In this lesson, using the Titanic dataset as an example, we'll explore the essential steps of data preprocessing : 
- Gathering and exploring the Data
- Data Integration
- Data Cleaning


---
## Topic 1: Data Gathering and Exploration

### Why Data Preprocessing?

Data preprocessing is crucial because raw data is often messy and contains errors, missing values, and inconsistencies. Proper data preprocessing ensures that we have high-quality data for analysis, which leads to more accurate insights and models.

### Gathering Data

The first step in data preprocessing is to gather the data. In our example, we'll use the Titanic dataset from Kaggle. Here's how to download it using the Kaggle API:

```python
!pip install kaggle
import kaggle

# Set your Kaggle API credentials
kaggle.api.authenticate(api_key='your_api_key_here')

# Download the Titanic dataset
kaggle.api.dataset_download_files('heptapod/titanic', path='.', unzip=True)
```

### Exploring the Data

After gathering the data, we need to explore it to understand its structure and contents. This includes examining columns, data types, and any missing values. Here's how to load and explore the Titanic dataset:

```python
import pandas as pd

# Load the Titanic dataset
titanic_data = pd.read_csv('train.csv')

# Explore the dataset
print(titanic_data.head())
print(titanic_data.info())
```

✅ Knowledge Check:

1. Why is data preprocessing important in the context of data analysis and modeling?
   - A) To make data gathering faster.
   - B) To introduce errors intentionally.
   - C) To ensure high-quality data for accurate insights and models.
   - D) To skip the data exploration step.
2. What is the purpose of exploring the data after gathering it?
   - A) To make the data larger.
   - B) To add inconsistencies to the data.
   - C) To understand the data's structure and contents, including columns, data types, and missing values.
   - D) To immediately build machine learning models.

Please select the correct answers by marking the appropriate option for each question (e.g., "1 - C, 2 - B, 3 - A, 4 - C").

---

## Topic 2: Data Integration

What is Data Integration?

Data integration involves combining data from different sources into a unified dataset. It helps gather more information and context for analysis and modeling.

Example: Integrating Data with Titanic Dataset

Let's say we have additional data about passengers' demographics and we want to integrate it with the Titanic dataset. Here's how to do it:
```python
# Load additional dataset (hypothetical example)
passenger_demographics = pd.read_csv('passenger_demographics.csv')

# Perform data integration (merge datasets on a common key)
integrated_data = pd.merge(titanic_data, passenger_demographics, on='PassengerId', how='left')

# Explore the integrated dataset
print(integrated_data.head())
```
✅ Knowledge Check:
1. In the provided code example, what is the common key used to merge the Titanic dataset with the passenger demographics dataset?
   - A) 'Name'
   - B) 'Age'
   - C) 'Ticket'
   - D) 'PassengerId'

2. What is the purpose of the 'how' parameter in the `pd.merge()` function?
   - A) To specify the column to merge on.
   - B) To indicate whether to perform a left, right, inner, or outer merge.
   - C) To control the sorting of the merged dataset.
   - D) To filter out specific rows during the merge operation.

---

## Topic 3: Data Cleaning

Data cleaning is the process of identifying and correcting errors and inconsistencies in the dataset. It involves several sub-steps:
  - Removing Duplicates
  - Removing Irrelevant Data
  - Fixing Structural Errors
  - Identifying Missing Values
  - Handling Missing Values
  - Handling Outliers

### Removing Duplicates
Duplicate rows can distort analysis results. Here's how to remove duplicates from the Titanic dataset using the `drop_duplicates()`:
```python
# Remove duplicate rows
titanic_data = titanic_data.drop_duplicates()

# Verify duplicates are removed
print(titanic_data.duplicated().sum())
```

### Removing Irrelevant Data

Sometimes, certain columns are irrelevant to the analysis. We can drop these columns using the `drop` function:

```python
# Remove irrelevant columns (e.g., 'Cabin' and 'Ticket')
titanic_data = titanic_data.drop(['Cabin', 'Ticket'], axis=1)
```

### Fixing Structural Errors

Structural errors include data format issues. We may need to address these, such as converting dates:
```python
# Convert 'Date' column to datetime format
titanic_data['Date'] = pd.to_datetime(titanic_data['Date'])
```

### Identifying Missing Values

Identifying missing values is the first step in handling them. The isnull() function in Pandas returns a DataFrame of the same shape as the input, with True where the data is missing and False where it is not.
   
   ```python
   import pandas as pd

   # Check for missing values in a DataFrame
   missing_data = df.isnull()
   print(missing_data.head())

   # Count missing values in each column
   missing_counts = df.isnull().sum()
   print(missing_counts)
```

### Handling Missing Values

Missing values need to be addressed. Depending on your problem, there is multiple solutions to handle them : 
- Removing Missing Data : we use this approach when the missing values are relatively few, randomly distributed, and removing them does not significantly reduce the size of the dataset.
- Imputation : we perform imputation when you want to retain as much data as possible, especially if the missing values contain valuable information.
- Advanced Imputation Techniques : it can be used when simple imputation methods like mean, median, or mode imputation are not suitable. In this case we use regression imputation, k-nearest neighbors imputation, or machine learning-based imputation (we will dive in this methods in a few weeks).

We will see below how to use them :

Removing Missing Data
In some cases, removing rows or columns with missing data may be a viable option. However, this should be done judiciously, as it can result in loss of valuable information.
```python
# Remove rows with missing values
df_cleaned = df.dropna()

# Remove columns with missing values
df_cleaned = df.dropna(axis=1)

```
✅ Knowledge Check: In which situations might removing rows with missing data be a good approach?
  A. When dealing with time-series data.
  B. When the dataset is too small.
  C. When missing values are concentrated in specific columns.
  D. When imputation is preferred.

Imputation
Imputation involves filling in missing values with estimated or calculated values using `fillna`function.
```python
# Fill missing values with a specific value (e.g., 0)
df_filled = df.fillna(0)

# Fill missing values with the mean of the column
df_filled = df.fillna(df.mean())

```
✅ Knowledge Check: When might it be appropriate to fill missing values with a specific value like 0?

Advanced Imputation Techniques
Advanced methods like predictive modeling or machine learning can be used for imputation when data has complex dependencies.
```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=2)
df_imputed = imputer.fit_transform(df)
```

### Handling Outliers

Outliers are data points that significantly differ from the majority of the data in a dataset. They are extreme values that fall far above or below the typical range of values observed in the dataset. Outliers can skew the results of statistical analyses and machine learning models, leading to inaccurate or biased conclusions. Therefore, it is essential to identify and handle outliers appropriately in data preprocessing.
In the provided code snippet, we are focusing on handling outliers in the 'Fare' column of the Titanic dataset:
```python
# Identify and handle outliers in 'Fare' column
Q1 = titanic_data['Fare'].quantile(0.25)
Q3 = titanic_data['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
titanic_data = titanic_data[(titanic_data['Fare'] >= lower_bound) & (titanic_data['Fare'] <= upper_bound)]
```
Quantiles (Q1 and Q3):
    Quantiles are values that divide a dataset into specific parts. In this case, we calculate the first quartile (Q1) and the third quartile (Q3) for the 'Fare' column.
    Q1 represents the 25th percentile, which is the value below which 25% of the data falls.
    Q3 represents the 75th percentile, which is the value below which 75% of the data falls.

Interquartile Range (IQR):
    The interquartile range (IQR) is a measure of the spread of data between the first quartile (Q1) and the third quartile (Q3).
    It is calculated as IQR=Q3−Q1IQR=Q3−Q1.

Lower and Upper Bounds:
    To identify potential outliers, we define lower and upper bounds based on the IQR.
    The lower bound is calculated as lower_bound=Q1−1.5⋅IQRlower_bound=Q1−1.5⋅IQR.
    The upper bound is calculated as upper_bound=Q3+1.5⋅IQRupper_bound=Q3+1.5⋅IQR.

Filtering Outliers:
    Finally, we filter the data to include only those rows where the 'Fare' value is within the bounds defined by the lower and upper bounds.
    Rows with 'Fare' values below the lower bound or above the upper bound are considered outliers and are removed from the dataset.

🚀 Challenge : Identify Outliers
1. Calculate the first quartile (Q1) and the third quartile (Q3) for the 'Age' column in the Titanic dataset.
2. Compute the interquartile range (IQR) for the 'Age' column.
3. Define the lower bound and upper bound for potential outliers based on the IQR.
4. Identify and count the number of outliers in the 'Age' column if there is.
---
