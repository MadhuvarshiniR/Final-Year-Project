from tkinter import *
from functools import partial
from custom_images import store_gesture



main_app = Tk()
main_app.title("TWO WAY SIGN INTERPRETER")
main_app.geometry('700x700')
main_app.resizable(width=0, height=0)
Header = Label(main_app, text='HOME',
               font=("Comic Sans Ms", 28))
Header.place(x=290, y=50)
button = Button(main_app, text='ADD CUSTOM DATA', width=29,
                command=store_gesture, font=("Comic Sans Ms", 14))
button.place(x=290, y=300)

main_app.mainloop()
