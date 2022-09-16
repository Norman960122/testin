from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from time import time
import numpy as np
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
highest_train = 0
highest_v = 0
x_train = x_train.reshape(-1, 20)
x_test = x_test.reshape(-1, 20)   
x_valid = x_valid.reshape(-1, 20)


clf = RandomForestClassifier(n_estimators=15, max_depth=6)
clf.fit(x_train, y_train)
train_pred = clf.predict(x_train)
valid_pred = clf.predict(x_valid)
test_pred = clf.predict(x_test)

train_acc = accuracy_score(train_pred, y_train)
valid_acc = accuracy_score(valid_pred, y_valid)
test_acc = accuracy_score(test_pred, y_test)

print('random forest traing set accuracy', train_acc)
print('random forest validation set accuracy', valid_acc)
print('random forest testing set accuracy', test_acc)

start = time()
predict = clf.predict(x_test[0, :].reshape(1, 20))
end = time()
print(end - start)