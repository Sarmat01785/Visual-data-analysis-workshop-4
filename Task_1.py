"""
Задание 1.
1. Считать данные с помощью pandas
2. Вывести на экран первые 5 строк
- Постройте график
- Назовите график
- Сделайте именование оси x и оси y
- Сделайте выводы
1.1 Изучите распределение количества памяти (Memory_Amount) с помощью matplotlib
1.2 Изучите распределение стоимости ноутбуков (Price_euros) с помощью matplotlib
1.3 Изучите распределение веса ноутбуков (Weight) с помощью matplotlib
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptops_10.csv")
print(df.head())

# 1.1 Изучите распределение количества памяти (Memory_Amount) с помощью matplotlib
plt.figure(figsize=(16, 10))

plt.hist(df["Memory_Amount"], bins=32)

plt.title("Распределение памяти")
plt.xlabel("GB")
plt.ylabel("Количество")
plt.xticks(range(0, 2112, 64), rotation=45)
plt.yticks(range(0, 550, 10))
plt.grid()
plt.show()

# 1.2 Изучите распределение стоимости ноутбуков (Price_euros) с помощью matplotlib
plt.figure(figsize=(16, 6))

plt.hist(df["Price_euros"], bins=61)

plt.title("Распределение стоимости")
plt.xlabel("EURO")
plt.ylabel("Количество")
plt.xticks(range(0, 6200, 100), rotation=45)
plt.yticks(range(0, 110, 5))
plt.grid()
plt.show()

# 1.3 Изучите распределение веса ноутбуков (Weight) с помощью matplotlib
plt.figure(figsize=(16, 6))

plt.hist(df["Weight"],bins = 40)

plt.title("Распределение веса")
plt.xlabel("грамм")
plt.ylabel("Количество")
plt.xticks(np.arange(0.7, 4.8, 0.1), np.arange(700, 4800, 100), rotation = 45)
plt.yticks(range(0, 160, 5) )
plt.grid()
plt.show()
