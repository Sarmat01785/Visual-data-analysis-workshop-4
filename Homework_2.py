"""
Задача 2
2.1. Изучите распределение домов от наличия вида на набережную.
Постройте график. Сделайте выводы.
2.2. Изучите распределение этажей домов.
2.3. Изучите распределение состояния домов.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium

df = pd.read_csv('kc-house-data.csv', encoding='1251')
print(df.head())

# 2.1. Изучите распределение домов от наличия вида на набережную.
df['waterfront'].value_counts().plot.pie(autopct='%1.1f%%')
plt.axis('equal')
plt.title('Распределение домов по береговой линии')
plt.show()

# Создание карты
map = folium.Map(location=[df['lat'].mean(), df['long'].mean()], zoom_start=10)

# Добавление точек на карту
for index, row in df.iterrows():
    folium.Marker([row['lat'], row['long']]).add_to(map)

# Отображение карты
map


# распределения цен на дома в зависимости от наличия вида на набережную.
g = sns.FacetGrid(df, col='waterfront')
g.map(plt.hist, 'price')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.suptitle('Распределение цены на жилье по береговой линии')
plt.show()

# 2.2. Изучите распределение этажей домов.
df['floors'].value_counts().plot.pie(autopct='%1.1f%%')
plt.axis('equal')
plt.title('Распределение домов по этажам')

# Ящик с усами
sns.boxplot(x='floors', y='price', data=df)
plt.xlabel('Этажи')
plt.ylabel('Цена')
plt.title('Распределение цены на жилье по этажам')
plt.show()

# 2.3. Изучите распределение состояния домов.
df['condition'].value_counts().plot.pie(autopct='%1.1f%%')
plt.axis('equal')
plt.title('Распределение домов по состоянию')
plt.show()

# Ящик с усами
sns.boxplot(x='condition', y='price', data=df)
plt.xlabel('Состояние')
plt.ylabel('Цена')
plt.title('Распределение цены на жилье по условиям')
plt.show()

# Распределения цен на дома в зависимости от количества этажей.
g = sns.FacetGrid(df, col='floors')
g.map(plt.hist, 'price')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.suptitle('Распределение цены на жилье по этажам')
plt.show()
