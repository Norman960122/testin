import pygame
import serial
import cv2
from time import sleep
from time import time
import numpy as np
from drive_func import car_control
from drive_func import get_new_text
from drive_func import add_horn_turnsig
from video_func import record

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def change_str_float_array(feedback):
    a = feedback.split(',')
    a.remove('\n')
    b = np.array(a)
    b = b.astype('float')
    return b
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

file_name = input("enter file name to write into:")
COM_number = input("enter com port number:")
cam_number = input("enter cam number:")
video_counter = int(input("enter the first video number:"))
COM_PORT = 'COM' + COM_number  # -------------------------------------------------------------序列埠名稱
BAUD_RATES = 38400
#---------------------------------------------------------------------- Screen width, height
S_W = 500
S_H = 500
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

left_sig_text = ''
right_sig_text = ''
moving_direction_text = ''
horn_text = ''
record_text = ''

run = True
save_flag = False #---------------------------------------------------------------是否開始存陣列
array_hight = 10 #-------------------------------------------------------------------儲存的陣列高度
onetime = 0
arr_save_counter = 0 #-----------------------------------------------------------儲存陣列用的計數器
times_to_save = 20 #---------------------------------------------------------------一次要儲存幾個陣列



write_flag = 0  #判斷是否為寫入模式
out = 0
cap = cv2.VideoCapture(int(cam_number))
_CAMERA_WIDTH = 640  #攝影機擷取影像寬度
_CAMERA_HEIGH = 480  #攝影機擷取影像高度
cap.set(cv2.CAP_PROP_FRAME_WIDTH, _CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, _CAMERA_HEIGH)
# 設定擷取影像的尺寸大小


ser = serial.Serial(COM_PORT, BAUD_RATES, timeout = 0.01)
pygame.init()#---------------------------------------------------------------pygame初始化
winScreen = pygame.display.set_mode((S_W, S_H))
winScreen.fill([255,255,255])
pygame.display.set_caption("Keyboard Demo")
my_font = pygame.font.SysFont(None, 30)
clean_buffer = ser.readall().decode()#-------------------------------------------清空serial緩衝器裡面的值

while run:
    time_start = time()
    pygame.time.Clock().tick(32)#--------------------------------------------設定每秒迴圈執行次數

    run, save_flag, left_sig_text, right_sig_text, horn_text = car_control(pygame.event.get(), ser, run, save_flag, left_sig_text, right_sig_text, horn_text)#車子控制涵式
   
    video_counter, out, write_flag= record(video_counter, save_flag, cap, _CAMERA_WIDTH, _CAMERA_HEIGH, write_flag, out)
    
    
    
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  #------------------------------ 接收回應訊息並解碼
        # print(mcu_feedback)
        new_float_array = change_str_float_array(mcu_feedback)
        new_float_array = add_horn_turnsig(new_float_array, horn_text, left_sig_text, right_sig_text)
        if onetime == 0:
            float_array_2d = new_float_array
            onetime = onetime + 1
        float_array_2d = np.vstack((float_array_2d, new_float_array))#-----------新列加到舊列下
        float_array_2d_hight = float_array_2d.shape[0]

        if float_array_2d_hight == array_hight:
#/////////////////////////////////////////////////////////////////////////     儲存資料部分
            if arr_save_counter == array_hight :#開始儲存時
                float_array_3d = float_array_2d
            if save_flag and (arr_save_counter > array_hight) and (arr_save_counter < (times_to_save + array_hight)):#等待（矩陣長度減一）之後才開始存才會存到0秒之後的矩陣
                float_array_3d = np.concatenate((float_array_3d, float_array_2d), axis = 0)
            print(save_flag)
            print(arr_save_counter)
            if save_flag:
                arr_save_counter = arr_save_counter + 1
            if arr_save_counter >= (times_to_save + array_hight):
                with open(file_name, 'a') as outfile:
                    np.savetxt(outfile, float_array_3d, delimiter=' ', newline='\n') #    dellimiter 每個元素間隔  ，newline 每列結束的字元
                    # outfile.write('\n')
                save_flag = False
                arr_save_counter = 0
#///////////////////////////////////////////////////////////////////
            print(float_array_2d)
            float_array_2d = np.delete(float_array_2d, (0), axis = 0)#-----------刪除第一列
            print('\n')
    keys = pygame.key.get_pressed()#----------------------------------------------偵測被按下的按鍵
    moving_direction_text, record_text = get_new_text(keys, save_flag)#更新要印出的文字    

    horn_text_surface = my_font.render(horn_text, True, blue)
    drive_text_surface = my_font.render(moving_direction_text, True, red)
    L_turn_text_surface = my_font.render(left_sig_text, True, blue)#---------------------------左方向燈狀態文字
    R_turn_text_surface = my_font.render(right_sig_text, True, blue)#---------------------------右方向燈狀態文字
    record_text_surface =  my_font.render(record_text, True, (0, 0, 0))
    winScreen.fill([255,255,255])
    winScreen.blit(drive_text_surface, (170, 10))#------------------------------------印出文字
    winScreen.blit(L_turn_text_surface, (10, 25))
    winScreen.blit(R_turn_text_surface, (320, 25))
    winScreen.blit(horn_text_surface, (160, 45))
    winScreen.blit(record_text_surface, (160, 70))
    pygame.display.update()
    time_end = time() 
    print(time_end - time_start, 's')
ser.close()
print("再見")
cap.release()
if not (type(out) == 'int'):
    out.release()
cv2.destroyAllWindows()
pygame.quit()