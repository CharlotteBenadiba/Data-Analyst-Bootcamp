# Lesson: Data Transformation

## Table of Contents
1. Data Integration
2. Data Normalization
3. Data Reduction
4. Data Aggregation

---

## 1. Data Integration

### What is Data Integration?
Data integration involves combining data from different sources into a unified dataset. It helps gather more information and context for analysis and modeling.

### Example: Integrating Data with Titanic Dataset
Let's say we have additional data about passengers' demographics and we want to integrate it with the Titanic dataset. Here's how to do it:
```python
# Load additional dataset (hypothetical example)
passenger_demographics = pd.read_csv('passenger_demographics.csv')

# Perform data integration (merge datasets on a common key)
integrated_data = pd.merge(titanic_data, passenger_demographics, on='PassengerId', how='left')

# Explore the integrated dataset
print(integrated_data.head())
```
✅ Knowledge Check : What is the common key used for merging the Titanic dataset with the additional demographic data in the example?
    A. 'PassengerName'
    B. 'Age'
    C. 'TicketNumber'
    D. 'PassengerId'

## 2. Data Normalization
### What is Data Normalization?

Data normalization is the process of rescaling data to have values between 0 and 1. It helps bring data on different scales to a standard scale, making it easier to compare and analyze.
Example: Min-Max Normalization

Here's how to perform min-max normalization on a numerical column, e.g., 'Age':
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
titanic_data['Age_normalized'] = scaler.fit_transform(titanic_data[['Age']])
```
After running this code, the 'Age' column in the titanic_data DataFrame will be replaced by the 'Age_normalized' column, which contains the Min-Max normalized values of the ages of passengers in the Titanic dataset. These normalized values will range between 0 (minimum age) and 1 (maximum age), making it easier to compare and analyze the 'Age' data alongside other features that may have different scales.

✅ Knowledge Check : What is the purpose of Min-Max normalization?

## 3. Data Reduction
### What is Data Reduction?

Data reduction involves reducing the volume but producing the same or similar analytical results. It helps in handling large datasets efficiently.

Example: Principal Component Analysis (PCA)

PCA is a technique for data reduction. It reduces the number of features (or dimensions) in a dataset while preserving the most important information. This is particularly useful when dealing with high-dimensional data or when you want to simplify a dataset for easier analysis.
Here's how to apply PCA to reduce the dimensionality of a dataset:
```python

from sklearn.decomposition import PCA

#This line creates an instance of the PCA class with the parameter n_components set to 2. It specifies that we want to reduce the dimensionality of the data to 2 principal components. In other words, the data will be projected into a 2D space.
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(original_data)

```
This code performs dimensionality reduction using PCA, reducing the original_data to a 2D representation in reduced_data by retaining the most important information captured by the first two principal components.

✅ Knowledge Check : In the provided code, what does the 'reduced_data' variable represent after applying PCA with two components?

---
## 4. Data Aggregation
### What is Data Aggregation?

Data aggregation involves combining multiple data points into a single data point to simplify analysis. It is often used in summarizing and reporting data.

Example: Aggregating Sales Data

Let's say we have daily sales data and want to aggregate it to monthly sales. Here's how to do it:

```python
monthly_sales = sales_data.groupby(pd.Grouper(freq='M')).sum()
```

✅ Knowledge Check : When might data aggregation be useful in data analysis?

 ---
 🚀 Challenge : Short-term Daily Precipitation Forecasting

Dataset Description:
- Dataset Link: [Short-term Daily Precipitation Forecasting](https://www.kaggle.com/muthuj7/weather-dataset)
- This dataset contains daily precipitation forecasts for multiple locations.

Data Integration
1. Load the "Short-term Daily Precipitation Forecasting" dataset.
2. Explore the dataset and understand its structure.
Data Normalization
1. Perform Min-Max normalization on the precipitation values.
2. Create a new column, e.g., "Precipitation_normalized," to store the normalized values.
Data Reduction
1. Apply Principal Component Analysis (PCA) to reduce the dimensionality of the dataset.
2. Reduce the dataset to a 2D representation using PCA.
Data Aggregation
1. Group the data by location and calculate the average precipitation for each location.
2. Create a new dataset with the aggregated values.

 
 Data transformation is a crucial step in data preprocessing and analysis. It includes data integration, normalization, reduction, and aggregation, each serving a specific purpose in preparing data for meaningful insights and modeling.
