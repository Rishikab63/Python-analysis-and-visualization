# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:49:11 2024

@author: SUBRAJEET
"""

import pandas as pd
# Create data frame from .csv File
# Create data frame from .csv File
df= pd.read_csv("C:/Users/Rishika/Downloads/Emp_data_1_NaN.csv", parse_dates=['doj'])  
#\\ so that no error in reading

#df=pd.read_csv("E:\BasicsOfPython/emp_data.csv", parse_dates=['doj'])

print(df)


# Sort the rows on 'doj' column

 ## Sorting in ascending order
df1=df.sort_values('doj')
print(df1)

## Sorting in descending order
 
 df1=df.sort_values('doj',  ascending=False)
 print(df1)
 
 ## Sorting on multiple columns
 
 df1=df.sort_values(by=['doj', 'salary'], ascending=[False, True])
 
 print(df1)