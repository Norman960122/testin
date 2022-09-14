import numpy as np
import xgboost as xgb

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder 

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score

x_train = np.loadtxt('x_train_short2.txt')
y_train = np.loadtxt('y_train_short2.txt')
x_test = np.loadtxt('x_test_short3.txt')
y_test = np.loadtxt('y_test_short3.txt')
x_train = x_train.reshape(-1, 20)
x_test = x_test.reshape(-1, 20)
y_test = y_test - 1
y_train = y_train - 1
print(x_train.shape, y_train.shape)
model = XGBClassifier(max_depth = 5) 

model.fit(x_train, y_train)
y_pred_train = model.predict(x_train) 
y_pred_test = model.predict(x_test) 


train_accuracy = accuracy_score(y_train, y_pred_train) 
test_accuracy = accuracy_score(y_test, y_pred_test) 
print("train Accuracy: %f%%" % (train_accuracy * 100.0))
print("test Accuracy: %f%%" % (test_accuracy * 100.0))
# import xgboost as xgb

# from sklearn import datasets

# from sklearn.model_selection import train_test_split

# from sklearn.preprocessing import LabelEncoder 

# from xgboost import XGBClassifier

# from sklearn.metrics import accuracy_score

# iris = datasets.load_iris()

# X = iris.data

# y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# lc = LabelEncoder() 

# lc = lc.fit(y) 

# lc_y = lc.transform(y)

# model = XGBClassifier() 

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test) 

# predictions = [round(value) for value in y_pred]

# accuracy = accuracy_score(y_test, predictions) 

# print("Accuracy: %.2f%%" % (accuracy * 100.0))
# print(X_train.shape, y_train.shape)