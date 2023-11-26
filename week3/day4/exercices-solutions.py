########################### EXERCISE 1

import pandas as pd

# Load Iris dataset
iris_data = pd.read_csv('path_to_iris.csv')

# Basic exploration
print(iris_data.head())
print(iris_data.describe())
print(iris_data.isnull().sum())


########################### EXERCISE 2
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_data = pd.read_csv('titanic.csv')  # Replace with the correct file path

# Visualize the data distribution for the age column using a box plot
sns.boxplot(x=titanic_data['Age'])
plt.show()

# Identify outliers using Z-score
titanic_data['z_score_age'] = stats.zscore(titanic_data['Age'])
outliers = titanic_data[(titanic_data['z_score_age'] > 3) | (titanic_data['z_score_age'] < -3)]

# Remove outliers for simplicity
cleaned_data = titanic_data[(titanic_data['z_score_age'] <= 3) & (titanic_data['z_score_age'] >= -3)]

# Re-visualize the age column to show the effect of handling the outliers
sns.boxplot(x=cleaned_data['Age'])
plt.show()


###########################EXERCISE 3


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_data = pd.read_csv('path_to_titanic_dataset.csv')  # Replace with the actual file path

# Fill missing values for simplicity
titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
titanic_data['Fare'].fillna(titanic_data['Fare'].mean(), inplace=True)

# Min-Max Normalization
min_max_scaler = MinMaxScaler()
titanic_data['Age_MinMax'] = min_max_scaler.fit_transform(titanic_data[['Age']])
titanic_data['Fare_MinMax'] = min_max_scaler.fit_transform(titanic_data[['Fare']])

# Z-score Normalization
standard_scaler = StandardScaler()
titanic_data['Age_ZScore'] = standard_scaler.fit_transform(titanic_data[['Age']])
titanic_data['Fare_ZScore'] = standard_scaler.fit_transform(titanic_data[['Fare']])

# Plotting histograms
# Original Age Distribution
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.hist(titanic_data['Age'], bins=20, color='blue', alpha=0.7)
plt.title('Original Age Distribution')

# Age after Min-Max Normalization
plt.subplot(2, 2, 2)
plt.hist(titanic_data['Age_MinMax'], bins=20, color='green', alpha=0.7)
plt.title('Age after Min-Max Normalization')

# Original Fare Distribution
plt.subplot(2, 2, 3)
plt.hist(titanic_data['Fare'], bins=20, color='blue', alpha=0.7)
plt.title('Original Fare Distribution')

# Fare after Z-Score Normalization
plt.subplot(2, 2, 4)
plt.hist(titanic_data['Fare_ZScore'], bins=20, color='green', alpha=0.7)
plt.title('Fare after Z-Score Normalization')

plt.tight_layout()
plt.show()




########################### EXERCISE 4
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load Titanic dataset
titanic_data = pd.read_csv('titanic.csv')

# Select numeric columns for PCA
numeric_columns = titanic_data.select_dtypes(include=['float64', 'int64'])
numeric_columns.fillna(numeric_columns.mean(), inplace=True)

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_columns)

# Perform PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# Add the results back to the dataframe
titanic_data['PCA1'] = reduced_data[:, 0]
titanic_data['PCA2'] = reduced_data[:, 1]

# Aggregate data by 'Pclass' and calculate summary statistics
aggregated_data = titanic_data.groupby('Pclass').agg(['mean', 'sum'])

# Visualization of PCA results
plt.figure(figsize=(10, 6))
plt.scatter(titanic_data['PCA1'], titanic_data['PCA2'], c=titanic_data['Pclass'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Titanic Dataset')
plt.colorbar(label='Pclass')
plt.show()

# Visualization of aggregated data
aggregated_data['Survived']['mean'].plot(kind='bar')
plt.title('Average Survival Rate by Pclass')
plt.ylabel('Average Survival Rate')
plt.xlabel('Pclass')
plt.show()



###########################EXERCISE 5
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# Load dataset (update with the correct path)
data = pd.read_csv('your_dataset.csv')

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Implement PCA
pca = PCA(n_components=2)
pca_results = pca.fit_transform(scaled_data)
explained_variance = pca.explained_variance_ratio_

# Implement t-SNE
tsne = TSNE(n_components=2, random_state=0)
tsne_results = tsne.fit_transform(scaled_data)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(pca_results[:, 0], pca_results[:, 1])
plt.title('PCA Results')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.subplot(1, 2, 2)
plt.scatter(tsne_results[:, 0], tsne_results[:, 1])
plt.title('t-SNE Results')
plt.xlabel('t-SNE1')
plt.ylabel('t-SNE2')

plt.show()

# Analysis of results
print("Explained variance by PCA components:", explained_variance)
# Further analysis can be added here based on the results
