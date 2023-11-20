# Learn How to Use Jupyter Notebook, Google Colab, and Kaggle

## What you will learn

- Basic operations in Jupyter Notebook
- How to utilize Google Colab for collaborative projects
- Navigating and participating in Kaggle competitions

### Introduction

This lesson covers the essentials of Jupyter Notebook, Google Colab, and Kaggle. You'll learn how to perform basic operations in Jupyter Notebook, use Google Colab for collaborative data science projects, and navigate Kaggle to participate in data science competitions.

### Prerequisite

* Familiarity with basic programming concepts
* Understanding of Python programming language

### Preparation

* [Install Anaconda for Jupyter Notebook](https://noteable.io/jupyter-notebook/install-jupyter-notebook/) and scroll down to the Operating System you are using (Apple, Windows or Linux).
* Create accounts on Google.

### Useful resources

* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
* [Google Colab FAQs](https://research.google.com/colaboratory/faq.html)
* [Kaggle Competitions](https://www.kaggle.com/competitions)

---

## Jupyter Notebook Basics

### Task:

Learn to create, run, and save a Jupyter Notebook. Follow these steps:

1. **Opening Jupyter Notebook**:
    - After installing Anaconda, open the Anaconda Navigator.
    - Click on the Jupyter Notebook icon to launch it. This will open a new tab or window in your default web browser with the Jupyter Notebook interface.
If you installed Jupyter Notebook with pip, type the command "jupyter notebook" in a terminal to open the interface. 

2. **Creating a New Notebook**:
    - In the Jupyter Notebook interface, navigate to the directory where you want to create the notebook.
    - Click on the “New” button at the top right and select “Python 3” from the dropdown. This will create and open a new notebook.

3. **Writing Code**:
    - In the new notebook, you'll see a cell where you can start typing your Python code.
    - Enter the following code in the cell:
        ```python
        # Simple Python code to display text
        print("Hello, Jupyter!")
        ```
    - This is a simple Python command that prints out the text "Hello, Jupyter!".

4. **Running the Code**:
    - To run the code, press `Shift + Enter` or click the "Run" button in the toolbar. 
    - The output of the code will appear immediately below the cell.

5. **Saving the Notebook**:
    - To save your work, go to the File menu and select "Save and Checkpoint", or click on the floppy disk icon in the toolbar.
    - Give your notebook a meaningful name by clicking on the notebook title at the top (next to the Jupyter logo) and typing in your preferred name.

6. **Closing the Notebook**:
    - When you're done, you can close the browser tab.
    - To shut down the notebook server, go back to the terminal where you launched Jupyter Notebook and press `Ctrl + C`.


✅ Knowledge Check: Why are Jupyter Notebooks popular in data science? 

- [ ] A. They only allow Python code execution, which is a widely used language in data science.
- [ ] B. They enable users to combine executable code, rich text, visualizations, equations, and other media.
- [ ] C. They can be easily shared and accessed remotely, facilitating collaboration and reproducibility in research.

Check all that apply. You can find the answers at the end of the lesson.

🚀 Challenge: Create a new Jupyter Notebook and write a simple Python program to calculate and display your age in days. Import `datetime`. Solution: 'age_in_days.py'

#### Exercise in class

Write a Python program to calculate the factorial of a number on Jupyter Notebook. Solution: `factorial.py`

---

## Google Colab Introduction

### Task: Create and Share a Google Colab Notebook

In this task, you will learn how to use Google Colab by creating a new notebook, writing some Python code, and then sharing it with a peer for collaboration. Follow these steps:

#### Step 1: Open Google Colab and Start a New Notebook

1. Navigate to [Google Colab](https://colab.research.google.com/).
2. Sign in with your Google account and go to your drive.
3. Click on `New`button at the top left and go to `More`then select `Google Colaboratory` to create a fresh notebook.
4. Rename the notebook to something relevant, like "First Colab Experiment." by clicking on the "Untitled.py" at the top left.

#### Step 2: Write Simple Python Code

1. In the first cell of the notebook, write a Python comment with your name and the date, e.g., `# Created by [Your Name] on [Date]`.
2. Below the comment, write a simple Python code, for example:

   ```python
   # Print a welcome message
   print("Hello, Google Colab!")

3. Run the cell by clicking the play button on the left side of the cell or by pressing `Shift + Enter`.
4. In Google Collab, there is two types of cells : `Text` cells and `Code cells`. To  add a `Text` cell, you click on "+Text" at the right top. It can be useful to write comments or titles in the Notebook.

#### Step 3: Share the Notebook with a Peer

1. Click on the `Share` button located at the top right corner of the notebook.
2. Enter the email address of your peer or generate a shareable link.
3. Set the sharing permissions to either `Viewer` or `Editor` based on your preference.
4. Send the link to your peer and ask them to open it.

#### Step 4: Understanding GPUs and TPUs

What is a GPU?

- **GPU** stands for **Graphics Processing Unit**.
- It's specialized hardware designed originally for rendering graphics.
- In data science, GPUs are used for parallel processing, significantly speeding up tasks like machine learning and deep learning.
- GPUs are well-suited for computations that can be run in parallel, making them efficient for algorithms where tasks can be processed simultaneously.

What is a TPU?

- **TPU** stands for **Tensor Processing Unit**.
- Developed by Google, TPUs are custom-built for machine learning tasks.
- They are designed to accelerate neural network computations specifically.
- TPUs are highly efficient in terms of speed and power consumption for tasks like training and running machine learning models.

How to Modify GPU/TPU Settings in Google Colab

1. **Selecting the Runtime Type**:
   - In your Google Colab notebook, go to the menu bar and click on `Runtime`.
   - Choose `Change runtime type` from the dropdown menu.

2. **Changing the Hardware Accelerator**:
   - In the `Runtime type` settings, you'll find the `Hardware accelerator` dropdown.
   - Select `GPU` or `TPU` based on your requirements.
   - Click `Save` to apply the changes.

3. **Utilizing the GPU/TPU in Code**:
   - After changing the settings, your notebook will have access to the selected hardware.
   - You can now write code that leverages the GPU or TPU for faster computations.

Benefits:

- Using GPUs and TPUs can drastically reduce the time required for training complex machine learning models.
- They enable the processing of larger datasets that might be impractical on standard CPUs.
- Google Colab provides access to these resources for free, making advanced computations accessible to a wider audience.

Remember, while TPUs are faster for certain tasks, they require specific types of models and code adjustments to fully utilize their capabilities.


✅ Knowledge Check: What are the benefits of using Google Colab for collaborative projects?

- [ ] A. Access to free GPUs and TPUs for computing.
- [ ] B. Ability to run Python code in the cloud without any setup.
- [ ] C. Exclusive access to Google's internal data sets.

Check all that apply. You can find the answers at the end of the lesson.

🚀 Challenge: Collaboratively write a Python script to sort a list of numbers in a shared Google Colab notebook.

#### Exercise in class

Write a Python script to merge two dictionaries. Solution: `merge_dictionaries.py`

---

## Kaggle Competition: Titanic - Machine Learning from Disaster

This lesson focuses on accessing the "Titanic: Machine Learning from Disaster" competition on Kaggle using Google Colab. This competition is ideal for beginners and involves predicting the survival of passengers based on various features.

### Task:

1. **Sign Up & Explore Kaggle**: Ensure you have a Kaggle account. If not, sign up at [Kaggle](https://www.kaggle.com).

2. **Locate the Titanic Competition**: Go to the [Titanic Competition](https://www.kaggle.com/c/titanic) page on Kaggle.

3. **Overview of the Competition**: Familiarize yourself with the competition's objectives, rules, and datasets by reading the provided information.

4. **Setup Google Colab**:
   - Open [Google Colab](https://colab.research.google.com/).
   - Start a new notebook.

5. **Install Kaggle Library in Colab**:
   - In the first cell of your Colab notebook, install the Kaggle library using the following command:
     ```python
     !pip install kaggle
     ```

6. **Setup Kaggle API Credentials in Colab**:
   - Go to your Kaggle account, navigate to the 'Account' tab of your user profile, and find the 'API' section.
   - Click 'Create New API Token'. This will download a `kaggle.json` file containing your API credentials.
   - In your Colab notebook, upload this file using the following code:
     ```python
     from google.colab import files
     files.upload()
     ```
   - Then, execute the following commands to set up the Kaggle API environment:
     ```python
     !mkdir -p ~/.kaggle
     !cp kaggle.json ~/.kaggle/
     !chmod 600 ~/.kaggle/kaggle.json
     ```

7. **Download the Dataset**:
   - Now, use the Kaggle API to download the Titanic dataset directly into your Colab environment:
     ```python
     !kaggle competitions download -c titanic
     ```
   - Unzip the downloaded files:
     ```python
     !unzip titanic.zip
     ```

8. **Load and View the Dataset**:
   - Import pandas and load the dataset:
     ```python
     import pandas as pd
     train_data = pd.read_csv('train.csv')
     ```
   - Display the first few rows of the dataset:
     ```python
     print(train_data.head())
     ```

✅ Knowledge Check: What makes Kaggle a unique platform for data scientists?

#### 🚀 Challenge:

Follow the steps outlined above to access and view the Titanic dataset in Google Colab. Explore the dataset by printing out different aspects of the data, such as column names using [dataframe].columns, data types using [dataframe].dtypes, and summary statistics using [dataframe].describe() .


#### Submission:

Submit your Colab notebook showing the executed code and any additional exploration or visualization you performed.


✅ Knowledge Check: What makes Kaggle a unique platform for data scientists?

- [ ] A. Community Collaboration**: Kaggle's vibrant community of data scientists and ML engineers from around the world collaborates, shares insights, and helps each other, making it a great platform for learning and growth.

- [ ] B. Wide Range of Competitions**: The platform hosts a variety of competitions with real-world data, providing opportunities to work on diverse, challenging problems and apply different data science techniques.

- [ ] C. Access to Datasets and Notebooks**: Kaggle provides access to a vast repository of datasets and public notebooks (Kernels), allowing users to experiment with data and learn from others’ code.



### Review & Self Study

- [Jupyter Notebook Advanced Usage](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#advanced-usage)
- [Collaborative Data Science with Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
- [Kaggle Micro-Courses](https://www.kaggle.com/learn/overview)


✅ Knowledge Check Answer Why are Jupyter Notebooks popular in data science? B and C : Jupyter Notebooks are popular in data science primarily because they support the integration of executable code, rich text, and visualizations in a single document (B), and they promote collaboration and reproducibility through easy sharing and remote access (C). While Python is a commonly used language in Jupyter Notebooks, they are not limited to Python and can support other programming languages as well, which makes option A incorrect.
✅ Knowledge Check: What are the benefits of using Google Colab for collaborative projects?  A and B; A: Google Colab provides free access to GPUs (Graphics Processing Units) and TPUs (Tensor Processing Units), which are essential for high-performance computing tasks, particularly in machine learning and data analysis. B: Google Colab allows users to run Python code in a cloud environment without the need for any local setup. This feature is particularly useful for collaborative projects as it ensures that all collaborators are working in the same environment with the same configurations. C: This option is not correct. Google Colab does not provide exclusive access to Google's internal datasets. However, it does facilitate easy access to datasets available on platforms like Google Drive and GitHub, making it easier to work with external data in collaborative projects.
✅ Knowledge Check: What makes Kaggle a unique platform for data scientists? A, B and C. Kaggle is unique for data scientists due to its vibrant community collaboration, wide range of real-world data competitions, and extensive access to datasets and shared notebooks.
