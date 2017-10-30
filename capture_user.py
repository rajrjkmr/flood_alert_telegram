#! /usr/bin/env python
import sys
import time
import os
import serial
import pygame
import pygame.camera
from os import getenv
from pygame.locals import *
from datetime import datetime as dt
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640, 480))
def capture_image():	
    file_name =  'image.png'
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, file_name)
    cam.stop()
# arduino_board = serial.Serial('/dev/ttyACM0', 9600)
arduino_board = serial.Serial('/dev/device_name', 9600)
while True:
    if arduino_board.inWaiting() > 0:

        data = arduino_board.readline().strip()

        print data
        try:
            data = int(float(data))
            if data <= 100:
            	print data
               	capture_image()
                # os.system('  bin/telegram-cli -k server.pub -W -e "send_photo Raj_p image.png" "safe_quit"')
                
                os.system('  bin/telegram-cli -k server.pub -W -e "send_photo contact_name image.png" "safe_quit"')
                # os.system('  bin/telegram-cli -k server.pub -W -e "msg Raj_p Some Thing Happen" "safe_quit"')
                os.system('  bin/telegram-cli -k server.pub -W -e "msg contact_name Some Thing Happen" "safe_quit"')
                
                time.sleep(1)
        except BaseException, be:
            print be.message
    