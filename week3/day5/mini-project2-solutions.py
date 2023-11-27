# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Wine Quality dataset
wine_data = pd.read_csv('winequality.csv')

# Data exploration
print(wine_data.head())
print(wine_data.describe())

# Data cleaning
# Handle missing values
wine_data.dropna(inplace=True)

# Analyze chemical properties and their correlation with wine quality
correlation = wine_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation between Variables')
plt.show()

# Compare quality of red and white wines
# Note: Assuming 'wine_type' column distinguishes between red and white wines
sns.boxplot(x='wine_type', y='quality', data=wine_data)
plt.title('Wine Quality by Type')
plt.show()

