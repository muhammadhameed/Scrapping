import os
import pandas as pd
import json

# Define the directory containing the Excel files
directory = os.getcwd()+"/untitled folder"
print(directory)
# Create a new directory to store the edited files
output_directory = os.path.join(directory, "edited_files")
os.makedirs(output_directory, exist_ok=True)

# Define a function to extract label and score from the JSON-like string
def extract_label_score(json_str):
    json_str = json_str.replace("'", '"')

    data = json.loads(json_str)
    print(data)
    try:
        label = data[0]['label']
        score = data[0]['score']
        return label, score
    except:
        return " "," "

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        # Read the Excel file
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path, engine='openpyxl')

        # Apply the function to extract label and score for each row in column S
        df[['label', 'score']] = df['S'].apply(lambda x: pd.Series(extract_label_score(x)))

        # Drop the original 'S' column if you no longer need it
        df.drop(columns=['S'], inplace=True)

        # Save the modified DataFrame to a new Excel file in the output directory
        output_file_path = os.path.join(output_directory, filename)
        df.to_excel(output_file_path, index=False)

print("All files have been processed and saved to the 'edited_files' directory.")
