import pygame


def get_new_text(keys, save_flag):
    moving_direction_text = ''
    record_text = ''

    
    if keys[pygame.K_w] and keys[pygame.K_a] and keys[pygame.K_d]:#-----按下wad
        moving_direction_text = 'forward'
        # ser.write(b'w\n')
    elif keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_d]:#-----按下sad
        moving_direction_text = 'backward'
        # ser.write(b'b\n')
    elif keys[pygame.K_w] and keys[pygame.K_a]:#----------------------按下wa
        moving_direction_text = 'forward left'
        # ser.write(b'fl\n')
    elif keys[pygame.K_w] and keys[pygame.K_d]:#----------------------按下wd
        moving_direction_text = 'forward right'
        # ser.write(b'fr\n')
    elif keys[pygame.K_a] and keys[pygame.K_d]:#----------------------按下ad
         moving_direction_text = ''
    elif keys[pygame.K_s] and keys[pygame.K_a]:#----------------------按下sa
        moving_direction_text = 'backward left'
        # ser.write(b'bl\n')
    elif keys[pygame.K_s] and keys[pygame.K_d]:#----------------------按下sd
        moving_direction_text = 'backward right'
        # ser.write(b'br\n')
    elif keys[pygame.K_w]:
        moving_direction_text = 'forward'
        # ser.write(b'f\n')
    elif keys[pygame.K_a]:
        moving_direction_text = 'left'
        # ser.write(b'l\n')
    elif keys[pygame.K_s]:
        moving_direction_text = 'backward'
        # ser.write(b'b\n')
    elif keys[pygame.K_d]:
        moving_direction_text = 'right'
        # ser.write(b'r\n')
    if save_flag:
        record_text = 'recording'
    
    return moving_direction_text, record_text