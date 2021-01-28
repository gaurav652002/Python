from pygame import mixer
from pydub import AudioSegment
from tkinter import *
import os

def playsong():#imports file using 
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():#function to pause the song
    songstatus.set("Paused")
    mixer.music.pause()


def stopsong():#function to stop the song
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():#function to resume a song 
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title('Ankys Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist--------------->>>>>>>>>>

playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)
# add your play list here
os.chdir(r'C:\Users\dell\Music')   # add here
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
#the play button
playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)
#the pause buttom 
pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
#the sto[ button]
stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
#the resume button 
Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()

#credits to anky 
