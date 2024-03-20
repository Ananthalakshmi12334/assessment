# -*- coding: utf-8 -*-
"""LVADSUSR_Ananthalakshmi_FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q_zN4iFkJrJ_AFX1ofAACyK9uekWnWa2

#Q1
"""

import pandas as pd
import numpy as np
df = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
print(df)
print("Number of rows and columns are:",df.shape)
print("The types of data are:",df.dtypes)
print("The numerical categorical data is:",df.describe)
print("The missing values are:",df.isnull().sum())

"""#Q2"""

missing_value=df.isnull().sum()
print("The missing values in the data set are:",missing_value)
filling_values=df.fillna(df.mean(), inplace=True)
print("Fillng the missing value:",filling_values)
Dropping_value = df.dropna()
print("Dropping the values:",Dropping_value)
duplicate = df.duplicated().sum()
print("Number of duplicate entries:", duplicate)
Drop_Duplicate = df.drop_duplicates()
print("Dropped off all the duplicate values",Drop_Duplicate)

"""#Q3"""

import pandas as pd
num_data=['Sales','Quantity','Profit']
mean=df[num_data].mean()
print("The mean is:",mean)
median=df[num_data].median()
print("The median is:",median)
mode=df[num_data].mode().iloc[0]
print("The mode is:",mode)
x=df[num_data].max()
y=df[num_data].min()
range=x-y
print("The range is:",range)
variance=df[num_data].var()
print("The variance is:",variance)
std=df[num_data].std()
print("The standard deviation is:",std)

"""#Q4"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.histplot(df['Category'], bins=20,color='red')#histogram
plt.title('Histogram of category')
plt.xlabel('category')
plt.ylabel('Profit')
plt.show()

plt.figure(figsize=(6, 6))
sns.scatterplot(x='Product Name', y='Sales', data=df, color='green')#scatterplot
plt.title('Scatter Plot of Product name and Sales')
plt.xlabel('Product name')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(6, 6))
sns.boxplot(x='Category', y='Quantity', data=df, palette='pink')#boxplot
plt.title('Box Plot of Sales by Quantity')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df)# barplot
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
plt.title('Pie Chart of category')
plt.axis('equal')
plt.show()

"""#Q5"""

correlations=df.corr()
print("The correlations between different variables are:",correlations)

"""#Q6"""

num_data = ['Sales', 'Quantity', 'Profit']
df_zscores = df[num_data].apply(lambda x: np.abs((x - x.mean()) / x.std()))
outliers = df_zscores > 5
out_data = df[outliers.any(axis=1)]
print("Outliers data are:",out_data)
plt.figure(figsize=(6, 6))
sns.boxplot(data=df[num_data])
plt.title('Boxplot of Sales, Quantity, and Profit')
plt.xlabel('Numerical Quantity')
plt.ylabel('Values')
plt.tight_layout()
plt.xticks(rotation=90)
plt.show()

"""#**Q7**(1)

Yes, there are noticable patten as a linear line. when the sales are increased, profits are also increased.
In the range between 8000 to 10000, the profit growth is more.
"""

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sales', y='Sales', data=df, color='green')#scatterplot
plt.title('Scatter Plot of Sales and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

"""#Q7(2)"""

import pandas as pd
df['Sales'] = pd.to_datetime(df['Sales'])
df.sort_values(by=['Product Name', 'Sales'], inplace=True)
df['TimeBetweenOrders'] = df.groupby('Product Name')['Sales'].diff()
avg_time_between_orders = df.groupby('Product Name')['TimeBetweenOrders'].mean()
print("Avg Time of sales for Each Customer by product name:")
print(avg_time_between_orders)
print("Overall Average Time Between Orders:", avg_time_between_orders.mean())

"""#Q7(3)"""

customer = df.groupby('Order ID').agg({'EmailID': 'nunique', 'Sales': 'sum'}).reset_index()
customer.columns = ['Order ID', 'Quantity', 'TotalSales']
top_customers_by_orders = customer.nlargest(5, 'Quantity')
top_customers_by_sales = customer.nlargest(5, 'TotalSales')
print("Top 5 Customers byOrders :")
print(top_customers_by_orders.set_index('Order ID'))
print("Top 5 Customers by Sales:")
print(top_customers_by_sales.set_index('Order ID'))

"""#Q7(4)"""

df['Time'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('Category')['Time'].mean()
print(average_time_between_order_and_delivery)

df['Time'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('EmailID')['Time'].mean()
print(average_time_between_order_and_delivery.mean())