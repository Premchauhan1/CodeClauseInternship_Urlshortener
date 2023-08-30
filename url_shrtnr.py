from tkinter import *
import pyshorteners

def shorten_url():
    url = long_url.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    short_url.insert(END, s)


window = Tk()
window.geometry("400x270")
window.config(bg="red")

title = Label(text="Url Shortener", font=("impack 20 bold"), bg="aqua")
title.pack(padx=10, pady=10)
text1 = Label(text="Enter your Link", font=("impack 15 bold"), bg="purple")
text1.pack(padx=10, pady=10)
long_url = Entry(width="200")
long_url.pack(padx=20, pady=5)
enter = Button(text="Submit", font=("impack 10 bold"), bg="purple", command=shorten_url)
enter.pack()

text2 = Label(text="Shortened Url is -", font=("impack 10 bold"), bg="purple")
text2.pack(padx=10, pady=10)
short_url = Entry(width="50")
short_url.pack()

window.mainloop()
