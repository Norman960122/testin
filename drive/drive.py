import pygame

def car_control(keyboard_event, ser, run, save_flag, left_sig_text, right_sig_text, horn_text):
    for event in keyboard_event:
        # print(event)
        if event.type == pygame.QUIT:#----------------------------------------判斷視窗是否被關掉
            run = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                ser.write(b'w\n')
            if event.key==pygame.K_a:
                ser.write(b'a\n')
            if event.key==pygame.K_s:
                ser.write(b's\n')
            if event.key==pygame.K_d:
                ser.write(b'd\n')
            if event.key==pygame.K_UP:
                ser.write(b'h\n')
                horn_text = 'horn activated'
            if event.key==pygame.K_LSHIFT:
                ser.write(b'yy\n')
#------------------------------------------------------------------------------------------------方向燈都是按下來改變狀態
            if event.key==pygame.K_LEFT:
                if left_sig_text == '':
                    left_sig_text = 'left turn sig on'
                    ser.write(b'l\n')
                else:
                    left_sig_text = ''
                    ser.write(b'nl\n')
            if event.key==pygame.K_RIGHT:
                if right_sig_text == '':
                    right_sig_text = 'right turn sig on'
                    ser.write(b'r\n')#---------------------------改變方向燈狀態為“有”
                else:
                    right_sig_text = ''
                    ser.write(b'nr\n')#-------------------------改變方向燈狀態為“無”
#---------------------------------------------------------------------------------------------------方向燈都是按下來改變狀態
            if event.key==pygame.K_f:
                save_flag = True 

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:              
                ser.write(b'nw\n')
            if event.key==pygame.K_a:             
                ser.write(b'na\n')
            if event.key==pygame.K_s:           
                ser.write(b'ns\n')
            if event.key==pygame.K_d:            
                ser.write(b'nd\n')
            if event.key==pygame.K_UP: 
                ser.write(b'nh\n')
                horn_text = ''
            if event.key==pygame.K_LSHIFT:
                ser.write(b'xx\n')
    return run, save_flag, left_sig_text, right_sig_text, horn_text