import numpy as np

def add_horn_turnsig(new_float_array, horn_text, left_sig_text, right_sig_text):
    if horn_text == 'horn activated':
        new_float_array = np.append(new_float_array, 1)#---------------------在陣列後加個喇叭狀態
    else:
        new_float_array = np.append(new_float_array, 0)
    if left_sig_text == 'left turn sig on':
        new_float_array = np.append(new_float_array, 1)
    else:
        new_float_array = np.append(new_float_array, 0)
    if right_sig_text == 'right turn sig on':
        new_float_array = np.append(new_float_array, 1)
    else:
        new_float_array = np.append(new_float_array, 0)
    return new_float_array