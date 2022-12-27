# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:19:37 2022

@author: Yusra Shahid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("India_FB_2021.csv")
data.head()

## departments covered
print(data)


## removing nans
data.dropna(inplace=True)

## summarizing categories as main categories and others category
data = data.iloc[[0,8,11,14,18,23,41,42,43],:]
row = {'Department /Ministry': 'OTHERS', 'Fund allotted(in crores)': 592971.0800000001}
data = data.append(row, ignore_index = True)
print(data)

## plot data to understand govt priorities
data.plot.bar(x='Department /Ministry', y='Fund allotted(in crores)')

## plotting data in a donut chart to understand % distribution of budget
df = data["Fund allotted(in crores)"]
labels = data["Department /Ministry"]
plt.figure(figsize=(7,7))
plt.pie(df, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow =True)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Distribution of The Budget", fontsize=20)
plt.show()