# -*- coding: utf-8 -*-
"""hw10_cleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1umYJUSUuc91tZN_XLo8vWSthOhTJjIoY
"""

import requests, pandas as pd

df=pd.read_csv("/content/Forest area (% of total land area).csv", skiprows=6, encoding='latin-1')

df
# We see that there are rows we don't want at the bottom, so drop all data after Zimbabwe

df = df.iloc[:191]

df

df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df

df.columns

countries = [' Brazil', ' China', ' Indonesia', ' Togo', ' Dominican Republic', ' United Kingdom', ' United States', ' China', 'Australia', ' Viet Nam', ' Uruguay', ' Germany']
df2 = df.loc[df['Country'].isin(countries)]

df2

df3 = df2.melt(id_vars=['Country'], 
value_vars=['1990','1995','2000','2005','2010','2011','2012','2013','2014','2015','2016'], var_name='Year', 
value_name='Forest Coverage')

df3

df.columns[0]

#Export to plot
df3.to_csv("hw10_forest_cover_ten.csv",encoding = 'utf-8', index=False)