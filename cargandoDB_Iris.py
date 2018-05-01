# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:23:02 2018

@author: endJG
"""

import seaborn as sns
sns.set(color_codes=True)
import pandas as pd

dataset = pd.read_csv('C:/Users/endJG/Desktop/IA_proyects/iris.csv')
dataset.head()

print(dataset.groupby('species').size())
sns.pairplot(dataset, hue="species")

setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())