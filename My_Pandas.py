# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:49:33 2024

@author: SUBRAJEET
"""


import pandas as pd

# Create data frame from .csv File
df=pd.read_csv("E:\BasicsOfPython/emp_data.csv")

# Create data frame from .xlsx File
WS = pd.read_excel('E:\BasicsOfPython/emp_data.xlsx')


#Creating Data frame from a Python dictionary

Employee_data={"empid":[1001,1002,1003,1004, 1005,1006], "empname":["Radha", "Sneh", "Utsav", "Sundar", "Suman","Sushree"],
               "sal":[10000, 12000.50, 14000.33, 16500.65, 19500.52, 18000.20], "doj":['22-03-2022', '10-02-2020', '29-03-2018',
       print(df)                                                                               '25-07-2022' , '12-08-2019', '10-08-2019']}

df=pd.DataFrame(Employee_data)

print(df)

# Creating Data Frame from Python list of tuples

empdata=[(1001, "Ganesh", 10000,'10-10-2000'), (1002, "Ramesh", 12400,'19-08-2004'), (1003, "Shyamli", 14000, '12-04-2001')]

df=pd.DataFrame(empdata, columns=["eno","ename", "sal", "doj"])

print(df)

# Viewing datframe using loc() and iloc()

df1=df.loc[:,['ename', 'doj']]

print(df1)

df2=df.iloc[:,[1,3]]
print(df2)

## To view only 0 to 3rd rows of 'ename' and 'doj' using loc()

dff2=df.loc[0:3,['ename', 'doj']]
dff2

## To view only 0 to 3rd rows of 'ename' and 'doj' using iloc()
dff1=df.iloc[0:3,[1,3]]

dff1

dff1=df.iloc[0:3,:]

print(dff1)

# #To view 3rd row to 0th row with all columns

dff1=df.loc[3:0:-1,:]

print(dff1)

#Using iloc()

dff1=df.iloc[3:0:-1,:]

print(dff1)

# Retrieve the last row
dff1=df.iloc[-1,:]
print(dff1)

# Retrieve the last column using iloc
dff1=df.iloc[:,-1]
print(dff1)

# Retrieve the last column using loc
dff1=df.loc[:,'doj']
print(dff1)




