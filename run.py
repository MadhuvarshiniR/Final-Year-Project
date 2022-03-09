from tkinter import *
from functools import partial
import os


def store_gesture():
    # os.system('')
    os.system('python custom_images.py')


def train():
    os.system('python dynamic_training.py')


def text_to_sign():
    os.system('python text_image.py')


def predictor():
    os.system('python dynamic_predictor.py')


def asl_predict():
    os.system('python Application.py')


main_app = Tk()
main_app.title("TWO WAY SIGN INTERPRETER")
main_app.geometry('700x700')
main_app.resizable(width=0, height=0)
Header = Label(main_app, text='HOME',
               font=("Comic Sans Ms", 28))
Header.place(x=290, y=50)
button = Button(main_app, text='ADD CUSTOM DATA', width=45,
                command=store_gesture, font=("Comic Sans Ms", 14))
button.place(x=100, y=200)
button2 = Button(main_app, text='TRAIN ON CUSTOM DATA', width=45,
                 command=train, font=("Comic Sans Ms", 14))
button2.place(x=100, y=300)

button3 = Button(main_app, text='PREDICT ON CUSTOM DATA', width=45,
                 command=predictor, font=("Comic Sans Ms", 14))
button3.place(x=100, y=400)

button5 = Button(main_app, text='ASL PREDICTOR', width=45,
                 command=asl_predict, font=("Comic Sans Ms", 14))
button5.place(x=100, y=500)

button4 = Button(main_app, text='TEXT TO SIGN COVERSION', width=45,
                 command=text_to_sign, font=("Comic Sans Ms", 14))
button4.place(x=100, y=600)

main_app.mainloop()
