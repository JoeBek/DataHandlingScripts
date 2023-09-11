import pandas as pd
import math
import matplotlib as plot
import openpyxl as xl

# data = {'x': [0,10,21,23,25,34,41,50,55,56,60,65,75], 'y': [10,110,121,123,251,314,141,150,155,516,610,165,715]}

# read 

def round_to_multiple(number, multiple):

    return multiple * round(number/multiple)


def apply_error_correction(value, error_tolerance):
    target_value = round(value)


    if abs(value - target_value) <= error_tolerance:
        return target_value
    else:
        return value

excel_file = 'lab1.12214.xlsx'

# Read the Excel file

data = pd.read_excel(excel_file)

df = pd.DataFrame(data, columns = ['Time','Channel1', 'Channel2','Current'])

print(df.head)

values_to_remove = []

rule = lambda x: round(x * 10, 1) % 2.5 != 0 if isinstance(x, float) else True

df['Channel2'].apply(lambda x: values_to_remove.append(x) if rule(x) else None)





remove_values = lambda y: y if y not in values_to_remove else None

# print(values_to_remove)

df['Channel2'] = df['Channel2'].apply(remove_values)
df = df.dropna(subset=['Channel2'])

df_corrected = df.drop_duplicates(subset=['Channel2']).reset_index()

print(df_corrected.head(20))



'''
plot.scatter(data['x'], data['y'], label='Data Points', color='blue', marker='o')
plot.xlabel('Time')
plot.ylabel('Y-Axis Label')
plot.title('Scatter Plot of Voltage vs. output')
plot.legend()  # Show the legend
plot.grid(True)  # Show gridlines
plot.show()
'''
