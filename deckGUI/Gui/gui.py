import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import os

root = tk.Tk()
root.resizable(width=False, height=False)



root.title("GUI")
root.configure(background="black")
root.minsize(300,200)
root.maxsize(500,500)
root.geometry("400x200+50+50")

def Option_1():
    with open("C:\deckGUI\Gui_Customization\Option1.txt", 'r') as file:
        option1 = file.read().rstrip()
    webbrowser.open(option1)


Option1_btn = PhotoImage(file='white.png')
Option1_label= Label(image=Option1_btn)
Option1= Button(root, image=Option1_btn, command=Option_1, borderwidth=0)
Option1.place(x=27, y=10)



def Option_2():
    with open("C:\deckGUI\Gui_Customization\Option2.txt", 'r') as file:
        option2 = file.read().rstrip('\n')
    webbrowser.open(option2)

Option2_btn = PhotoImage(file='white.png')
Option2_label= Label(image=Option2_btn)
Option2= Button(root, image=Option2_btn, command=Option_2, borderwidth=0)
Option2.place(x=117, y=10)

def Option_3():
    with open("C:\deckGUI\Gui_Customization\Option3.txt", 'r') as file:
        option3 = file.read().rstrip()
    webbrowser.open(option3)


Option3_btn = PhotoImage(file='white.png')
Option3_label= Label(image=Option3_btn)
Option3= Button(root, image=Option3_btn, command=Option_3, borderwidth=0)
Option3.place(x=207, y=10)



def Option_4():
    with open("C:\deckGUI\Gui_Customization\Option4.txt", 'r') as file:
        option4 = file.read().rstrip()
    webbrowser.open(option4)


Option4_btn = PhotoImage(file='white.png')
Option4_label= Label(image=Option4_btn)
Option4= Button(root, image=Option4_btn, command=Option_4, borderwidth=0)
Option4.place(x=297, y=10)


def Option_5():
    with open("C:\deckGUI\Gui_Customization\Option5.txt", 'r') as file:
        option5 = file.read().rstrip()
    webbrowser.open(option5)


Option5_btn = PhotoImage(file='white.png')
Option5_label= Label(image=Option5_btn)
Option5= Button(root, image=Option5_btn, command=Option_5, borderwidth=0)
Option5.place(x=27, y=100)



def Option_6():
    with open("C:\deckGUI\Gui_Customization\Option6.txt", 'r') as file:
        option6 = file.read().rstrip()
    webbrowser.open(option6)


Option6_btn = PhotoImage(file='white.png')
Option6_label= Label(image=Option6_btn)
Option6= Button(root, image=Option6_btn, command=Option_6, borderwidth=0)
Option6.place(x=117, y=100)


def Option_7():
    with open("C:\deckGUI\Gui_Customization\Option7.txt", "r") as file:
        option7 = file.read().rstrip()
    webbrowser.open(option7)


Option7_btn = PhotoImage(file='white.png')
Option7_label= Label(image=Option7_btn)
Option7= Button(root, image=Option7_btn, command=Option_7, borderwidth=0)
Option7.place(x=207, y=100)



def Option_8():
    with open("C:\deckGUI\Gui_Customization\Option8.txt", 'r') as file:
        option8 = file.read().rstrip()
    webbrowser.open(option8)


Option8_btn = PhotoImage(file='white.png')
Option8_label= Label(image=Option8_btn)
Option8= Button(root, image=Option8_btn, command=Option_8, borderwidth=0)
Option8.place(x=297, y=100)

root.mainloop()
