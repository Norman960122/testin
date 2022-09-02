import numpy as np
import cv2
def show_img(_CAMERA_HEIGH, _CAMERA_WIDTH, start_frame, end_frame, arr_num):
    window_name = 'image' #   設定視窗名
    img = np.ones((_CAMERA_HEIGH, _CAMERA_WIDTH, 3), dtype="uint8")#    設定圖案
    img[:] = (255, 255, 255)#--------------------------------畫布顏色
    start_frame_text = str(start_frame)
    end_frame_text = str(end_frame)
    arr_num_text = str(arr_num + 1)
    current_arr_text = 'frames from '+ start_frame_text + ' to '+ end_frame_text +' / matrix '+ arr_num_text
    # cv2.line(img,(0,0),(200,300),(255,255,255),50)#-----------------------------------------畫圖形(not needed)
    # cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
    # cv2.circle(img,(447,63), 63, (0,255,0), -1)
    # pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
    # pts = pts.reshape((-1,1,2))
    # cv2.polylines(img, [pts], True, (0,255,255), 3)#----------------------------------------畫圖形
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'press p to play and pause',(10,50), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img,'press n to next clip',(10,100), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img,'press b to previous clip',(10,150), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img,'press q to quit playing clip',(10,200), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img,'press ESC to exit',(10,250), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, current_arr_text,(10,300), font, 1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow(window_name, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return window_name