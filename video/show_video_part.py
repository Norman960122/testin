import numpy as np
import cv2
def show_video(file_name, start_frame, end_frame, frametime, window_name):
    frame_count = 1
    break_flag = False
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(file_name)

    while(True):
        ret, frame = cap.read()

        if (not ret) or (frame_count > end_frame):
            break
        elif frame_count >= start_frame and frame_count <= end_frame:
            key = cv2.waitKey(frametime)
            if key == ord('q') or break_flag:
                break
            elif key == ord('p'):
                while(True):
                    # print("paused at frame ", frame_count)
                    frame_count_text = str(frame_count)
                    cv2.putText(frame, "paused at frame:" + frame_count_text ,(10,50), font, 1, (255,0,0), 2, cv2.LINE_AA)
                    cv2.imshow(window_name,frame)
                    resume_key = cv2.waitKey(0)
                    if resume_key == ord('p'):
                        break
                    elif resume_key == ord('q'):
                        break_flag = True
                        break
            
            cv2.imshow(window_name,frame)
        frame_count = frame_count + 1

    cap.release()


    print('video ended')