## Exercise 1: Introduction to Data Analysis (Easy)

### Objective: Understand the basic overview and significance of data analysis.

### Task:

Write a short essay or report on the following topics:
  - What is data analysis?
  - Why is data analysis important in modern contexts?
  - List and describe three areas where data analysis is applied today.

---

## Exercise 2: Exploring Data Types (Easy)

### Objective: Learn about different types of data in data analysis.

### Task:

- Load the Iris dataset using Kaggle into a Jupyter Notebook or Google Colaboratory Notebook.
- Identify and list which columns in your dataset are qualitative and which are quantitative.
- Write a brief description of why each column is classified as qualitative or quantitative.

Tools: Jupyter Notebook, Python with Pandas library.

---

## Exercise 3: Basic Data Analysis with Google Colab (Easy)

### Objective: Perform basic data analysis using Google Colab.

### Task:

- Using the same notebook from the previous exercise, perform basic data analysis tasks:
  - Calculate the mean, median, and mode of a quantitative column.
  - Create a simple plot (like a histogram or bar chart) to visualize the data using Matplotlib/Seaborn libraries :
    ```python
    import matplotlib.pyplot as plt
    plt.plot(data['Name_column1'], data['Name_column2'])
    plt.show()
    ```
  - Document your findings in the notebook.

Tools: Google Colab, Python with Pandas and Matplotlib/Seaborn libraries.

---

## Exercise 4: Synthetic Data Generation (Medium)

### Objective: Generate fake data using Faker

### Task:
- Generate fake names, adress, email and birth dates using `Faker`.
- Create Customized User Profiles and save them to CSV
- Print the generated data.

### Hint 

to save the profiles into a csv file :
```python
with open('user_profiles.csv', mode='w', newline='', encoding='utf-8') as file:
  writer = csv.DictWriter(file, fieldnames=['name', 'mail', 'birthdate', 'address', 'company'])
  writer.writeheader()
  for profile in profiles:
    writer.writerow(profile)
```

---
## Exercise 5: Transforming Qualitative Data into Quantitative Data with the Titanic Dataset

- Download the Titanic dataset from a source like Kaggle or any other open data platform.
- Load the dataset into a Python environment using Pandas.
- Transform the sex column, to represent 0 as 'female' and 1 for 'male' using `.map` function.

---

## Exercise 6: Exploratory Data Analysis (Hard)

### Objective: Implement a data-driven decision-making process.
Exploratory Data Analysis (EDA) is a process in data analysis where various techniques are used to understand, summarize, and visualize the underlying structure and characteristics of a dataset. 

### Task:

Follow the steps of EDA on [this medium post](https://medium.com/@ugursavci/complete-exploratory-data-analysis-using-python-9f685d67d1e4)

