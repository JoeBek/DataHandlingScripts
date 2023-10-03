import pandas as pd
import math
import matplotlib.pyplot as plot
import openpyxl as xl

file = 'lab2_physical.csv'


# Read the Excel file

data = pd.read_csv(file)

df = pd.DataFrame(data, columns = ['time','Vin', 'Vout'])



Vdsq = 2.557


# setting up to change the column
def Change_Vout(Vout, Vdsq):
    return float(Vout) - Vdsq

df['Vout'] = df['Vout'].apply(Change_Vout, args=(Vdsq,))

new_csv = 'physical_lab2_adjusted.csv'

df.to_csv(new_csv, index=False)


# create independent columns to graph

time = df['time']

vin = df['Vin']

vout = df['Vout']

fig, ax = plot.subplots()

print(df.head())

ax.plot(time, vin, label='Vin', color='blue')
ax.plot(time, vout, label='Vout', color='red')


ax.set_xlabel('Time')
ax.set_ylabel('Voltage (V)')
ax.set_title('Vin and Vout vs Time')
ax.legend()  # Show the legend with labels

plot.show()



