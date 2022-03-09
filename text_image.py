from tkinter import *
from functools import partial
import os
import cv2
from django import conf
import numpy as np
import config


MODEL = "ASL"


def store_text(text):
    text_name = text.get().lower()
    path = config.MODEL_CONFIGS[MODEL][1]
    path += "\\"
    print(text_name)

    for i in text_name:
        if i == " ":
            l = "space"
            dir = path+'space'+'\\1.jpg'
        else:
            l = i
            dir = path+i.upper()+'\\1.jpg'
        image = cv2.imread(dir, 0)

    # Using cv2.imshow() method
    # Displaying the image
        cv2.putText(image, l.upper(), (20, 180),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Text to Sign', image)
        cv2.waitKey(1000)
    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)

    # closing all open windows
    cv2.destroyAllWindows()


app = Tk()
app.title("text Capture")
app.geometry('400x300')
app.resizable(width=0, height=0)
Header = Label(app, text='Please Enter The text', font=("Comic Sans Ms", 18))
Header.place(x=60, y=50)
text_label = Label(app, text='text', font=("Comic Sans Ms", 14))
text = StringVar()
text_entry = Entry(app, textvariable=text, font=("Comic Sans Ms", 14))

text_label.place(x=45, y=150)
text_entry.place(x=130, y=150)
store_text = partial(store_text, text)
button = Button(app, text='TRANSLATE', width=29,
                command=store_text, font=("Comic Sans Ms", 14))
button.place(x=45, y=200)
app.mainloop()
