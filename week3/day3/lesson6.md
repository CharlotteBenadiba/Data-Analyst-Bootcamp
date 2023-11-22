# Importing Data - An essential skill in any data scientist's toolkit


## What You Will Learn
- In-depth methods for importing data in Jupyter Notebook, Colab, and Kaggle.
- Handling various data formats like CSV, JSON, and Excel.
- Advanced techniques and common challenges in data import.

### Introduction
This comprehensive lesson dives into the world of data import, a foundational skill in data science. We'll explore robust methods for importing data across different platforms like Jupyter Notebook, Colab, and Kaggle, catering to various data formats.

### Prerequisite
- Basic knowledge of Python.
- Basic familiarity with Pandas library.
- A google account to have access to Colab and Google Drive.
- Access to Jupyter Notebook, and Kaggle.

### Preparation
- Install Python and Pandas. (`pip install pandas`)
- Create a Kaggle account if not already done.

### Useful Resources
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Colab Features Overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- [Kaggle Datasets](https://www.Kaggle.com/datasets)
- Previous lessons

---

## Data Import - general notions

Importing data is a crucial step in any data science project. It is the process of loading data from an external source into a local environment. The data can be stored in various formats like CSV, JSON, Excel, etc. and can be accessed from different platforms like Jupyter Notebook, Colab, and Kaggle. This enables data scientists to analyze and use data for multiple purposes like building machine learning models, creating visualizations, and so on.

### 1. **Import a CSV File**:
   A CSV (Comma Separated Values) file is one of the most common data format for storing tabular data. It is a simple text file where each line represents a row and each value is separated by a comma. The first row usually contains the column names. Let's import a CSV file using Pandas and display the first few rows.

   - First download a sample dataset, e.g., [Iris Dataset CSV](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data).
   - Put the csv file in the same folder as your notebook or your python script.
   - We can now read the CSV file and display the first few rows by executing the next code:

   ```python
   import pandas as pd
   iris_data = pd.read_csv('iris.data', header=None)
   print(iris_data.head())
   ```
   The `header=None` argument indicates that the CSV file does not contain column names. If the CSV file contains column names, we can omit this argument.
   `iris_data.head()` displays the first five rows of the dataset. This allows us to quickly inspect the data and verify that it was imported correctly.
   You can also specify the column names by passing a list of strings to the `names` argument. For example, if the CSV file contains the column names "sepal_length", "sepal_width", "petal_length", "petal_width", and "species", we can import the data by executing the following code:
   ```python
   iris_data = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
   print(iris_data.head())
   ```


### 2. **Read Data from a JSON File**:
   - Find a JSON formatted data, such as a sample [JSON dataset](https://jsonplaceholder.typicode.com/posts).
   - Reading and parsing JSON data is very similar to when we did it for a CSV file..

   ```python
   json_data = pd.read_json('https://jsonplaceholder.typicode.com/posts')
   print(json_data.head())
   ```

### 3. **Load Data from an Excel File**:
   - We can use the same method to read an Excel file, like the ones found [here](https://file-examples.com/index.php/sample-documents-download/sample-xls-download/).
   - To import the data, we can use the following code:

   ```python
   excel_data = pd.read_excel('sample_data.xls', index_col=0)
   print(excel_data.head())
   ```
   The `index_col=0` argument indicates that the first column should be used as the index of the dataframe. If the Excel file does not contain an index column, we can omit this argument. Other arguments like `sheet_name` can be used to import data from a specific sheet in the Excel file.

✅ Knowledge Check: Why is Pandas a versatile tool for data import in Python?

🚀 Challenge: Find a version of the Iris dataset that includes column names in the CSV file. Import this dataset and show the initial few rows.

---

## Colab Data Import

You can import data into Colab from local files by uploading them from your computer. To do so, click on the folder icon on the left sidebar and select the file you want to upload. This is a convenient way to import data from your local machine. All examples shown in this lesson can be replicated in Colab by uploading the appropriate files.

Colab also integrates with Google Drive, allowing users to import data from their Google Drive account. This is a convenient way to access data from a shared drive and collaborate with other users. Let's see how we can import data from Google Drive in Colab.

### **Linking Google Drive for Data Access**:
   In order to access data from Google Drive, we need to link our Google Drive account to Colab. This can be done by executing the following code:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
   Then connect your Google Drive account by following the instructions in the pop-up window. Once the connection is established, you can access your Google Drive files from Colab. The folder might not be visible in the left sidebar. To view it, click on the folder icon and select "Refresh" (folder icon with a looping arrow). You should now see a folder named "drive" in the left sidebar.

   You can now access any file in your Google Drive by specifying the path to the file. For example, if you have a CSV file named "iris.data" in the "My Drive" folder, you can import it by executing the following code:
   ```python
   iris_data = pd.read_csv('/content/drive/My Drive/iris.data')
   print(iris_data.head())
   ```

✅ Knowledge Check: Why would you want to import data from Google Drive in Colab instead of putting it in the local environment?

🚀 Challenge: Using the previously found Iris dataset with column names, upload it to your google Google Drive and then import it from a Colab notebook. To confirm that the data was imported correctly, display the first few rows.

---

## Kaggle Data Import

Kaggle hosts a large repository of datasets that can be used for data science projects. It also provides a convenient API for importing datasets directly into a Jupyter Notebook or Colab environment. This is a great way to quickly access datasets for learning and experimentation. Let's see how we can import data from Kaggle in Jupyter Notebook.

### **Using Kaggle's API for Dataset Import**:
   
   First, launch a Jupyter Notebook or Colab environment. Then, install the Kaggle library by executing the following code: 
   ```python
   !pip install Kaggle
   ```
   Next, setup your Kaggle api credentials. This will allow you to download datasets from Kaggle directly into your notebook. To do this, follow these steps:
   1. Go on [Kaggle](https://www.kaggle.com/).
   2. Click on your profile picture on the top right corner.
   3. Click on "My Account".
   4. Scroll down to the section "API" and click on "Create New API Token". This will download a file named "kaggle.json" to your computer.
   5. If you are on Jupyter Notebook, upload the file "Kaggle.json" to the same folder as your notebook. If you are on Colab, upload the file to your environment. You can do this by clicking on the folder icon on the left sidebar and selecting "Upload" (folder icon with an upwards arrow).
   6. Once done you will have to place this file in the folder `~/.kaggle/`. You can do this by executing the following code:
      ```python
      !mkdir -p ~/.kaggle
      !mv Kaggle.json ~/.kaggle/
      ```
      `mkdir -p ~/.kaggle` creates a new folder (if it does not exist already) named ".Kaggle" in the home directory. `mv kaggle.json ~/.kaggle/` moves the file "Kaggle.json" to the newly created folder.

   With this, you have successfully setup your Kaggle API credentials.

   Finally, download a dataset from Kaggle by executing the following code:
   ```python
   !Kaggle datasets download -d uciml/iris
   ```
   This will download the dataset "iris" from Kaggle and save it in the current directory in a zip file named "iris.zip". You can now unzip the file and import the CSV file into a Pandas dataframe by executing the following code:
   ```python
   !unzip iris.zip
   ```
   You should now see a CSV file named "Iris.csv" in the current directory. You can import it into a Pandas dataframe by executing the following code:
   ```python
   iris_data = pd.read_csv('Iris.csv')
   ```




✅ Knowledge Check: What are the benefits of using Kaggle's datasets in data science projects?

#### Conclusion
We covered the process of importing data in Jupyter Notebook, and Colab, tackling data from multiple sources including the local machine, Google Drive, and Kaggle. We also explored various data formats like CSV, JSON, and Excel This foundational knowledge is crucial for anyone aspiring to effectively manage and analyze data.

---
