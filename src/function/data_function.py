import pandas as pd
def read_temp_change():
    temp_change = pd.read_csv("./src/data/environement_temperature_clean.csv", sep = ';')
    return temp_change