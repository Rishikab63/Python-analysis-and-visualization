# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:18:29 2024

@author: SUBRAJEET
"""

import pandas as pd
# Create data frame from .csv File
df=pd.read_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\Emp_data_1_NaN.csv", parse_dates=['doj'])
print(df)


# Replace Na or NaN by a specified value here->0

df1=df.fillna(0)

print(df1)

# Replace Na or NaN in each column with a different value
#null jha jha h wha ye sb sai replace ho jaiga
df2=df.fillna({'ename':'Name Missing', 'sal': 0.0, 'doj':'00-00-00'})

print(df2)

# Removing rows with missing data

df3=df.dropna()
print(df3)

### Creating series from a DataFrame

import pandas as pd
df=pd.read_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\Emp_data_1_NaN.csv")

# Create a series object
#col wise de dega wo value ko
ser=pd.Series(df['ename'])
ser

# Create another series object

ser1=pd.Series(df['sal'])
ser1

# Creating DataFrame from Series

dff1=pd.concat([ser, ser1], axis=1)
dff1