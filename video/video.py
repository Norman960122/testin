import numpy as np
import cv2
from show_video_part import show_video
from show_image import show_img
_CAMERA_WIDTH = 640  #攝影機擷取影像寬度
_CAMERA_HEIGH = 480  #攝影機擷取影像高度


frametime = 40  #-------------------------------------------time for each frame
file_name= input("enter file name:")
fps = input("enter video fps:")
frame_interval = float(fps) * 3
frame_shift = frame_interval / 10
arr_num = 0  

while True:
    start_frame = arr_num * int(frame_shift)
    end_frame = start_frame + int(frame_interval)
    window_name = show_img(_CAMERA_HEIGH, _CAMERA_WIDTH, start_frame, end_frame, arr_num)
    # print('frames from', start_frame, 'to', end_frame, '/matrix ', arr_num)

    key = cv2.waitKey(0)
    if key == ord('n'):
        arr_num = arr_num + 1
    elif key == ord('p'):
        show_video(file_name, start_frame, end_frame, frametime, window_name)
    elif key == ord('b'):
        arr_num = arr_num - 1
    elif key == 27:
        break
    if arr_num > 19:
        break
    elif arr_num < 0:
        arr_num = 0


cv2.destroyAllWindows()
print("bye")
        