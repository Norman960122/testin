import cv2
def record(video_counter, save_flag, cap, _CAMERA_WIDTH, _CAMERA_HEIGH, write_flag, out):
    
    
    video_name = 'video_' #儲存影片名稱
    file_type = '.avi' #儲存影片副檔名
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    FPS = 25  #擷取影片頻率
    


    ret, frame = cap.read()
    # if ret == True:
    if save_flag == 1 and write_flag == 0: # 寫入影格
        write_flag = 1
        save_name = video_name + str(video_counter) + file_type
        out = cv2.VideoWriter(save_name, fourcc, FPS, (_CAMERA_WIDTH, _CAMERA_HEIGH))
        # print('writing to ' + save_name)
    elif save_flag == 0 and write_flag == 1: #關閉影片
        write_flag = 0
        video_counter = video_counter + 1
        # print('finish')

    if (write_flag == 1):
        out.write(frame)
        # cv2.waitKey(1)
    cv2.imshow('frame',frame)
    
    return video_counter, out, write_flag
