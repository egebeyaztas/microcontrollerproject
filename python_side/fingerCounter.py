import cv2
import mediapipe as mp
import os
import time
import HandTrackingModule as htm
from mediapipe.python._framework_bindings import packet
import serial

serialComm = serial.Serial(port='/dev/cu.usbserial-1320', baudrate=9600, timeout=2)

cam_w, cam_h = 320, 240

cap = cv2.VideoCapture(0)
cap.set(3, cam_w)
cap.set(4, cam_h)

detector = htm.handDetector(detectionCon=0.89)

tipIds = [4, 8, 12, 16, 20]

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        fingers = []
        
        if lmlist[tipIds[0]][1] > lmlist[tipIds[1] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        finger_count = fingers.count(1)
        
        #print(finger_count)

        serialComm.write(str(finger_count).encode('utf-8'))
        print(serialComm.readline().decode('utf-8'))

    img = cv2.flip(img, 1)

    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == 27:
        serialComm.write(str(0).encode('utf8'))
        break

serialComm.close()