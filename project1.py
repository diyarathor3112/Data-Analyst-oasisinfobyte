import numpy as np
import pandas as pd


df=pd.read_csv('retail_sales_dataset.csv')
#data cleaning 
print("Shape : ", df.shape)
print("Datatypes : ", df.dtypes)
print("Missing values : ",df.isnull().sum())
print("Unique Values : ",df.nunique())

#handling missing values
print("Missing values : ",df.isnull().sum())
cols=df.select_dtypes(include=['Int64','float64']).columns
for col in cols:
    df[col]=df[col].fillna(df[col].median)

obj_cols=df.select_dtypes(include=['object']).columns
for col in obj_cols:
    df[col]=df[col].fillna(df[col].mode()[0])

print("handled Missing Value : ")
print(df.isnull().sum())

calc_mean=df.select_dtypes(include=['int64','float64']).coloumns

    