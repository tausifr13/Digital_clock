from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

Label = Label(window, font=("Arial White",78,"bold"), bg="steelblue")
Label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    Label.configure(text=time)
    Label.after(500,clock)

clock()

window.mainloop()
