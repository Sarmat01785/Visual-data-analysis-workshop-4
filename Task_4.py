"""
Задание 4.
Постройте график.
Назовите график.
Сделайте именование оси x и оси y
Сделайте выводы.
4.1 Изучите взаимосвязь стоимости ноутбука и компании производителя процессора
4.2 Изучите взаимосвязь стоимости ноутбука и типа носителя памяти
4.3 Изучите взаимосвязь стоимости ноутбука и кол-ва оперативной памяти
4.4 Изучите взаимосвязь стоимости ноутбука и компании производителя
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptops_10.csv")
print(df.head())

# 4.1 Изучите взаимосвязь стоимости ноутбука и компании производителя процессора
plt.figure(figsize=(16, 6))
sns.boxplot(data=df, x="Price_euros", y="Cpu_Company")
plt.title("Взаимосвязь цены и компании-производителя процессора")
plt.xlabel("Цена")
plt.ylabel("Производитель процессоров")
plt.show()

# 4.2 Изучите взаимосвязь стоимости ноутбука и типа носителя памяти
plt.figure(figsize=(16, 6))
sns.boxplot(data=df, x="Price_euros", y="Memory_Type")
plt.title("Взаимосвязь стоимости ноутбука и типа носителя памяти")
plt.xlabel("Цена")
plt.ylabel("Тип памяти")
plt.show()

# 4.3 Изучите взаимосвязь стоимости ноутбука и кол-ва оперативной памяти
plt.figure(figsize=(16, 6))
sns.boxplot(data=df, x="Price_euros", y="Ram");
plt.title("Взаимосвязь стоимости ноутбука и кол-ва оперативной памяти")
plt.xlabel("Цена")
plt.ylabel("Ram")
plt.show()

# 4.4 Изучите взаимосвязь стоимости ноутбука и компании производителя
plt.figure(figsize=(16, 6))
sns.boxplot(data=df, x="Price_euros", y="Company");
plt.title("Взаимосвязь цены и компании-производителя")
plt.xlabel("Цена")
plt.ylabel("Производитель")
plt.show()
