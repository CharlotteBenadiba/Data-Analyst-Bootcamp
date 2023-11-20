#####Exercise 1

# Function to check if a number is prime
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

# Check if the number 7 is prime
number = 7
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


#####Exercise 2

# Define the range (1 to 20 in this case)
range_start = 1
range_end = 20

# Define the divisor (e.g., 3)
divisor = 3

# Use list comprehension to find numbers divisible by the divisor
divisible_numbers = [number for number in range(range_start, range_end + 1) if number % divisor == 0]

# Print the result
print(f"Numbers in range {range_start} to {range_end} divisible by {divisor}: {divisible_numbers}")


#####Exercise 3

import pandas as pd

# Example with the Iris Dataset
iris_data = pd.read_csv('path_to_iris_dataset.csv')

# Print the first five rows
print(iris_data.head())

# Print the column names
print(iris_data.columns)

# Print the data types
print(iris_data.dtypes)


#####Exercise 4

# Basic data analysis on Boston Housing Dataset
housing_data = pd.read_csv('path_to_boston_housing_dataset.csv')

# Assuming analyzing 'MEDV' column
mean_value = housing_data['MEDV'].mean()
median_value = housing_data['MEDV'].median()
std_dev = housing_data['MEDV'].std()

print(f'Mean: {mean_value}, Median: {median_value}, Standard Deviation: {std_dev}')

