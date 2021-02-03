from tkinter import *
from PIL import Image, ImageTk
import random
import webbrowser

win = Tk()
win.geometry('700x340')
win.iconbitmap("H:\Python Program\search_engine\Background\zoom.ico")
win.title("Easy Search")
win.resizable(0, 0)
win.wm_attributes("-alpha", 0.9999)




a = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\Glass-Wallpaper-03-1680x1050.jpg"))
b = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\Glass-Wallpaper-27-1280x1024.jpg"))
c = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\Glass-Wallpaper-31-1600x1200.jpg"))
d = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\Glass-Wallpaper-39-1024x768.jpg"))
e = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\pexels-josh-sorenson-831889.jpg"))
f = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\pexels-jessica-lewis-5838461.jpg"))
g = ImageTk.PhotoImage(Image.open("H:\Python Program\search_engine\Background\zoom.ico"))
list = [a, b, c, d, e, f]
p1 = ImageTk.PhotoImage(Image.open("icons8-search-64.jpg"))
r = random.choice(list)
Label(win, image=r).place(x=-2, y=-2)
Label(win, image=p1, bg="lightcyan2", fg="gray40", borderwidth=0, relief="groove", width=25, height=30).place(x=460,
                                                                                                              y=14)
Label(win, text="Easy Search !", fg="orange1", bg="gray40", font=("After Shok", "11", "bold")).place(x=500, y=20)
entry = Entry(win, bg="lightcyan2", fg="brown4", borderwidth=3, relief="ridge", font=("times of roman", "18"), width=35)
#webbrowser==================================================
def webpage():
    if entry.get()=="":
        pass

    else:
       if n.get()=="Google":
           Label(win, image=a1, relief="flat", bg="orange1").place(x=70, y=150)
           webbrowser.open("https://www.google.com/search?q={}".format(entry.get()))
       elif n.get() == 'Yahoo!':
            Label(win, image=a2, relief="flat", bg="orange1").place(x=70, y=150)
            webbrowser.open("https://www.yahoo.com/search?q={}".format(entry.get()))
       elif n.get() == 'Duck duck Go':
            Label(win, image=a3, relief="flat", bg="orange1").place(x=70, y=150)
            webbrowser.open("https://www.duckduckgo.com/search?q={}".format(entry.get()))
       elif n.get() == 'Bing':
            Label(win, image=a5, relief="flat", bg="orange1").place(x=70, y=150)
            webbrowser.open("https://www.bing.com/search?q={}".format(entry.get()))
       elif n.get() == 'Youtube':
            Label(win, image=a4, relief="flat", bg="orange1").place(x=70, y=150)
            webbrowser.open("https://www.youtube.com/search?q={}".format(entry.get()))


Button(win, image=g, relief="ridge", bg="lightcyan2", borderwidth=3,command=webpage).place(x=605, y=151)
entry.place(x=120, y=150)

name = ['Google', 'Yahoo!', 'Duck duck Go', "Bing", "Youtube"]
n = StringVar()
n.set(name[0])

engine = OptionMenu(win, n, *name)
engine.config(bg="lightcyan2", fg="red", font=("Alternity", "10"))
engine.place(x=461, y=190)
a1 = ImageTk.PhotoImage(Image.open('H:\Python Program\search_engine\Background\download.png'))
a2 = ImageTk.PhotoImage(Image.open('H:\Python Program\search_engine\Background\download (3).jpg'))
a3 = ImageTk.PhotoImage(Image.open('H:\Python Program\search_engine\Background\download (2).jpg'))
a4 = ImageTk.PhotoImage(Image.open('H:\Python Program\search_engine\Background\download (4).png'))
a5 = ImageTk.PhotoImage(Image.open('H:\Python Program\search_engine\Background\download (1).png'))
def pop():
    from tkinter import messagebox
    messagebox.showinfo("Easy Search","Piyush Chauhan \nMca 3rd Year \nAbes Engineering College")

Button(win,text="About us",relief="ridge", bg="lightcyan2", borderwidth=3,command=pop).place(x=550,y=300)
Label(win,text=" India ",relief="flat", bg="lightcyan2", borderwidth=3).place(x=617,y=303)



win.mainloop()
