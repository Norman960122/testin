import pygame
import serial
from time import sleep
import numpy as np

ser2 = serial.Serial('COM15', 9600)
while True:
    while ser2.in_waiting:
            mcu_feedback = ser2.readline().decode()  
            print(mcu_feedback)