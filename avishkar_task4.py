# -*- coding: utf-8 -*-
"""avishkar_task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xH2YfvK0OGHAF9DRF9pzRSt45BPjqe1r

**Sales prediction**

---
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your sales dataset (replace 'your_dataset.csv' with your actual file)
sales_data = pd.read_csv('/content/drive/MyDrive/advertising.csv')

# Display the column names
print(sales_data.columns)

# Separate features and target variable
X_columns = ['advertising_expenditure', 'target_audience_segmentation']
if all(col in sales_data.columns for col in X_columns):
    X = sales_data[X_columns]
    y = sales_data['sales']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Continue with the rest of your code...
    # Create a Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Visualize the predictions vs actual values
    plt.scatter(X_test['advertising_expenditure'], y_test, color='black', label='Actual')
    plt.scatter(X_test['advertising_expenditure'], predictions, color='blue', label='Predicted')
    plt.xlabel('Advertising Expenditure')
    plt.ylabel('Sales')
    plt.legend()
    plt.show()

else:
    print("One or more specified columns not found in the DataFrame.")