from __future__ import print_function
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, LSTM
from tensorflow.keras import backend as K
from time import time
import numpy as np
def divide(data):  #資料第一行除以250
    vector, remain = np.split(data,[1],axis = 1)
    vector = vector/250
    data = np.concatenate((vector, remain), axis = 1)
    return data
s = 0   #用來存取最高正確率
times = 0
# 定義梯度下降批量
batch_size = 64
# 定義分類數量
num_classes = 9
# 定義訓練週期
epochs = 200



# 載入 MNIST 訓練資料
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
y_train = y_train - 1     #on hot encoding 要求 類別要從零開始
y_test = y_test - 1
y_valid = y_valid - 1
# 保留原始資料，供 cross tab function 使用
y_test_org = y_test

# divide first col by 250
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train = divide(x_train)
# x_test = divide(x_test)


# channels_first: 色彩通道(R/G/B)資料(深度)放在第2維度，第3、4維度放置寬與高

input_shape = (img_rows, img_cols)


# y 值轉成 one-hot encoding
y_train = keras.utils.to_categorical(y_train, num_classes)#？////////////////？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
y_test = keras.utils.to_categorical(y_test, num_classes)
y_valid = keras.utils.to_categorical(y_valid, num_classes)

i = 64
# j = 64
# for j in range(32, 129, 32):
# for i in range(16, 129, 16):
for k in range(1):
   
    model = Sequential()
   
    model.add(LSTM(i, input_shape = input_shape))

    model.add(Dropout(0.25))
  
    model.add(Dense(32, activation='relu'))
  
    model.add(Dropout(0.5))

    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adam(),
                metrics=['accuracy'])

    train_history = model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1,                
            validation_data=(x_valid, y_valid))

    # 顯示損失函數、訓練成果(分數)
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    start = time()
    aaa = model.predict_classes(x_train[1, :, :].reshape(1, 5, 4))
    end = time()
    print(end - start)

    if s < score[1]:#儲存正確率最高的模型
        save_i = i
        # save_j = j
        model = model.save('model_short.h5')#儲存模型py
        s = score[1]
    # if 0.8 < score[1]:#把測試資料正確率大於0.8的存起來
    with open('result_short.txt' , 'a') as outfile:
        outfile.write('layer 1:')
        outfile.write(str(i))
        outfile.write(' layer 2:')
        # outfile.write(str(j))
        outfile.write(' score:')
        outfile.write(str(score[1]))
        outfile.write('\n')
    times = times + 1
        
                
            
print('best score : ', s)
print('number of first layer', save_i)
# print('num of second kernel', save_j)
print(times)
