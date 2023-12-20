"""
Задание 5
Постройте матрицу корреляций для таблицы.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptops_10.csv")
print(df.head())

# Постройте матрицу корреляций для таблицы.
corr_matrix = df[["Inches", "Weight", "Price_euros", "Memory_Amount"]].corr().round(2)
print(corr_matrix)

plt.figure(figsize=(5, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=1)
plt.show()
