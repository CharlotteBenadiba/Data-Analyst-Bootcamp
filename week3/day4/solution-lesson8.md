✅ Knowledge Check: When might it be appropriate to fill missing values with a specific value like 0?
When the missing values are not informative and can be safely replaced.

✅ Knowledge Check: In which situations might removing rows with missing data be a good approach?C. When missing values are concentrated in specific columns.

Please select the correct answers by marking the appropriate option for each question (e.g., "1 - A, 2 - C, 3 - D, 4 - B").

🚀 Challenge : Identify Outliers
1. Calculate Q1 and Q3 for the 'Age' column:
    * Q1 = 20.125
    * Q3 = 38.0
2. Compute the Interquartile Range (IQR):
    * IQR = Q3 - Q1 = 38.0 - 20.125 = 17.875
3. Define the lower bound and upper bound for potential outliers based on the IQR:
    * Lower Bound = Q1 - 1.5 * IQR = 20.125 - 1.5 * 17.875 = -6.25 (Note: Lower bound cannot be negative, so we use 0 as the lower bound)
    * Upper Bound = Q3 + 1.5 * IQR = 38.0 + 1.5 * 17.875 = 64.125
4. Identify and count the number of outliers in the 'Age' column:
    * There are no outliers in the 'Age' column based on the defined bounds. All 'Age' values fall within the range of [0, 64.125].
This means that there are no outliers in the 'Age' column of the Titanic dataset based on the IQR method, as all ages fall within the range of [0, 64.125].
