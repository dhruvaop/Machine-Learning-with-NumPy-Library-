# python
"""
multi-line commnts
python basics ML training  

"""
# PANDAS
import pandas as pd

# Numpy = ARRAYS
# PANDAS = DATAFRAMES is a table with rows and columns
# One single column is called as Series.
# .csv - Comma Seperated Values

import math
import numpy as np
arr = np.array([12, 45, 2, 4, 255, 5, 6])
arr1 = np.array([13, 88, 54, 23])
print(arr1)
print(arr)
print(type(arr1))
# print(arr1.dtype())
arr2 = np.array([56, 8, 3, 222, 12, 1])
print(arr2)
# print(type(arr2))
# print(arr2.dtype())


np.ones(10)
np.zeros(10)

arr2 = np.array([1, 12, 7, 81, 75, 42, 11])
x = np.where(arr2 == 12)
print(x)

arr3 = arr.copy()
arr3[0] = 54
print(arr3)
print(arr)

arr4 = arr.view()
arr4[0] = 67
print(arr4)
print(arr)

arr5 = arr2.copy()
print(arr5)

a = input("Enter the number of elements: ")
y = []  # y
b = int(a)

for i in range(0, b):
    z = int(input())  # z
    y.append(z)

print(y)


print(type(arr))
print(arr)

i = 1
while i < 6:
    print(i)
    i += 1

tuple1 = ("ram", "shyam")

for i in tuple1:
    print(i)

x = math.sqrt(16)
print(x)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr4)

print(arr1.shape)
print(arr1.ndim)

arr2 = np.array([])

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr5)

print(arr1.shape)
print(arr1.ndim)

arr6 = np.array([[1, 5, 7], [9, 4, 2]])
print(arr6)

print(arr2.shape)
print(arr2.ndim)

arr9 = np.array([[[1, 5, 43, 55], [3, 4, 8, 76], [23, 51, 56, 41]]])
print(arr9)

arr0 = np.array([4, 15, 87, 75, 2, 7, 1])
print(arr0[0])

arr21 = np.array([[1, 5, 7], [9, 4, 2], [56, 54, 41]])
print(arr21)

print(arr21[0][0])
print(arr21[1][0])

arr23 = np.array([[1, 5, 7], [9, 4, 2], [56, 54, 41]])
print(arr23)

print(arr23[1][1])
print(arr23[2][1])

np.zeros(10, int)

# NUMPY ARRAY SLICIiNG

arr44 = np.array([16, 6, 32, 56, 41, 78, 12, 24])

print(arr44[1:5])

print(arr44[0:4])

arr09 = np.array([16, 6, 32, 56, 41, 78, 12, 24])
print(arr09[2:7])
print(arr09[0:7:3])

print(arr09[-1])  # Negative indexing


arr100 = np.array([1, 2, 3, 4, 5])
np.count_nonzero(arr100)  # to count number of elements in Numpy Array.


df = pd.read_csv("C:/Users/DELL/Downloads/data.csv")
# Reading CSV files

print(df)

print(df.to_string())

print(df.head())  # Displays top 5 rows

print(df.head(10))

print(df.tail())  # Displays bottom 5 rows

print(df.info())  # displays information about file

print(df.tail(10))

print(df.describe())  # here std stands for standard deviation

aiml = pd.Series([10, 90, 95, 83, 82, 80, 18, 19])
print(aiml)

aiml.describe()

print(df.isnull().sum())

df.dropna(inplace=True)  # DROP NULL VALUES.

df.isnull().sum()
