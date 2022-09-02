from __future__ import print_function
from tensorflow import keras
from tensorflow.keras.models import load_model#import 要這樣打才可以跑
import numpy as np
import cv2

def divide(data):  #資料第一行除以250
    vector, remain = np.split(data,[1],axis = 1)
    vector = vector/250
    data = np.concatenate((vector, remain), axis = 1)
    return data

# 定義分類數量
num_classes = 8

# 定義圖像寬、高
img_rows, img_cols = 10, 4

# 載入  訓練資料
x_test = np.loadtxt('x_test.txt')
y_test = np.loadtxt('y_test.txt')
y_test = y_test - 1
# 保留原始資料，供 cross tab function 使用
y_test_org = y_test

# x_test = x_test.astype('float64')
x_test = divide(x_test)

# channels_first: 色彩通道(R/G/B)資料(深度)放在第2維度，第3、4維度放置寬與高  ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

x_test = x_test.reshape(-1, img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)



# y 值轉成 one-hot encoding
# y_train = keras.utils.to_categorical(y_train, num_classes) ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
y_test = keras.utils.to_categorical(y_test, num_classes)
model = load_model('model914.h5')#----------------------------------------------------------------讀取模型
score = model.evaluate(x_test, y_test, verbose=0)
# x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols)
sample, remain = np.split(x_test,[1],axis = 0)    #--------------------------------------------剪出第一張圖片

preds = model.predict_classes(sample)#-----------------------------------判斷圖片
print(sample.shape)
sample = sample.reshape(10, 4 ,1)#改變維度讓cv2可以印出來（cv2吃3維
window_name = 'hello'
cv2.imshow(window_name, sample)


print('Test loss:', score[0])
print('Test accuracy:', score[1])
print ('predicted', preds)
print(sample.shape)

key = cv2.waitKey(0)