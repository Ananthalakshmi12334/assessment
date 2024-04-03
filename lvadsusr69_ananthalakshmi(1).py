# -*- coding: utf-8 -*-
"""LVADSUSR69_ANANTHALAKSHMI(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oOm0luQUmHjEUbZ8KBPGvVqe8C7zPZ_W
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, classification_report

# Load data
data = pd.read_csv("loan_approval.csv")

# Handle missing values
data.dropna(inplace=True)

# Outlier Handling
Q1 = data[' income_annum'].quantile(0.25)
Q3 = data[' income_annum'].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data[' income_annum'] < (Q1 - 1.5 * IQR)) | (data[' income_annum'] > (Q3 + 1.5 * IQR)))]

# Convert categorical variables to numerical using LabelEncoder
label_encoder = LabelEncoder()
data[' education'] = label_encoder.fit_transform(data[[' education']])
data[' loan_status'] = label_encoder.fit_transform(data[[' loan_status']])
data[' self_employed'] = label_encoder.fit_transform(data[[' self_employed']])

# Splitting data into features and target variable
X = data.drop(['loan_id', ' loan_status'], axis=1)
y = data[' loan_status']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Classifier model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Make predictions
dt_y_pred = dt_model.predict(X_test)

# Evaluate
dt_accuracy = accuracy_score(y_test, dt_y_pred)
dt_precision = precision_score(y_test, dt_y_pred)
dt_recall = recall_score(y_test, dt_y_pred)
dt_f1 = f1_score(y_test, dt_y_pred)
dt_conf_matrix = confusion_matrix(y_test, dt_y_pred)

print("Decision Tree Classifier Metrics:")
print(f'Accuracy: {dt_accuracy}')
print(f'Precision: {dt_precision}')
print(f'Recall: {dt_recall}')
print(f'F1 Score: {dt_f1}')
print('Confusion Matrix:')
print(dt_conf_matrix)
print(classification_report(y_test, dt_y_pred))

# Visualize the Confusion Matrix for Decision Tree Classifier
sns.heatmap(dt_conf_matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Decision Tree Classifier Confusion Matrix')
plt.show()

# K-Nearest Neighbors (KNN) Classifier model
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
# Logistic Regression model
model = dcl()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Make predictions using KNN Classifier
knn_y_pred = knn_model.predict(X_test)

# Evaluate KNN Classifier
knn_accuracy = accuracy_score(y_test, knn_y_pred)
knn_precision = precision_score(y_test, knn_y_pred)
knn_recall = recall_score(y_test, knn_y_pred)
knn_f1 = f1_score(y_test, knn_y_pred)
knn_conf_matrix = confusion_matrix(y_test, knn_y_pred)

# Evaluate Logistics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
conf_matrix = confusion_matrix(y_test, y_pred)

print("K-Nearest Neighbors (KNN) Classifier Metrics:")
print(f'Accuracy: {knn_accuracy}')
print(f'Precision: {knn_precision}')
print(f'Recall: {knn_recall}')
print(f'F1 Score: {knn_f1}')
print('Confusion Matrix:')
print(knn_conf_matrix)
print(classification_report(y_test, knn_y_pred))

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print('Confusion Matrix:')
print(conf_matrix)

# Visualize
sns.heatmap(knn_conf_matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('K-Nearest Neighbors (KNN) Classifier Confusion Matrix')
plt.show()
# Visualize
sns.heatmap(conf_matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()