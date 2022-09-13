import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

x_train = np.loadtxt('x_train_short2.txt')
y_train = np.loadtxt('y_train_short2.txt')
x_test = np.loadtxt('x_test_short3.txt')
y_test = np.loadtxt('y_test_short3.txt')
x_train = x_train.reshape(-1, 20)
x_test = x_test.reshape(-1, 20)
# x_train = np.asmatrix(x_train)
# x_test = np.asmatrix(x_test)
# y_train = list(y_train)
# y_test = list(y_test)
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=400, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=400,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(x_train, y_train)
bdt_discrete.fit(x_train, y_train)
print('aaaaaaaaaaaaaaaaaaaaaaa')
real_test_predict, discrete_test_predict = bdt_real.predict(x_test), bdt_discrete.predict(x_test)
print('bbbbbbbbbbbbbbbbbbbbb')
print( accuracy_score(real_test_predict, y_test))
print(accuracy_score(discrete_test_predict, y_test))
# print(len(list(real_test_predict)))
