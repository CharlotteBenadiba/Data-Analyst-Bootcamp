################# Exercise 1

def print_essay():
    # Part 1: What is data analysis?
    data_analysis_definition = """
    Data analysis is the process of inspecting, cleansing, transforming, and modeling data 
    with the goal of discovering useful information, informing conclusions, and supporting 
    decision-making. It involves applying statistical and logical techniques to evaluate and 
    interpret data, extract meaningful insights, and generate actionable knowledge.
    """

    # Part 2: Why is data analysis important in modern contexts?
    importance_in_modern_contexts = """
    In today's data-driven world, data analysis has become vital for understanding complex 
    systems, making decisions, and solving problems. It helps businesses and organizations 
    make informed decisions based on empirical evidence and trends identified from data. 
    From optimizing processes to understanding customer preferences and predicting future trends, 
    data analysis is essential for staying competitive and efficient in a rapidly evolving global market.
    """

    # Part 3: Areas where data analysis is applied today
    application_areas = """
    1. Business Intelligence: Companies use data analysis for market research, understanding 
    customer behavior, and improving decision-making processes.

    2. Healthcare: Data analysis helps in medical research, diagnosis optimization, and treatment 
    effectiveness assessment, leading to better patient care and health management.

    3. Government and Public Policy: Governments use data analysis for urban planning, resource 
    management, policy formulation, and to enhance the quality of life of their citizens.
    """

    # Print the essay
    print("Essay on Data Analysis\n")
    print("What is Data Analysis?")
    print(data_analysis_definition)
    print("Why is Data Analysis Important in Modern Contexts?")
    print(importance_in_modern_contexts)
    print("Areas Where Data Analysis is Applied Today")
    print(application_areas)

# Run the function to print the essay
print_essay()




################# Exercise 2
# Import necessary library
import pandas as pd

# Load the Iris dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv(url, names=columns)

# Display the first few rows of the dataset
print(iris_data.head())

# Identifying and listing data types
data_types = iris_data.dtypes
print("\nData Types in the Iris Dataset:")
print(data_types)

# Describing why each column is qualitative or quantitative
print("\nDescription of Data Types:")

for column in iris_data.columns:
    if iris_data[column].dtype == 'object':
        print(f"{column} is qualitative (categorical) because it represents a category or class.")
    else:
        print(f"{column} is quantitative (numerical) because it represents a measurement.")


################# Exercise 3

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset to understand its structure
print(iris.head())

# Basic Data Analysis Tasks
# Calculate mean, median, and mode of a quantitative column (e.g., petal_length)
mean_petal_length = iris['petal_length'].mean()
median_petal_length = iris['petal_length'].median()
mode_petal_length = iris['petal_length'].mode()[0]

print(f"Mean of Petal Length: {mean_petal_length}")
print(f"Median of Petal Length: {median_petal_length}")
print(f"Mode of Petal Length: {mode_petal_length}")

# Create a simple plot to visualize the data
# Histogram of petal length
plt.figure(figsize=(8, 6))
sns.histplot(iris['petal_length'], kde=True)
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of petal length vs petal width
plt.figure(figsize=(8, 6))
plt.scatter(iris['petal_length'], iris['petal_width'])
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

# Documenting Findings
# The mean, median, and mode provide a basic understanding of the central tendency of petal length.
# The histogram shows the distribution of petal length across the Iris dataset.
# The scatter plot visualizes the relationship between petal length and petal width.


################# Exercise 4
# Import necessary libraries
from faker import Faker
import csv

# Create a Faker instance
fake = Faker()

# Task 2: Generating Basic Data
names = [fake.name() for _ in range(10)]
addresses = [fake.address() for _ in range(10)]
emails = [fake.email() for _ in range(10)]
birth_dates = [fake.date_of_birth() for _ in range(10)]

# Task 3: Creating Customized User Profiles
profiles = [fake.profile(fields=['name', 'mail', 'birthdate', 'address', 'company']) for _ in range(5)]

