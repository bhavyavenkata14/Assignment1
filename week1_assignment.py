# -*- coding: utf-8 -*-
"""Week1 Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OgpwgcG_a_KTyf3k11SvgBZ82Z71hx-b
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# creating a data frame
df = pd.read_csv("Children.csv")

print(df.head())
print(df.tail())

df.dropna()
df

sns.lineplot(x="Month",y="Attendance", data=df)

sns.histplot(data=df,x="Event Type Option 1")

sns.scatterplot(x="Event Type Option 1",y="Primary Event Type",data=df)