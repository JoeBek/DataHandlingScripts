import pandas as pd
import math
import matplotlib as plot
import openpyxl as xl

file = 'lab2_physical.csv'


# Read the Excel file

data = pd.read_csv(file)

df = pd.DataFrame(data, columns = ['time','Vin', 'Vout'])



Vdsq = 2.557


# setting up to change the column
def Change_Vout(Vout, Vdsq):
    return Vout - Vdsq

df['Vout'] = df['Vout'].apply(Change_Vout, args=(Vdsq))



print(df.head())
