"""
Задача 1
Постройте график.
Назовите график.
Сделайте именование оси x и оси y.
Сделайте выводы.

1.1. Скачать следующие данные: kc-house-data и laptop_price
1.2. Изучите стоимость недвижимости
1.3. Изучите распределение квадратуры жилой площади
1.4. Изучите распределение года постройки
"""

"""
Шпаргалка
id - Уникальный ID для каждого дома.
date - Дата продажи дома.
price - Стоимость продажи дома.
bedrooms - Кол-во спален.
bathrooms - Кол-во ванных комнат (0.5 - туалет без душа).
sqft_living - Кв. метры жилые.
sqft_lot - Кв. метры общие.
floors - Кол-во этажей.
waterfront - Есть набержная или нет.
view - Значение от 0 до 4 насколько хороший вид.
condition - Значение от 1 до 5 насколько хорошее состояние.
grade - Значение от 1 до 13, где 1-3 плохая  конструкция здания и дизайн, 7 - средний уровень конструкции и дизайна,  
11-13 - высокое качество конструкции и дизайна.
sqft_above - Кв. метры дома, которые находятся выше земли.
sqft_basement - Кв. метры дома, которые находятся ниже земли.
yr_built - Год постройки дома.
yr_renovated - Год ремонта дома.
zipcode - Индекс.
lat - Широта.
long - Долгота.
sqft_living15 - Кв. метры жилой площади у 15 соседей.
sqft_lot15 - Кв. метры общей площади у 15 соседей.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('kc-house-data.csv', encoding='1251')
print(df.head())

# 1.2. Изучите стоимость недвижимости

# Распределение стоимости недвижимости
sns.histplot(data=df, x='price', kde=True)
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость')
plt.ylabel('Количество')

plt.figure(figsize=(9, 4))
plt.hist(df['price'], bins=32)
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость')
plt.ylabel('Количество')
plt.grid()
plt.show()

# Распределения цен на дома в зависимости от состояния
g = sns.FacetGrid(df, col='condition')
g.map(plt.hist, 'price')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.suptitle('Распределение цены на жилье по условиям')
plt.show()

# 1.3. Изучите распределение квадратуры жилой площади

# Распределение квадратуры жилой площади
sns.histplot(data=df, x='sqft_living', kde=True)
plt.title('Распределение квадратуры жилой площади')
plt.xlabel('Квадратура жилой площади')
plt.ylabel('Частота')
plt.show()

# 1.4. Изучите распределение года постройки

# Распределение года постройки
sns.histplot(data=df, x='yr_built', kde=True)
plt.title('Распределение года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Частота')
plt.show()
