"""
Задание 3.
Изучите взаимосвязь компаний производителей ноутбуков и компаний производителей процессоров,
используя сложенную или многорядовую столбчатую диаграмму Процессоры от Samsung не изучайте
3.1 Постройте график в абсолютных величинах
3.2 Постройте график в относительных величинах
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptops_10.csv")
print(df.head())

# 3.1 Постройте график в абсолютных величинах
data = pd.crosstab(index=df["Company"], columns=df["Cpu_Company"]).reset_index()
data.drop(columns=["Samsung"], inplace=True)
print(data)

n_ticks = data.index
print(n_ticks)

offset = 0.2
w = 0.4

plt.figure(figsize=(16, 6))

plt.bar(n_ticks - offset, data["Intel"], width=w)
plt.bar(n_ticks + offset, data["AMD"], width=w)
plt.xticks(n_ticks, data["Company"], rotation=45)
plt.title("Ноутбуки")
plt.xlabel("Производитель ноутбуков")
plt.ylabel("Количество")
plt.legend(["Intel", "AMD"])
plt.show()

# 3.2 Постройте график в относительных величинах
data = pd.crosstab(index=df["Company"], columns=df["Cpu_Company"], normalize="index").reset_index().round(2)
data.drop(columns=["Samsung"], inplace=True)
print(data)

plt.figure(figsize=(16, 6))

plt.bar(data["Company"], data["Intel"])
plt.bar(data["Company"], data["AMD"], bottom=data["Intel"])
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 1.01, 0.05), range(0, 101, 5))
plt.title("Ноутбуки")
plt.xlabel("Производитель ноутбуков")
plt.ylabel("Доля")
plt.legend(["Intel", "AMD"])
plt.show()
