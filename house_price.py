import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
# save filepath to variable for easier access
melbourne_file_path = 'archive/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data = melbourne_data.dropna(axis=0)     #剪掉含有空格的列（）
y = melbourne_data.Price                           #把房價的行取出來當做label
# print(y.describe())                                #印出資料總數/平均/標準差/中位數/四分位數....
# print(type(y))
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# print(type(melbourne_features))
x = melbourne_data[melbourne_features]             #把list中的5行取出來當做輸入資料
# print(x.describe())
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 0)

# for i in [50,500,5000]:
#     print(get_mae(i, train_x, val_x, train_y, val_y))

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_x, train_y)
melb_preds = forest_model.predict(val_x)
print(mean_absolute_error(val_y, melb_preds))
