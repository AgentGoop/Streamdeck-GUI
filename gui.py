import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import os

root = tk.Tk()
root.resizable(width=False, height=False)


Youtube_url = "https://www.youtube.com"
Outlook_url = "https://outlook.live.com/mail/0/"
gmail_url = "https://mail.google.com/mail/u/0/#inbox"

root.title("GUI")
root.configure(background="black")
root.minsize(300,200)
root.maxsize(500,500)
root.geometry("400x200+50+50")

def YouTube_command():
    webbrowser.open(Youtube_url)

YouTube_btn = PhotoImage(file='YouTube.png')
YouTube_label= Label(image=YouTube_btn)
YouTube= Button(root, image=YouTube_btn, command=YouTube_command, borderwidth=0)
YouTube.place(x=27, y=10)

def Steam_command():
    def __init__(self, master):
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open', command = self.openFile)
        self.b.grid(row = 1)
        self.frame.grid()
    os.startfile('\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk')

Steam_btn = PhotoImage(file='Steam.png')
Steam_label= Label(image=Steam_btn)
Steam= Button(root, image=Steam_btn, command=Steam_command, borderwidth=0)
Steam.place(x=117, y=10)

def Outlook_command():
    webbrowser.open(Outlook_url)

Outlook_btn = PhotoImage(file='Outlook.png')
Outlook_label= Label(image=Outlook_btn)
Outlook= Button(root, image=Outlook_btn, command=Outlook_command, borderwidth=0)
Outlook.place(x=207, y=10)

def Discord_command():
    def __init__(self, master):
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open', command = self.openFile)
        self.b.grid(row = 1)
        self.frame.grid()
    os.startfile(r"\Users\Kiera\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")

Discord_btn= PhotoImage(file='discord.png')
Discord_label= Label(image=Discord_btn)
Discord= Button(root, image=Discord_btn, command=Discord_command, borderwidth=0)
Discord.place(x=297, y=10 )

def Gmail_command():
    webbrowser.open(gmail_url)

Gmail_btn = PhotoImage(file='Gmail.png')
Gmail_label= Label(image=Gmail_btn)
Gmail= Button(root, image=Gmail_btn, command=Gmail_command, borderwidth=0)
Gmail.place(x=27, y=100)

def vss_command():
    def __init__(self, master):
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open', command = self.openFile)
        self.b.grid(row=1)
        self.frame.grid()
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2022.lnk")


vss_btn = PhotoImage(file='vss.png')
vss_label= Label(image=vss_btn)
vss= Button(root, image=vss_btn, command=vss_command, borderwidth=0)
vss.place(x=117, y=100)

def settings_command():
    def __init__(self, master):
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open', command = self.openFile)
        self.b.grid(row=1)
        self.frame.grid()
    os.startfile(r"ms-settings:privacy-location")

settings_btn = PhotoImage(file='settings.png')
settings_label= Label(image=settings_btn)
settings= Button(root, image=settings_btn, command=settings_command, borderwidth=0)
settings.place(x=207, y=100)

def cmd_command():
    def __init__(self, master):
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open', command = self.openFile)
        self.b.grid(row=1)
        self.frame.grid()
    os.startfile(r'\Users\Kiera\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk')

cmd_btn= PhotoImage(file='cmd.png')
cmd_label= Label(image=cmd_btn)
cmd= Button(root, image=cmd_btn, command=cmd_command, borderwidth=0)
cmd.place(x=297, y=100)

root.mainloop()
