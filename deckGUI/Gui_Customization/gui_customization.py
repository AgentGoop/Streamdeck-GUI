import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import ImagePath
import os
import webbrowser
import tkinter.messagebox

root = tk.Tk()
root.resizable(width=False, height=False)


current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "images", "qsnmark.png")


root.title("Gui Customization")
root.configure(background="Black")
root.minsize(300,200)
root.maxsize(500,500)
root.geometry("400x200+50+50")


def open_new_window1():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()


    def open_text():
        txt_input = open("Option1.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option1.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option1.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()


def open_new_window2():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option2.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option2.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option2.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window3():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(300,300)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option3.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option3.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option3.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window4():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option4.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option4.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option4.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window5():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option5.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option5.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option5.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window6():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option6.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option6.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option6txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window7():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()

    def open_text():
        txt_input = open("Option7.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option7.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option7.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()

def open_new_window8():
    new_window = Toplevel(root)
    new_window.title("Link Customization")
    txt = tk.Text(new_window, height=5, width=20)
    new_window.minsize(200,200)
    new_window.maxsize(200,200)
    new_window.geometry("200x200+50+50")
    txt.pack()


    def open_text():
        txt_input = open("Option8.txt", "r")
        content = txt_input.read()
        txt.insert(END, content)
        txt_input.close()
    
    def save_text():
        f = open('Option8.txt', 'r+')
        f.truncate(0)
        txt_input = open("Option8.txt", "w")
        txt_input.write(txt.get(1.0, END))
        txt_input.close()
        tkinter.messagebox.showinfo("You have Saved your hyperlink!")

    save = Button(new_window, text="SAVE", command=save_text)
    save.pack()


qsnmark1_btn = PhotoImage(file=image_path)
qsnmark1_label = Label(image=qsnmark1_btn)
qsnmark1= Button(root, image=qsnmark1_btn, command=open_new_window1, borderwidth=0)
qsnmark1.place(x=27, y=10)

qsnmark2_btn = PhotoImage(file=image_path)
qsnmark2_label = Label(image=qsnmark2_btn)
qsnmark2= Button(root, image=qsnmark2_btn, command=open_new_window2, borderwidth=0)
qsnmark2.place(x=117, y=10)

qsnmark3_btn = PhotoImage(file=image_path)
qsnmark3_label = Label(image=qsnmark3_btn)
qsnmark3= Button(root, image=qsnmark3_btn, command=open_new_window3, borderwidth=0)
qsnmark3.place(x=207, y=10)

qsnmark4_btn = PhotoImage(file=image_path)
qsnmark4_label= Label(image=qsnmark4_btn)
qsnmark4= Button(root, image=qsnmark4_btn, command=open_new_window4, borderwidth=0)
qsnmark4.place(x=297, y=10)

qsnmark5_btn = PhotoImage(file=image_path)
qsnmark5_label= Label(image=qsnmark5_btn)
qsnmark5= Button(root, image=qsnmark5_btn, command=open_new_window5, borderwidth=0)
qsnmark5.place(x=27, y=100)

qsnmark6_btn = PhotoImage(file=image_path)
qsnmark6_label= Label(image=qsnmark6_btn)
qsnmark6= Button(root, image=qsnmark6_btn, command=open_new_window6, borderwidth=0)
qsnmark6.place(x=117, y=100)

qsnmark7_btn= PhotoImage(file=image_path)
qsnmark7_label= Label(image=qsnmark7_btn)
qsnmark7= Button(root, image=qsnmark7_btn, command=open_new_window7, borderwidth=0)
qsnmark7.place(x=207, y=100)

qsnmark8_btn = PhotoImage(file=image_path)
qsnmark8_label = Label(image=qsnmark8_btn)
qsnmark8= Button(root, image=qsnmark7_btn, command=open_new_window8, borderwidth=0)
qsnmark8.place(x=297, y=100)

root.mainloop()