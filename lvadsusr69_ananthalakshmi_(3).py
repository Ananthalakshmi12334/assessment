# -*- coding: utf-8 -*-
"""LVADSUSR69_ANANTHALAKSHMI (3).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPGbbWI40Q84td9TIlcMlIvqtIABwk5y
"""

import pandas as pd
data = pd.read_csv("seeds.csv")
data.head()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns

#a.Data exploration and pre-processing
# Handle missing values
print(data.isnull().sum())
data.fillna(data.mean(), inplace=True)

# Normalize the numerical columns
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

#EDA
data.describe()
print(data.shape)
print(data.info())
# Summary statistics
print(data.describe())

# Histogram of numerical features
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Pairplot of numerical features
sns.pairplot(data, diag_kind='kde')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


#optimal number of clusters determination
inertia_values = []
silhouette_scores = []
k_values = range(2, 10)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))

plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve for Optimal k')
plt.xticks(k_values)
plt.show()

plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k')
plt.xticks(k_values)
plt.show()

#clustering algorithm application
optimal_k = 7
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_data)

cluster_labels = kmeans.predict(scaled_data)

silhouette_avg = silhouette_score(scaled_data, cluster_labels)
print("Average silhouette score: ",silhouette_avg)

#cluster analysis
data['Cluster'] = kmeans.labels_
cluster_profiles = data.groupby('Cluster').mean()
print(cluster_profiles)