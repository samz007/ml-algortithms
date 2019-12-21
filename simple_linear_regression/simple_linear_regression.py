import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# creating test set from dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

# fitting part of simple liear regression
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# prediction
y_pred = regressor.predict(X_test)

# comparison for training set

plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, regressor.predict(X_train), color='red')
plt.title("salary vs years of experience")
plt.show()


# comparison for test set

plt.scatter(X_test, y_test , color='blue')
plt.plot(X_train, regressor.predict(X_train), color='red')
plt.title("salary vs years of experience")
plt.show()
