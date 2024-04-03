# -*- coding: utf-8 -*-
"""LVADSUSR_Ananthalakshmi(3).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RMTwc09WSnfdM71SPuan5L44u_NAyFxI
"""

import pandas as pd
data = pd.read_csv('social_network.csv')
data.columns

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Handle missing values
print(data.isnull().sum())

# Outlier Handling
outlier_model = IsolationForest(contamination=0.1, random_state=42)
outliers = outlier_model.fit_predict(data[['login_activity', 'posting_activity', 'social_connections']])
data['is_outlier'] = outliers

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

# Encoding data
label_encoder = LabelEncoder()
data['account_status'] = label_encoder.fit_transform(data['account_status'])

# Extracting significant features
features = ['login_activity', 'posting_activity', 'social_connections']

X = data[features]
y = data['is_outlier']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model development
model = IsolationForest(n_estimators=100, contamination=0.1, max_features=3, max_samples=10000, random_state=42)
model.fit(X_train)

# Predict the anomalies in the data
y_pred = model.predict(X_train)

# Add the predicted anomaly scores to the original dataframe
data["anomaly_score"] = model.decision_function(X)

anomalies = data.loc[data["anomaly_score"] < 0]

# Create a scatter plot of suspicious activity vs social connections
plt.scatter(data["social_connections"], data["anomaly_score"], label="Not Anomaly")
plt.scatter(anomalies["social_connections"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Social Connections")
plt.ylabel("Anomaly Score")
plt.legend()
plt.show()