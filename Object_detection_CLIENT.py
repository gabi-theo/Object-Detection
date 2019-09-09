import time
import cv2
import os
import numpy as np
from imutils.video import VideoStream
import imutils
import socket
import sys
import pickle
import struct
import RPi.GPIO as gpio
from tkinter import *
from tkinter import ttk

#pins initialization
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#Initialize motor1
gpio.setup(22,gpio.OUT)
gpio.setup(3,gpio.OUT)
gpio.setup(18,gpio.OUT)
pwma = gpio.PWM(18, 50)
pwma.start(50)

#Initialize standby
gpio.setup(25,gpio.OUT)

#Initialize motor1
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setup(17,gpio.OUT)
pwmb = gpio.PWM(17,50)
pwmb.start(50)

gpio.output(25, gpio.LOW)

#Initialize servo-motor for arm
servoPin = 20
gpio.setup(servoPin, gpio.OUT)
p = gpio.PWM(servoPin,50)
p.start(5)
p.ChangeDutyCycle(20)
time.sleep(1)

#defining functions for motor movement
def get_inchide():
    p.ChangeDutyCycle(3)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

def get_deschide():
    p.ChangeDutyCycle(20)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    
def get_stanga():

    gpio.output(25, gpio.HIGH)

    gpio.output(22, gpio.HIGH)
    gpio.output(3, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)
    pwmb.ChangeDutyCycle(30)
    pwma.ChangeDutyCycle(30)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

def get_dreapta():
    gpio.output(25, gpio.HIGH)

    gpio.output(22, gpio.LOW)
    gpio.output(3, gpio.HIGH)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    pwmb.ChangeDutyCycle(30)
    pwma.ChangeDutyCycle(30)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

def get_stop():
    gpio.output(25, gpio.LOW)
    
def get_inainte():
    gpio.output(25, gpio.HIGH)
    
    gpio.output(22, gpio.HIGH)
    gpio.output(3, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    pwmb.ChangeDutyCycle(30)
    pwma.ChangeDutyCycle(30)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

#establishing connection to Server
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("192.168.1.5", 5555))
usingPiCamera = True
# Set initial frame size.
frameSize = (640, 480)

# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
                framerate=32).start()
# Allow the camera to warm up.
time.sleep(2.0)
key = cv2.waitKey(1)
print("Sending frames")

while True:
        # Get the next frame.
        frame = vs.read()
        data = pickle.dumps(frame)
        clientsocket.sendall(struct.pack("L", len(data)) + data)        
        # Analizing the message received from the Server and moving based on that
        full_msg = ''
        msg = clientsocket.recv(8)
        full_msg += msg.decode('utf-8')
        if len(full_msg) > 0:
                if full_msg == 'cauta':
                        get_dreapta()
                elif full_msg == 'dreapta':
                        get_dreapta()
                elif full_msg == 'stanga':
                        get_stanga()
                elif full_msg == 'centru':
                        get_inainte()
                elif full_msg == 'inchide':
                        get_stop()
                        time.sleep(3)
                        get_inchide()
                        time.sleep(2)
                        print('Done')
                        break

        # if the `q` key was pressed, break from the loop.
        if key == ord("q"):
                break

#defining functions for GUI

def get_close(event):
    p.ChangeDutyCycle(3)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

def get_open(event):
    p.ChangeDutyCycle(20)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    
def get_left(event):

    gpio.output(25, gpio.HIGH)

    gpio.output(22, gpio.HIGH)
    gpio.output(3, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.output(24, gpio.HIGH)
    pwmb.ChangeDutyCycle(50)
    pwma.ChangeDutyCycle(50)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

def get_right(event):
    gpio.output(25, gpio.HIGH)

    gpio.output(22, gpio.LOW)
    gpio.output(3, gpio.HIGH)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    pwmb.ChangeDutyCycle(50)
    pwma.ChangeDutyCycle(50)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

def get_stai(event):
    gpio.output(25, gpio.LOW)
    
def get_forwoard(event):
    gpio.output(25, gpio.HIGH)
    
    gpio.output(22, gpio.HIGH)
    gpio.output(3, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.output(24, gpio.LOW)
    pwmb.ChangeDutyCycle(50)
    pwma.ChangeDutyCycle(50)
    time.sleep(0.5)
    gpio.output(25, gpio.LOW)

#creating the GUI
root = Tk()

root.title('Robot_gui')
root.geometry('600x300')
root.resizable(width = False, height = False)

C = Canvas(root, bg = ‘blue’, height = 600, width = 300)
filename = PhotoImage(file = ‘gui_bg.png’)
background_label = Label(root, image = filename)
backgroun_label.place(x=0, y=0, relwidth = 1, relheight = 1)

style=ttk.Style()
style.configure('TButton',
                font = 'Serif 15',
                padding = 10)

#binding the buttons with the correct functions
button_Inainte = ttk.Button(root,text = 'Inainte')
button_Inainte.bind('<Button-1>',get_forwoard)
button_Inainte.place(x = 250, y = 10)

button_Stanga = ttk.Button(root,text = 'Stanga')
button_Stanga.bind('<Button-1>',get_left)
button_Stanga.place(x = 10, y = 150)

button_Dreapta = ttk.Button(root,text = 'Dreapta')
button_Dreapta.bind('<Button-1>',get_right)
button_Dreapta.place(x = 480, y  = 150 )

button_Stop = ttk.Button(root,text = 'Stop')
button_Stop.bind('<Button-1>',get_stai)
button_Stop.place(x = 250, y = 150)


button_Inchide = ttk.Button(root,text = 'Inchide')
button_Inchide.bind('<Button-1>',get_close)
button_Inchide.place(x = 150, y = 250)


button_Deschide = ttk.Button(root,text = 'Deschide')
button_Deschide.bind('<Button-1>',get_open)
button_Deschide.place(x = 350, y = 250)



C.pack()
root.mainloop()


# Cleanup before exit.

cv2.destroyAllWindows()
vs.stop()
