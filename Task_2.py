"""
Задание 2.
Постройте график. Сделайте выводы
2.1 Изучите распределение типов носителя (Memory_Type)
2.2 Изучите распределение компаний производителей (Company)
2.3 Изучите распределение операционной системы (OpSys)
2.4 Изучите распределение компаний производителей CPU (Cpu_Company)
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptops_10.csv")
print(df.head())

# 2.1 Изучите распределение типов носителя (Memory_Type)
data = df["Memory_Type"].value_counts()
print('Распределение типов носителя Memory_Type:')
print(data)

plt.pie(data, labels=data.index, autopct="%.2f%%")
plt.show()

# 2.2 Изучите распределение компаний производителей (Company)
data = df["Company"].value_counts()
print('Распределение компаний производителей Company:')
print(data)

plt.figure(figsize=(16, 5))
plt.bar(data.index, data)

plt.title("Распределение компаний")
plt.xlabel("Компании")
plt.ylabel("Количество")
plt.xticks(rotation=45)
plt.yticks(range(0, 320, 10))
plt.grid()
plt.show()

# 2.3 Изучите распределение операционной системы (OpSys)
data = df["OpSys"].value_counts()
print('Распределение операционной системы OpSys:')
print(data)

plt.figure(figsize=(16, 5))
plt.bar(data.index, data)

plt.title("Распределение операционной системы")
plt.xlabel("ОС")
plt.ylabel("Количество")
plt.xticks(rotation=45)
plt.yticks(range(0, 1200, 50))
plt.grid()
plt.show()

# 2.4 Изучите распределение компаний производителей CPU (Cpu_Company)
data = df["Cpu_Company"].value_counts()
print('Распределение компаний производителей CPU Cpu_Company:')
print(data)

plt.figure(figsize=(10, 5))
plt.pie(data, labels=data.index, autopct="%.2f%%")
plt.show()

