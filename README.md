# Medical-Appointment-Data-Cleaning

Data Cleaning and Preprocessing – Task 1
📊 Dataset Used:

Medical Appointment No Shows Dataset
File: KaggleV2-May-2016.csv

🎯 Objective:
To clean and preprocess a raw dataset by handling duplicates, standardizing formats, and ensuring proper data types.

🔍 Steps Performed:
Loaded dataset using Pandas.
Checked dataset structure using .info() and .describe().
Verified missing values using .isnull().sum().
Removed duplicate records using drop_duplicates().
Standardized column names (lowercase, replaced special characters).
Converted date columns to datetime format.
Transformed the "No-show" column into binary format (Yes = 1, No = 0).
Saved cleaned dataset as:
cleaned_medical_dataset.csv

🛠 Tools Used:
Python
Pandas
Command Prompt

📁 Files in Repository
- KaggleV2-May-2016.csv
- cleaned_medical_dataset.csv
- data_cleaning.ipynb
- README.md

✅ Outcome:

The dataset is cleaned, structured, and ready for analysis or modeling.
