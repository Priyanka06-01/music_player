import pygame 
from pygame import mixer
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image, ImageTk

image =Tk()
image.geometry("600x500")
image.configure(bg="black")

pygame.mixer.init()

songs=["Hamari-Adhuri-Kahani.mp3","Tera-Ban-Jaunga.mp3",
       "Baatein-Ye-Kabhi-Na-Tu-Bhulna.mp3",
       "Chal-Wahan-Jaate-Hain.mp3",
       "Khairiyat-Pucho.mp3","Roke-Na-Ruke-Naina.mp3",
       "Soch-Na-Sake.mp3","Teri-Galliyan.mp3",
       "Tum-Hi-Ho.mp3","Tum-Mere-Ho.mp3"]

# functions related to play the songs
text="................ LET'S PLAY THE SONG ................"
fr=Label(image,bg="orange",text=text,font=("Arial",25),pady=20,fg="white").pack(side=BOTTOM,fill=X)

def play():
   mixer.music.load(songs[0])
   mixer.music.play()
   #text="PLAYING....................."
   
def pause():
   mixer.music.pause()
   #text="PAUSED....................."
def resume():
   mixer.music.unpause()
   #text="PLAYING....................."
i=1
r=[sub[:-4] for sub in songs] # removing last 4 characters of all strings in list

def next():
    global i
    if i==len(songs):
         i=0
    mixer.music.load(songs[i])
    mixer.music.play()
    i+=1

"""def play_song(s):
     action.configure(text="playing")
     mixer.music.load(s)  
     mixer.music.play()"""
      
# photo =PhotoImage("file=priya.jpg") - jpg files are not supported by tkinter

frame=Frame(image,width=600,height=500,bg="purple",pady=50)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
frame.pack_propagate(0)

# button
button=font.Font(family="Helvetica",size=10,weight="bold")
button4=Button(frame,text="NEXT",width=7,height=1,bg="black",borderwidth=5,font=button,relief=SUNKEN,fg="orange",command=next).pack(side=BOTTOM,pady=10)
button1=Button(frame,text="RESUME",width=7,height=1,bg="black",borderwidth=5,font=button,relief=SUNKEN,fg="orange",command=resume).pack(side=BOTTOM,pady=10)
button2=Button(frame,text="PAUSE",width=7,height=1,bg="black",borderwidth=5,font=button,relief=SUNKEN,fg="orange",command=pause).pack(side=BOTTOM,pady=10)
button3=Button(frame,text="PLAY",width=7,height=1,bg="black",borderwidth=5,font=button,relief=SUNKEN,fg="orange",command=play).pack(side=BOTTOM,pady=10)

frame1=Frame(image,width=300,height=600,bg="white",pady=10)
frame1.pack()
frame1.place(anchor="n",relx=0.9,rely=0.1)
frame1.pack_propagate(0)
#playlist=Listbox(image,selectmode=SINGLE,bg="white").pack()
button5=Button(frame1,text="LIST",width=10,height=1,bg="black",borderwidth=6,fg="red",font=button).pack(side=TOP,pady=8)
for i in range(0,len(songs)):
  button5=Button(frame1,text=r[i],width=25,height=1,bg="black",borderwidth=6,fg="red",font=button,relief=FLAT).pack(side=TOP,pady=8)

# for jpg images
our_image=[
   ImageTk.PhotoImage(Image.open("img1.jpeg"),Image.ANTIALIAS),
   ImageTk.PhotoImage(Image.open("img2.jpeg"),Image.ANTIALIAS),
   ImageTk.PhotoImage(Image.open("img3.jpeg").resize((250,250),Image.ANTIALIAS)),
   ImageTk.PhotoImage(Image.open("img4.jpeg"),Image.ANTIALIAS),
   ImageTk.PhotoImage(Image.open("img5.jpeg"),Image.ANTIALIAS),
   ImageTk.PhotoImage(Image.open("img6.jpeg"),Image.ANTIALIAS),
   ImageTk.PhotoImage(Image.open("img7.jpeg"),Image.ANTIALIAS),
]

l=Label(frame,font="bold")
l.pack()

x=1
# function to display the images 
def move():
    global x
    if x==1:
      l.config(image=our_image[0])
      x=3
    elif x==2:
      l.config(image=our_image[1])
      x=4
    elif x==3:
         l.config(image=our_image[2])
         x=2
    elif x==4:
         l.config(image=our_image[3])
         x=5
    elif x==5:
         l.config(image=our_image[4])
         x=6
    elif x==6:
         l.config(image=our_image[5])
         x=7
    elif x==7:
         l.config(image=our_image[6])
         x=1
    # set images to work automatically
    image.after(1800,move) 
      
move()
image.mainloop()

