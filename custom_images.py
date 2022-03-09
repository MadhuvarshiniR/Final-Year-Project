
from tkinter import *
from functools import partial
import os
import cv2
import numpy as np
import shutil

background = None
accumulated_weight = 0.5

ROI_top = 100
ROI_bottom = 300
ROI_right = 150
ROI_left = 350


def cal_accum_avg(frame, accumulated_weight):

    global background

    if background is None:
        background = frame.copy().astype("float")
        return None

    cv2.accumulateWeighted(frame, background, accumulated_weight)


def segment_hand(frame, threshold=25):
    global background

    diff = cv2.absdiff(background.astype("uint8"), frame)

    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Grab the external contours for the image
    contours, hierarchy = cv2.findContours(
        thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None
    else:

        hand_segment_max_cont = max(contours, key=cv2.contourArea)

        return (thresholded, hand_segment_max_cont)


def store_gesture(gesture):
    gesture_name = gesture.get().upper()
    path = r"C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\custom\train\\"+gesture_name
    if not os.path.isdir(path):
        os.mkdir(path)
        os.mkdir(
            r"C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\custom\test\\"+gesture_name)
    else:
        print("GESTURES ALREADY EXIST")
        return

    cam = cv2.VideoCapture(0)

    num_frames = 0
    element = gesture_name
    num_imgs_taken = 0

    while True:
        ret, frame = cam.read()

        # filpping the frame to prevent inverted image of captured frame...
        frame = cv2.flip(frame, 1)

        frame_copy = frame.copy()

        roi = frame[ROI_top:ROI_bottom, ROI_right:ROI_left]

        gray_frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

        if num_frames < 60:
            cal_accum_avg(gray_frame, accumulated_weight)
            if num_frames <= 59:

                cv2.putText(frame_copy, "FETCHING BACKGROUND...PLEASE WAIT",
                            (80, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                #cv2.imshow("Sign Detection",frame_copy)

        # Time to configure the hand specifically into the ROI...
        elif num_frames <= 300:

            hand = segment_hand(gray_frame)

            cv2.putText(frame_copy, "Adjust hand...Gesture for" + str(element),
                        (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Checking if hand is actually detected by counting number of contours detected...
            if hand is not None:

                thresholded, hand_segment = hand

                # Draw contours around hand segment
                cv2.drawContours(
                    frame_copy, [hand_segment + (ROI_right, ROI_top)], -1, (255, 0, 0), 1)

                cv2.putText(frame_copy, str(num_frames)+"For" + str(element),
                            (70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Also display the thresholded image
                cv2.imshow("Thresholded Hand Image", thresholded)

        else:

            # Segmenting the hand region...
            hand = segment_hand(gray_frame)

            # Checking if we are able to detect the hand...
            if hand is not None:

                # unpack the thresholded img and the max_contour...
                thresholded, hand_segment = hand

                # Drawing contours around hand segment
                cv2.drawContours(
                    frame_copy, [hand_segment + (ROI_right, ROI_top)], -1, (255, 0, 0), 1)

                cv2.putText(frame_copy, str(num_frames), (70, 45),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                #cv2.putText(frame_copy, str(num_frames)+"For" + str(element), (70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                cv2.putText(frame_copy, str(num_imgs_taken) + 'images' + "For" +
                            str(element), (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Displaying the thresholded image
                cv2.imshow("Thresholded Hand Image", thresholded)
                if num_imgs_taken <= 300:
                    #cv2.imwrite(path+"\\" + str(num_imgs_taken+300) + '.jpg', thresholded)
                    cv2.imwrite(path+"\\" + str(num_imgs_taken) +
                                '.jpg', thresholded)
                    if num_imgs_taken < 40:
                        cv2.imwrite(os.getcwd()+'\\gestures\\test\\'+gesture_name +
                                    "\\" + str(num_imgs_taken) + '.jpg', thresholded)

                else:
                    break
                num_imgs_taken += 1
            else:
                cv2.putText(frame_copy, 'No hand detected...', (200, 400),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Drawing ROI on frame copy
        cv2.rectangle(frame_copy, (ROI_left, ROI_top),
                      (ROI_right, ROI_bottom), (255, 128, 0), 3)

        cv2.putText(frame_copy, "hand sign recognition_ _ _",
                    (10, 20), cv2.FONT_ITALIC, 0.5, (51, 255, 51), 1)

        # increment the number of frames for tracking
        num_frames += 1

        # Display the frame with segmented hand
        cv2.imshow("Sign Detection", frame_copy)

        # Closing windows with Esc key...(any other key with ord can be used too.)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

    # Releasing camera & destroying all the windows...

    cv2.destroyAllWindows()
    cam.release()
    for i in range(0, 40):
        shutil.copy(r"C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\custom\train\\"+element.upper()+"\\"+
                    str(i)+".jpg", r"C:\Users\muhym\Desktop\GUI Main Project\Final-Year-Project\gestures\custom\test\\"+element.upper()+"\\"+str(i)+".jpg")
    

app = Tk()
app.title("Gesture Capture")
app.geometry('400x300')
app.resizable(width=0, height=0)
Header = Label(app, text='Please Enter The Gesture',
               font=("Comic Sans Ms", 18))
Header.place(x=60, y=50)
gesture_label = Label(app, text='Gesture', font=("Comic Sans Ms", 14))
gesture = StringVar()
gesture_entry = Entry(app, textvariable=gesture, font=("Comic Sans Ms", 14))

gesture_label.place(x=45, y=150)
gesture_entry.place(x=130, y=150)
store_gesture = partial(store_gesture, gesture)
button = Button(app, text='Start Capturing', width=29,
                command=store_gesture, font=("Comic Sans Ms", 14))
button.place(x=45, y=200)
app.mainloop()