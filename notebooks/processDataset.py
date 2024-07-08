import pandas as pd # type: ignore

# Define the path for the input CSV file
input_file = '../data/raw/BGG_Data_Set.csv'

# Load the CSV file into a DataFrame
df = df = pd.read_csv(input_file, encoding='ISO-8859-1')

# Check if the 'Year Published' column exists in the DataFrame
if 'Year Published' not in df.columns:
    raise ValueError("Column 'Year Published' was not found in the CSV file.")

# Filter the DataFrame to include only rows where 'Year Published' is between 2001 and 2021
filtered_df = df[(df['Year Published'] >= 2001) & (df['Year Published'] <= 2021)]

# Define the path for the output CSV file
output_file = '../data/processed/dataset.csv'

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

# Print a message indicating where the new CSV file was saved
print(f'Filtered CSV saved at: {output_file}')
