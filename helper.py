import os
import shutil

letters = os.listdir(
    r'C:\Users\muhym\Desktop\ASL\asl_alphabet_train\asl_alphabet_train')
print(os.getcwd(), letters)

for letter in letters:
    path = r'C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\ASL\train'
    test_path = r'C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\ASL\test'
    os.mkdir(path+"\\"+letter)
    os.mkdir(test_path+"\\"+letter)
    for i in range(0, 301):
        shutil.copy(r'C:\Users\muhym\Desktop\ASL\asl_alphabet_train\asl_alphabet_train\\'+letter+"\\" +
                    str(i)+".jpg", path+"\\"+letter+"\\"+str(i)+".jpg")
    for i in range(0, 40):
        shutil.copy(r'C:\Users\muhym\Desktop\ASL\asl_alphabet_train\asl_alphabet_train\\'+letter+"\\" +
                    str(i)+".jpg", test_path+"\\"+letter+"\\"+str(i)+".jpg")


"""
'''from tkinter import *
from functools import partial
import os
import cv2
import numpy as np



def cal_accum_avg(frame, accumulated_weight):

    global background
    
    if background is None:
        background = frame.copy().astype("float")
        return None

    cv2.accumulateWeighted(frame, background, accumulated_weight)


def segment_hand(frame, threshold=25):
    global background
    
    diff = cv2.absdiff(background.astype("uint8"), frame)

    _ , thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Grab the external contours for the image
    contours, hierarchy = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None
    else:
        
        hand_segment_max_cont = max(contours, key=cv2.contourArea)
        
        return (thresholded, hand_segment_max_cont)


background = None
accumulated_weight = 0.5
#cam = cv2.VideoCapture(0)
num_frames = 0
#element = gesture_name
num_imgs_taken = 0

frame = cv2.imread(r"C:\Users\muhym\Desktop\ASL\asl_alphabet_train\asl_alphabet_train\nothing\180.jpg")
frame = cv2.flip(frame, 1)
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)
cal_accum_avg(gray_frame, accumulated_weight)
frame = cv2.imread(r"C:\Users\muhym\Desktop\ASL\asl_alphabet_train\asl_alphabet_train\M\200.jpg")
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)
hand = segment_hand(gray_frame)
thresholded, hand_segment = hand
cv2.imshow("Thresholded Hand Image", thresholded)
#cv2.imshow('image',gray_frame)
while(True):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()'''
"""
