import pandas as pd
import math
import matplotlib as plot
import openpyxl as xl

file = 'lab2_physical.csv'


# Read the Excel file

data = pd.read_csv(file)

df = pd.DataFrame(data, columns = ['time','Vin', 'Vout'])

print(df.head())