import numpy as np
img_rows, img_cols = 5, 4

x = np.loadtxt('x_train_short_all.txt')   #------------------讀取檔案
y = np.loadtxt('y_train_short_all.txt')  
reshaped_x = x.reshape(-1, img_rows, img_cols)
first_dim = np.random.permutation(reshaped_x.shape[0])		#打亂後的行號（將0～1719的數字打亂）
print(first_dim)
# print(type(reshaped_x.shape[0]*0.9))
train_index, valid_index, test_index = first_dim[ : int((reshaped_x.shape[0]*0.8))],    first_dim[int((reshaped_x.shape[0]*0.8)) : int((reshaped_x.shape[0]*0.9))],    first_dim[int(reshaped_x.shape[0]*0.9) : reshaped_x.shape[0]]
new_train_X = reshaped_x[train_index, :, :]		#獲取打亂後的訓練資料(照著打亂的array順序創造一個新的檔案)
new_train_y = y[train_index]

new_test_X = reshaped_x[test_index, :, :]		#獲取打亂後的測試資料(照著打亂的array順序創造一個新的檔案)
new_test_y = y[test_index]

new_valid_X = reshaped_x[valid_index, :, :]		#獲取打亂後的validation資料(照著打亂的array順序創造一個新的檔案)
new_valid_y = y[valid_index]

print(new_train_X.shape, new_test_X.shape, new_valid_X.shape)