import pandas as pd
import os
def read_temp_change():
    # Get the directory of the current Python script
    current_directory = os.path.dirname(__file__)

    # Define the relative path to the CSV file
    file_path = os.path.join(current_directory, "../data/environement_temperature_clean.csv")

    # Check if the file exists
    if os.path.exists(file_path):
        # File exists, proceed with reading
        temp_change = pd.read_csv(file_path, sep=',')
        temp_change = temp_change.loc[(temp_change['Months Code'] == 7020) & (temp_change['Element Code'] == 7271)]
    else:
        # File doesn't exist, handle the error accordingly
        print(f"The file {file_path} does not exist.")
    return temp_change