# Task 4: Data Export - Save profiles to CSV
with open('user_profiles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'mail', 'birthdate', 'address', 'company'])
    writer.writeheader()
    for profile in profiles:
        writer.writerow(profile)


# Print generated data for verification
print("Sample Names:", names)
print("Sample Addresses:", addresses)
print("Sample Emails:", emails)
print("Sample Birth Dates:", birth_dates)
print("\nCustomized User Profiles:")
for profile in profiles:
    print(profile)





################# Exercise 5

import numpy as np # linear algebra
import pandas as pd # data manipulation and analysisimport matplotlib.pyplot as plt # data visualization
import seaborn as sns # data visualizationsns.set_style('whitegrid') # set style for visualizationimport warnings # ignore warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('insurance.csv')
df.head()
df.info()
df.shape()
df.columns
df.describe()
df.describe(include='O')
list(df.sex.unique())
df.isnull().sum()
df[df.duplicated(keep='first')]
df.drop_duplicates(keep='first',inplace=True)
plt.figure(figsize=(10,6))
sns.distplot(df.charges,color='r')
plt.title('Charges Distribution',size=18)
plt.xlabel('Charges',size=14)
plt.ylabel('Density',size=14)
plt.show()
plt.figure(figsize=(10,6))
sns.histplot(df.age)
plt.title('Age Distribution',size=18)
plt.xlabel('Age',size=14)
plt.ylabel('Count',size=14)
plt.show()
plt.figure(figsize=(10,6))
plt.hist(df.bmi,color='y')
plt.title('BMI Distribution',size=18)
plt.show()
plt.figure(figsize = (10,6))
sns.boxplot(df.charges)
plt.title('Distribution Charges',size=18)
plt.show()
Q1 = df['charges'].quantile(0.25)
Q3 = df['charges'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df[(df['charges']< Q1-1.5* IQR) | (df['charges']> Q3+1.5* IQR)]
plt.figure(figsize=(10,6))
sns.countplot(x = 'sex', data = df)
plt.title('Total Number of Male and Female',size=18)
plt.xlabel('Sex',size=14)
plt.show()
plt.figure(figsize = (10,6))
sns.countplot(df.children)
plt.title('Children Distribution',size=18)
plt.xlabel('Children',size=14)
plt.ylabel('Count',size=14)
plt.show()
plt.figure(figsize = (10,6))
sns.countplot(df.smoker)
plt.title('Smoker Distribution',size=18)
plt.xlabel('Smoker',size=14)
plt.ylabel('Count',size=14)
plt.show()
df.smoker.value_counts()
plt.figure(figsize = (10,6))
sns.countplot(df.region,palette='Blues')
plt.title('Region Distribution',size=18)
plt.xlabel('Region',size=14)
plt.ylabel('Count',size=14)
plt.show()


plt.figure(figsize = (10,6))
sns.countplot(df.region,palette='Blues')
plt.title('Region Distribution',size=18)
plt.xlabel('Region',size=14)
plt.ylabel('Count',size=14)
plt.show()

plt.figure(figsize = (10,6))
sns.scatterplot(x='age',y='charges',color='r',data=df)
plt.title('Age vs Charges',size=18)
plt.xlabel('Age',size=14)
plt.ylabel('Charges',size=14)
plt.show()
print('Correlation between age and charges is : {}'.format(round(df.corr()['age']['charges'],3)))
plt.figure(figsize = (10,6))
sns.set_style('darkgrid')
sns.boxplot(x='smoker',y='charges',data=df)
plt.title('Smoker vs Charges',size=18);
sns.pairplot(df, 
                 markers="+",
                 diag_kind="kde",
                 kind='reg',
                 plot_kws={'line_kws':{'color':'#aec6cf'}, 
                           'scatter_kws': {'alpha': 0.7, 
                                           'color': 'red'}},
                 corner=True);
plt.figure(figsize = (10,6))
sns.heatmap(df.corr(),annot=True,square=True,
            cmap='RdBu',
            vmax=1,
            vmin=-1)
plt.title('Correlations Between Variables',size=18);
plt.xticks(size=13)
plt.yticks(size=13)
plt.show()



