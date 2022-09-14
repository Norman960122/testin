import numpy as np
new_arr = np.zeros([ 5, 4])
wrong_index = np.empty([])

x_train = np.loadtxt('x_train_short3.txt')
y_train = np.loadtxt('y_train_short3.txt')

x_train = x_train.reshape(-1, 5, 4)
result = np.where(y_train == 4)

# print(type(result[0][0]))
# print(x_train[1, :, :].shape)
# for i in result[0]:
#     a =  x_train[i, :, :]
#     print('----------------------------------------------')
#     new_arr = np.concatenate((new_arr, a), axis = 0)
    # print(x_train[i, :, :])
    # print('\n')
# print(new_arr.shape)
# with open('insp2', 'a') as outfile:
#     np.savetxt(outfile, new_arr, delimiter=' ', newline='\n') #  

for i in result[0]:

    if x_train[i, 0, 2] == 0:
        print(i)
        wrong_index = np.append(wrong_index, i)
   
# print(wrong_index)