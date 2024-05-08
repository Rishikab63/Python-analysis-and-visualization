# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:06:40 2024

@author: Rishika
"""
'''
import pandas as pd
# Create data frame from .csv File
df= pd.read_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\Emp_data.csv")  #\\ so that no error in reading
print("Our DataFrame....\n",df)

df.to_excel("C:\\Users\\Rishika\\Desktop\\CSV file\\new_csv_file_from_excel.xlsx")

tt = pd.read_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\new2.csv")
print(tt)
'''
# importing panda library 
import pandas as pd 
  
# readinag given csv file 
# and creating dataframe 
dataframe1 = pd.read_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\New Text Document.txt") 
  
# storing this dataframe in a csv file 
dataframe1.to_csv("C:\\Users\\Rishika\\Desktop\\CSV file\\NewTextDocument.csv",  
                  index = None) 