# the program may will crash while you spamming *
# importing
from tkinter import *
import pyautogui, time

# the spam command
def spamming():

    for i in range(int(amount.get())):
        time.sleep(0.3)
        pyautogui.write(text.get())
        pyautogui.press('enter')

# making the window
WIN = Tk()
WIN.geometry("500x300")
WIN.title("Spam Bot")

# making the texts and the outputs
lbl = Label(WIN, text="type what you want to spam")
lbl.pack()
text = Entry(WIN)
text.pack()

lbl_amount = Label(WIN, text="Type the amount you want to spam ")
lbl_amount.pack()

amount = Entry(WIN)
amount.pack()

# the spam button
btn = Button(WIN, text="SPAM", bg="#cce3e6", fg="black", command= spamming)
btn.pack()


# this is for stay the window on until i close
WIN.mainloop()
