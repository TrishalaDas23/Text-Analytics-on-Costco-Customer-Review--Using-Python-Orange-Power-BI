import pandas as pd
from datetime import datetime
import re


def convert_to_ddmmyyyy(date_string):
    try:
        # Parse the date from the given format and convert to dd/mm/yyyy
        parsed_date = datetime.strptime(date_string.strip(), "%b %d, %Y")
        return parsed_date.strftime("%d/%m/%Y")
    except Exception as e:
        return date_string  # Return original value if parsing fails


def clean_text(text):
    # Remove special characters, punctuation, and emojis using regex
    return re.sub(r'[^\w\s]', '', text)


# Cleaning (phase 1) - Deleting empty rows

# Load the Excel file
input_file = r"C:\Users\Milad\PycharmProjects\firstProject\basicsyntax\Ramzinex_4 (Nobitex)\H2_company_data_Walmart_2.xlsx"
output_file = r"C:\Users\Milad\PycharmProjects\firstProject\basicsyntax\Ramzinex_4 (Nobitex)\H2_company_data_Walmart_2_new.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)

# Drop rows where the first column is empty
# Assuming the first column is the first in the DataFrame (index 0)
df_cleaned = df.dropna(subset=[df.columns[0]])

# Save the cleaned DataFrame to a new Excel file
df_cleaned.to_excel(output_file, index=False)

print(f"Cleaned data saved to {output_file}")

# Cleaning (phase 2) - fixing dates (1/2)

# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)

# Convert the DataFrame to a list of lists for easy row manipulation
rows = df.values.tolist()

# Iterate over each row
for i in range(len(rows)):
    # Example: Access the first column and second column of the current row
    first_column_value = rows[i][0]
    second_column_value = rows[i][1]

    # if pd.isna(first_column_value):  # Check if the first column is empty (NaN)
    #     rows[i][0] = "Default Value"  # Replace it with a default value
    if str(rows[i][1]).lower() == "a day ago":
        rows[i][1] = "Dec 4, 2024"
    elif str(rows[i][1]).lower() == "2 days ago":
        rows[i][1] = "Dec 3, 2024"
    elif str(rows[i][1]).lower() == "3 days ago":
        rows[i][1] = "Dec 2, 2024"
    elif str(rows[i][1]).lower() == "4 days ago":
        rows[i][1] = "Dec 1, 2024"
    elif str(rows[i][1]).lower() == "5 days ago":
        rows[i][1] = "Nov 30, 2024"
    elif str(rows[i][1]).lower() == "6 days ago":
        rows[i][1] = "Nov 29, 2024"
    elif str(rows[i][1]).lower() == "7 days ago":
        rows[i][1] = "Nov 28, 2024"
    elif str(rows[i][1]).lower().find("hours ago") != -1:
        rows[i][1] = "Dec 5, 2024"

# Convert the modified rows back to a DataFrame
df_modified = pd.DataFrame(rows, columns=df.columns)

# Save the modified DataFrame to a new Excel file
df_modified.to_excel(output_file, index=False)

print(f"Modified data saved to {output_file}")

# Cleaning phase 3 (fixing date 2/2)
# Handling "Sept"
# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)

# Convert the DataFrame to a list of lists for easy row manipulation
rows = df.values.tolist()

# Iterate over each row
for i in range(len(rows)):
    # Example: Access the first column and second column of the current row
    first_column_value = rows[i][0]
    second_column_value = rows[i][1]

    # if pd.isna(first_column_value):  # Check if the first column is empty (NaN)
    #     rows[i][0] = "Default Value"  # Replace it with a default value
    if str(rows[i][1]).lower().find("sept") != -1:
        rows[i][1] = str(rows[i][1]).replace("Sept", "Sep").replace("sept", "Sep")

# Convert the modified rows back to a DataFrame
df_modified = pd.DataFrame(rows, columns=df.columns)

# Save the modified DataFrame to a new Excel file
df_modified.to_excel(output_file, index=False)

print(f"Modified data saved to {output_file}")

df = pd.read_excel(input_file)
for i in range(len(df)):
    if isinstance(df.iloc[i, 1], str):  # Ensure the value is a string
        df.iloc[i, 1] = convert_to_ddmmyyyy(df.iloc[i, 1])

# Save the modified DataFrame to a new Excel file
df.to_excel(output_file, index=False)

print(f"Modified data saved to {output_file}")

# cleaning phase 4 (removing duplicate reviews)
df = pd.read_excel(input_file)

# Remove duplicate rows based on the "Review" column (4th column)
df_unique = df.drop_duplicates(subset=df.columns[3], keep='first')  # Keep the first occurrence

# Save the cleaned DataFrame to a new Excel file
df_unique.to_excel(output_file, index=False)

print(f"Cleaned data with unique reviews saved to {output_file}")

# cleaning phase 5 (making strings lower case and removing special charachters)
df = pd.read_excel(input_file)

# Process only the 3rd and 4th columns
columns_to_clean = [df.columns[2], df.columns[3]]  # 3rd and 4th columns

for column in columns_to_clean:
    # Convert to lowercase
    df[column] = df[column].str.lower()

    # Remove special characters and emojis
    df[column] = df[column].apply(clean_text)

# Save the cleaned DataFrame to a new Excel file
df.to_excel(output_file, index=False)

print(f"Cleaned data saved to {output_file}")

# repeating phase 4 (removing duplicate reviews)
df = pd.read_excel(input_file)

# Remove duplicate rows based on the "Review" column (4th column)
df_unique = df.drop_duplicates(subset=df.columns[3], keep='first')  # Keep the first occurrence

# Save the cleaned DataFrame to a new Excel file
df_unique.to_excel(output_file, index=False)

print(f"Cleaned data with unique reviews saved to {output_file}")