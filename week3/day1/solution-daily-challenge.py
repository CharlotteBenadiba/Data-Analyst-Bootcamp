import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

!pip install kaggle
#import kaggle
from google.colab import files
files.upload()
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download osmi/mental-health-in-tech-survey
!unzip mental-health-in-tech-survey.zip

titanic_data = pd.read_csv('train.csv')

#Data Exploration
print("Data Structure:")
print(titanic_data.info())

#Get Basic Statistics for Quantitative Data
print("\nBasic Statistics for Quantitative Data:")
print(titanic_data.describe())

#Analyze Data Types in the Dataset
print("\nData Types in the Dataset:")
print(titanic_data.dtypes)

#Identify Qualitative and Quantitative Data Columns
qualitative_columns = titanic_data.select_dtypes(include=['object']).columns
quantitative_columns = titanic_data.select_dtypes(include=['float64', 'int64']).columns
print("\nQualitative Data Columns:")
print(qualitative_columns)
print("\nQuantitative Data Columns:")
print(quantitative_columns)

#Calculate and print the survival rate.
print("\nDescriptive Analysis:")
survival_rate = titanic_data['Survived'].mean() * 100
print(f"Survival Rate: {survival_rate:.2f}%")

#Analyze and print the class distribution.
class_distribution = titanic_data['Pclass'].value_counts()
print("\nClass Distribution:")
print(class_distribution)

#Visualize survival count by class and by gender.
print("\nDiagnostic Analysis:")
sns.catplot(x="Pclass", hue="Survived", kind="count", data=titanic_data)
plt.title("Survival Count by Class")
plt.show()

sns.catplot(x="Sex", hue="Survived", kind="count", data=titanic_data)
plt.title("Survival Count by Gender")
plt.show()

