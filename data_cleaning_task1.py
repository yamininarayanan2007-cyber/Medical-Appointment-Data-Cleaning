import pandas as pd

df = pd.read_csv("KaggleV2-May-2016.csv")

print("Before Cleaning:")
print(df.info())

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.replace("-", "_")

# Convert date columns
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# Convert No-show to binary (Yes=1, No=0)
df['no_show'] = df['no_show'].map({'Yes': 1, 'No': 0})

df.to_csv("cleaned_medical_dataset.csv", index=False)

print("Cleaning completed successfully!")