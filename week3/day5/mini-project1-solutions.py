import pandas as pd
!pip install kaggle
from google.colab import files
files.upload()
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download osmi/mental-health-in-tech-survey
!unzip mental-health-in-tech-survey.zip

df = pd.read_csv("survey.csv")

# Handling missing values
df.fillna(method='ffill', inplace=True)


# Correcting inconsistencies in gender entries
df['Gender'] = df['Gender'].str.lower()
df['Gender'] = df['Gender'].replace(dict.fromkeys(['male', 'm', 'man'], 'male'))
df['Gender'] = df['Gender'].replace(dict.fromkeys(['female', 'f', 'woman'], 'female'))

# Drop irrelevant columns
df.drop(columns=['Timestamp', 'state', 'self_employed'], inplace=True)

#nan_count = df['treatment'].isna().sum()
#print(f"Number of NaN values in 'treatment': {nan_count}")
#no NaN in treatment

# Age Group Distribution
#categorize ages into bins
age_bins = [0, 18, 25, 35, 45, 55, 65, 75, 85, 95, 105]
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins)

# Group by AgeGroup and treatment, then count and normalize
age_group_dist = df.groupby(['AgeGroup', 'treatment']).size().groupby(level=0).apply(lambda x: x / x.sum())


# Gender-Based Frequency
gender_dist = df.groupby('Gender')['treatment'].value_counts(normalize=True)

# Country-Wise Analysis
country_dist = df.groupby('Country')['treatment'].value_counts(normalize=True)

# Display the results
print("Age Group Distribution of Mental Health Conditions:\n", age_group_dist)
print("\nGender-Based Frequency of Mental Health Issues:\n", gender_dist)
print("\nCountries with Highest and Lowest Reported Rates:\n", country_dist)

-------

