############ Python program to calculate age in days

# Import the datetime module to work with dates
import datetime

def calculate_age_in_days(birth_date):
    # Get the current date
    current_date = datetime.date.today()
    
    # Calculate the difference between the current date and the birth date
    age_in_days = (current_date - birth_date).days
    
    return age_in_days

# Replace with your birth date
year_of_birth = 1990
month_of_birth = 1
day_of_birth = 1

# Create a date object for the birth date
birth_date = datetime.date(year_of_birth, month_of_birth, day_of_birth)

# Call the function and print the age in days
print("Your age in days is:", calculate_age_in_days(birth_date))

######## Python program to calculate the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Replace with the number you want to find the factorial of
number = 5

# Calculate and print the factorial
print(f"The factorial of {number} is: {factorial(number)}")

############ Python Script to Merge Two Dictionaries

# Define two sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dict2 into dict1
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)

#✅ Knowledge Check Answer Why are Jupyter Notebooks popular in data science? B and C : Jupyter Notebooks are popular in data science primarily because they support the integration of executable code, rich text, and visualizations in a single document (B), and they promote collaboration and reproducibility through easy sharing and remote access (C). While Python is a commonly used language in Jupyter Notebooks, they are not limited to Python and can support other programming languages as well, which makes option A incorrect.
#✅ Knowledge Check: What are the benefits of using Google Colab for collaborative projects?  A and B; A: Google Colab provides free access to GPUs (Graphics Processing Units) and TPUs (Tensor Processing Units), which are essential for high-performance computing tasks, particularly in machine learning and data analysis. B: Google Colab allows users to run Python code in a cloud environment without the need for any local setup. This feature is particularly useful for collaborative projects as it ensures that all collaborators are working in the same environment with the same configurations. C: This option is not correct. Google Colab does not provide exclusive access to Google's internal datasets. However, it does facilitate easy access to datasets available on platforms like Google Drive and GitHub, making it easier to work with external data in collaborative projects.
#✅ Knowledge Check: What makes Kaggle a unique platform for data scientists? A, B and C. Kaggle is unique for data scientists due to its vibrant community collaboration, wide range of real-world data competitions, and extensive access to datasets and shared notebooks.




