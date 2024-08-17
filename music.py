from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from PIL import ImageTk, Image
from pygame import mixer
import os

colour1 = "#d4ddfc" #lightest blue
colour2 = "#031f80" #dark blue
colour3 = "#8495d1"

window = Tk()
window.title ("Music Player")
window.geometry ('450x550')
window.configure(background=colour1)
window.resizable(False, False)


mixer.init()
l=[]
def folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)
                l.append(song)

def playsong():
    music_name = playlist.get(ACTIVE)
    for song in l:
        index = l.index(music_name)
    playlist.selection_set(index)
    playlist.activate(index)
    mixer.music.load(music_name)
    mixer.music.play() 

def nextsong():
    music_name = playlist.get(ACTIVE)
    for song in l:
        index = l.index(music_name)
    newin = index + 1
    next_song = l[newin]
    playlist.select_clear(index)
    playlist.selection_set(newin)
    playlist.activate(newin)
    mixer.music.load(next_song)
    mixer.music.play() 

def previoussong():
    music_name = playlist.get(ACTIVE)
    for song in l:
        index = l.index(music_name)
    newin = index - 1
    if newin < 0:
        son = l[0]
        playlist.selection_set(0)
        playlist.activate(0)
        mixer.music.load(son)
        mixer.music.play()
    else :
        previous_song = l[newin]
        playlist.select_clear(index)
        playlist.selection_set(newin)
        playlist.activate(newin)
        mixer.music.load(previous_song)
        mixer.music.play() 

top = PhotoImage(file="Images/backgroud-removebg-preview.png")
Label(window, image=top, bg=colour1).pack()

logo = Image.open('Images/logo-removebg-preview.png')
logo = logo.resize((135, 135))
logo = ImageTk.PhotoImage(logo)
Label(window, image=logo, bg=colour1).place(x=45, y=110)

stop = Image.open('Images/stop-removebg-preview.png')
stop = stop.resize((40, 40))
stop = ImageTk.PhotoImage(stop)
Button(window, image=stop, bg=colour1, bd=0, command=mixer.music.stop).place(x=55, y=480)

previous = Image.open('Images/previous-removebg-preview.png')
previous = previous.resize((40, 40))
previous = ImageTk.PhotoImage(previous)
Button(window, image=previous, bg=colour1, bd=0, command=previoussong).place(x=115, y=480)

play = Image.open('Images/play-removebg-preview.png')
play = play.resize((40, 40))
play = ImageTk.PhotoImage(play)
Button(window, image=play, bg=colour1, bd=0, command=playsong).place(x=175, y=480)

pause = Image.open('Images/pause-removebg-preview.png')
pause = pause.resize((40, 40))
pause = ImageTk.PhotoImage(pause)
Button(window, image=pause, bg=colour1, bd=0, command=mixer.music.pause).place(x=235, y=480)

resume = Image.open('Images/resume-removebg-preview.png')
resume = resume.resize((40, 40))
resume = ImageTk.PhotoImage(resume)
Button(window, image=resume, bg=colour1, bd=0, command=mixer.music.unpause).place(x=295, y=480)

next = Image.open('Images/next-removebg-preview.png')
next = next.resize((40, 40))
next = ImageTk.PhotoImage(next)
Button(window, image=next, bg=colour1, bd=0, command=nextsong).place(x=355, y=480)

menu = Image.open('Images/menu1.png')
menu = menu.resize((400, 400))
menu = ImageTk.PhotoImage(menu)
Label(window, image=menu, bg=colour1).pack(padx=10, pady=87)

music_frame = Frame(window, bd=2, relief=RIDGE)
music_frame.place(x=50, y=290, width=350, height=160)

Button(window, text="Open Folder", width=15, height=1, font=("arial",10, "bold"), fg=colour2, bg=colour1, command=folder). place(x=50, y=258)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial",10), fg=colour2, selectbackground=colour2, cursor="hand2", yscrollcommand=scroll.set )
scroll.config(command=playlist.yview)

scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


window.mainloop()