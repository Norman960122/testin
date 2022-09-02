import numpy as np
img_rows, img_cols = 5, 4

x = np.loadtxt('x_train_short2.txt')   #------------------讀取檔案
y = np.loadtxt('y_train_short2.txt')  
xr = x.reshape(-1, img_rows, img_cols)
print(xr[0])
first_dim = np.random.permutation(xr.shape[0])		#打亂後的行號（將0～1719的數字打亂）
print(x.shape[0])
print(first_dim)
print(type(x))
new_train_X = xr[first_dim, :, :]		#獲取打亂後的訓練資料(照著打亂的array順序創造一個新的檔案)
new_train_y = y[first_dim]
new_train_X = new_train_X.reshape(-1, img_cols)
with open('x_trian_short2s.txt', 'w') as outfile:
    np.savetxt(outfile, new_train_X, delimiter=' ', newline='\n')#另存檔案
with open('y_train_short2s.txt', 'w') as outfile:
    np.savetxt(outfile, new_train_y, delimiter=' ', newline='\n')#另存檔案