from __future__ import print_function
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import backend as K
import numpy as np
def divide(data):  #資料第一行除以250
    vector, remain = np.split(data,[1],axis = 1)
    vector = vector/250
    data = np.concatenate((vector, remain), axis = 1)
    return data
s = 0   #用來存取最高正確率
times = 0
# 定義梯度下降批量
batch_size = 1300
# 定義分類數量
num_classes = 12
# 定義訓練週期
epochs = 1500

# 定義圖像寬、高
img_rows, img_cols = 5, 4

# 載入 MNIST 訓練資料
x_train = np.loadtxt('x_train_short2.txt')
y_train = np.loadtxt('y_train_short2.txt')
x_test = np.loadtxt('x_test_short3.txt')
y_test = np.loadtxt('y_test_short3.txt')

y_train = y_train - 1     #on hot encoding 要求 類別要從零開始
y_test = y_test - 1
# 保留原始資料，供 cross tab function 使用
y_test_org = y_test

# divide first col by 250
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
x_train = divide(x_train)
x_test = divide(x_test)


# channels_first: 色彩通道(R/G/B)資料(深度)放在第2維度，第3、4維度放置寬與高

x_train = x_train.reshape(-1, img_rows, img_cols, 1)
x_test = x_test.reshape(-1, img_rows, img_cols, 1)
input_shape = (img_rows, img_cols,1)


# y 值轉成 one-hot encoding
y_train = keras.utils.to_categorical(y_train, num_classes)#？////////////////？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
y_test = keras.utils.to_categorical(y_test, num_classes)



# print(x_train.shape, x_train[0])
# print(x_test.shape)
# print(y_train.shape, y_train[0])
# print(y_test.shape)

i = 128
j = 64
# for j in range(32, 129, 32):
# for i in range(16, 129, 16):
for k in range(1):
    # 建立簡單的線性執行的模型
    model = Sequential()
    # 建立卷積層, Kernal Size: 3x3, activation function 採用 relu
    model.add(Conv2D(i, kernel_size=(3, 3),
                    activation='relu',
                    padding= 'same', 
                    input_shape=input_shape))
    # 建立卷積層  Kernal Size: 3x3, activation function 採用 relu
    model.add(Conv2D(j, (3, 3), activation='relu'))
    # Dropout層隨機斷開輸入神經元，用於防止過度擬合，斷開比例:0.25
    model.add(Dropout(0.25))
    # Flatten層把多維的輸入一維化，常用在從卷積層到全連接層的過渡。
    model.add(Flatten())
    # 全連接層: 128個output
    model.add(Dense(128, activation='relu'))
    # 使用 softmax activation function，將結果分類
    model.add(Dense(num_classes, activation='softmax'))

    # 編譯: 選擇損失函數、優化方法及成效衡量方式
    model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adam(),
                metrics=['accuracy'])

    # 進行訓練, 訓練過程會存在 train_history 變數中
    train_history = model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1,
            validation_data=(x_test, y_test))

    # 顯示損失函數、訓練成果(分數)
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    if s < score[1]:#儲存正確率最高的模型
        save_i = i
        save_j = j
        model = model.save('model2.h5')#儲存模型py
        s = score[1]
    # if 0.8 < score[1]:#把測試資料正確率大於0.8的存起來
    with open('result.txt' , 'a') as outfile:
        outfile.write('kernel 1:')
        outfile.write(str(i))
        outfile.write(' kernel 2:')
        outfile.write(str(j))
        outfile.write(' score:')
        outfile.write(str(score[1]))
        outfile.write('\n')
    times = times + 1
        
                
            
print('best score : ', s)
print('number of first kernel', save_i)
print('num of second kernel', save_j)
print(times)