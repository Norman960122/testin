import numpy as np
sum = 0
x_train = np.loadtxt('x_train_short2.txt')


x_train[:, 1] = 0 ##################################將喇叭改成0（先印出再改，之後再自己寫判斷式）

len, _ = np.shape(x_train)
for i in range(len):###################計算一列有多少喇叭
    sum = sum + int(x_train[i, 2])

print(x_train)
print(sum)