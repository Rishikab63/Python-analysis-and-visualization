# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:14:34 2024

@author: SUBRAJEET
"""
import pandas as pd
# Create data frame from .csv File
df=pd.read_csv("E:\BasicsOfPython/emp_data.csv")

print(df)

#Operations on dataframes

#1. Knowing number of rows and coluns

df.shape

#2. Retrieve the dimension of the data frame in rows and columns

r, c=df.shape

print(r)
print(c)

#3.Retrieving rows from data frame using head(), it gives the first five rows

df.head()

#4.Retrieving rows from data frame using tail(), it gives the last five rows

df.tail()

#5. Display only the first two rows

df.head(2)

#6. Display only the last two rows
df.tail(2)

# 7. Retrieving a range of rows
df[2:5]

#8. Retrieving alternate rows

df[0::2]


#9. Display the rows in reverse order


df[5:0:-1]


# 11.  To retrieve column names

df.columns

# 12.  To retrieve column data

df.empid

  # Another approach
  
  df['empid']
  
# 13. Retrieving data from multiple columns

  df[['empid' , 'ename']]
  
# 14. Finding Maximum and Minimum

df['salary'].max()

# 15. Display statistical information


df.describe()


# Performing Queries on Data

df[df.salary>10000]

# Retrieve the row where salary is maximum 

df[df.salary==df.salary.max()]


# Display data for some specified columns


df[['empid', 'ename']][df.salary>10000]
  

#Knowing the index range

df.index


# Setting a column as a Index

df1=df.set_index('empid')

print(df1)


# Modify original data frame

df.set_index('empid', inplace=True)
print(df)

# Locate the data of an individual employee in the given datframe


df.loc[104]

# Resetting the index

df.reset_index(inplace=True)
print(df)





