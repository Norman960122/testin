import numpy as np

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score
from time import time

#--------------------------------------------------------
img_rows, img_cols = 5, 4
x = np.loadtxt('x_train_short_all.txt')   #------------------讀取檔案
y = np.loadtxt('y_train_short_all.txt')  
reshaped_x = x.reshape(-1, img_rows, img_cols)
first_dim = np.random.permutation(reshaped_x.shape[0])		#打亂後的行號（將0～1719的數字打亂）
# print(type(reshaped_x.shape[0]*0.9))
train_index, valid_index, test_index = first_dim[ : int((reshaped_x.shape[0]*0.8))],    first_dim[int((reshaped_x.shape[0]*0.8)) : int((reshaped_x.shape[0]*0.9))],    first_dim[int(reshaped_x.shape[0]*0.9) : reshaped_x.shape[0]]
x_train = reshaped_x[train_index, :, :]		#獲取打亂後的訓練資料(照著打亂的array順序創造一個新的檔案)
y_train = y[train_index]

x_test = reshaped_x[test_index, :, :]		#獲取打亂後的測試資料(照著打亂的array順序創造一個新的檔案)
y_test = y[test_index]

x_valid = reshaped_x[valid_index, :, :]		#獲取打亂後的validation資料(照著打亂的array順序創造一個新的檔案)
y_valid = y[valid_index]
#--------------------------------------------
y_test = y_test - 1
y_train = y_train - 1
y_valid = y_valid - 1

x_train = x_train.reshape(-1, 20)
x_test = x_test.reshape(-1, 20)   
x_valid = x_valid.reshape(-1, 20)

model = XGBClassifier(max_depth = 6, n_estimators = 15) 

model.fit(x_train, y_train)
y_pred_train = model.predict(x_train) 
y_pred_valid = model.predict(x_valid)
y_pred_test = model.predict(x_test) 


train_accuracy = accuracy_score(y_train, y_pred_train) 
valid_accuracy = accuracy_score(y_valid, y_pred_valid)
test_accuracy = accuracy_score(y_test, y_pred_test) 
print("train Accuracy: %f%%" % (train_accuracy * 100.0))
print("validation Accuracy: %f%%" % (valid_accuracy * 100.0))
print("test Accuracy: %f%%" % (test_accuracy * 100.0))
start = time()
predict = model.predict(x_test[0, :].reshape(1, 20))
end = time()
print(end - start)
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