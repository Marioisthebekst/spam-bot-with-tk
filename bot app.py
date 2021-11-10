from tkinter import *
import pyautogui, time

def spamming():
    for i in range(int(amount.get())):
        time.sleep(0.3)
        pyautogui.write(text.get())
        pyautogui.press('enter')

WIN = Tk()
WIN.geometry("500x300")
WIN.title("Spam Bot")

lbl = Label(WIN, text="type what you want to spam")
lbl.pack()

text = Entry(WIN)
text.pack()

lbl_amount = Label(WIN, text="Type the amount you want to spam ")
lbl_amount.pack()

amount = Entry(WIN)
amount.pack()

btn = Button(WIN, text="Spam!", bg="#cce3e6", fg="black", command= spamming)
btn.pack()

WIN.mainloop()