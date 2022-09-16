import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
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
highest_train = 0
highest_v = 0

highest_v_estimator_num = 0
highest_test = 0
x_train = x_train.reshape(-1, 20)
x_test = x_test.reshape(-1, 20)   
x_valid = x_valid.reshape(-1, 20)
i = 800
# for i in range(800, 801, 50):
for j in range(1):
    bdt_real = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=2), n_estimators=i, learning_rate=1.5
    )

    bdt_discrete = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=2),
        n_estimators=i,
        learning_rate=1.5,
        algorithm="SAMME",
    )
    print('start fitting')
    bdt_real.fit(x_train, y_train)
    bdt_discrete.fit(x_train, y_train)
    real_train_predict, discrete_train_predict = bdt_real.predict(x_train), bdt_discrete.predict(x_train)
    real_test_predict, discrete_test_predict = bdt_real.predict(x_test), bdt_discrete.predict(x_test)     #求出預測結果
    real_valid_predict, discrete_valid_predict = bdt_real.predict(x_valid), bdt_discrete.predict(x_valid)
    start = time()
    predict = bdt_real.predict(x_test[0, :].reshape(1, 20))
    end = time()

    sammeR_train_acc = accuracy_score(real_train_predict, y_train)
    sammeR_valid_acc = accuracy_score(real_valid_predict, y_valid)#求出正確率
    sammeR_test_acc = accuracy_score(real_test_predict, y_test)
    samme_train_acc = accuracy_score(discrete_train_predict, y_train)
    samme_valid_acc = accuracy_score(discrete_valid_predict, y_valid)
    samme_test_acc = accuracy_score(discrete_test_predict, y_test)
    print('n_estimators = %d' %i)
    print('SAMME.R training set accuracy:', sammeR_train_acc)
    print('SAMME.R validation set accuracy:', sammeR_valid_acc)
    print('SAMME.R testing set accuracy:', sammeR_test_acc)
    
    print('SAMME training set accuracy:', samme_train_acc)
    print('SAMME validation set accuracy:', samme_valid_acc)
    print('SAMME testing set accuracy:', samme_test_acc)
    
    print('-----------------------------------------------------------------------------------------------')
    comp = [sammeR_valid_acc, samme_valid_acc]
    if np.max(comp) > highest_v:
        highest_v = max(comp)
        highest_v_estimator_num = i
print('highest validation accuracy', highest_v)
print('highest validation acc estimators', highest_v_estimator_num)
# print(len(list(real_test_predict)))
print(end - start)