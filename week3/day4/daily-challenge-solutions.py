# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data_science_job_salary.csv')

# Data Normalization - Min-Max normalization of 'salary'
scaler = MinMaxScaler()
data['normalized_salary'] = scaler.fit_transform(data[['salary']])

# Data Reduction - PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data.select_dtypes(include=['float64', 'int64']))

# Data Aggregation - Average and median salary by experience level
aggregated_data = data.groupby('experience_level')['salary'].agg(['mean', 'median'])

# Data Cleaning - Handling missing values and renaming columns
data_clean = data.rename(columns={'job_title': 'Title', 'job_type': 'Type'})
data_clean.fillna(method='ffill', inplace=True)

# Visualization of Aggregated Data
aggregated_data.plot(kind='bar')
plt.title('Average and Median Salary by Experience Level')
plt.ylabel('Salary')
plt.xlabel('Experience Level')
plt.show()

