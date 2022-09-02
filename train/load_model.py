from __future__ import print_function
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import backend as K
# from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model#import 要這樣打才可以跑
import numpy as np
import cv2


# 定義分類數量
num_classes = 10
# 定義訓練週期
epochs = 5

# 定義圖像寬、高
img_rows, img_cols = 28, 28

# 載入 MNIST 訓練資料
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 保留原始資料，供 cross tab function 使用
y_test_org = y_test

# channels_first: 色彩通道(R/G/B)資料(深度)放在第2維度，第3、4維度放置寬與高  ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
if K.image_data_format() == 'channels_first':
    # x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else: # channels_last: 色彩通道(R/G/B)資料(深度)放在第4維度，第2、3維度放置寬與高
    # x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# 轉換色彩 0~255 資料為 0~1
# x_train = x_train.astype('float32') ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
x_test = x_test.astype('float32')
# x_train /= 255
x_test /= 255

# y 值轉成 one-hot encoding
# y_train = keras.utils.to_categorical(y_train, num_classes) ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
y_test = keras.utils.to_categorical(y_test, num_classes)
model = load_model('model2.h5')#----------------------------------------------------------------讀取模型
score = model.evaluate(x_test, y_test, verbose=0)
# x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols)
sample, remain = np.split(x_test,[1],axis = 0)    #--------------------------------------------剪出第一張圖片

preds = model.predict_classes(sample)#-----------------------------------判斷圖片

sample = sample.reshape(28, 28 ,1)
window_name = 'hello'
cv2.imshow(window_name, sample)


print('Test loss:', score[0])
print('Test accuracy:', score[1])
print ('predicted', preds)
print(sample.shape)
key = cv2.waitKey(0)