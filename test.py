# print("hello world")

# myList = ['banana', 'apple', 'pear']
# myList.append('blueberry')

# print(myList[3])


import pandas as pd
df = pd.read_csv("Workers.txt", sep="\s+", skiprows=2)
print(df.describe())
df['Gary Sunchem Ratio'] = df['Gary'] / df['Sunchem']
print(df['Gary Sunchem Ratio'])