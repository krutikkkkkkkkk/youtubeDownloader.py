import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import pytube


root = Tk()

root.title('Youtube Downloader: Reboot13')
root.geometry('500x330') 
root.configure(bg='#222')

heading= Label(root, 
		 text="Youtube Downloader",
         background="#222",
         padding=10,
		 foreground = "red",
		 font =("Arial", 25) ).pack()

placeholder = Label(root, 
		 text="Enter Video URL",
         background="#222",
         padding=10,
		 foreground = "white",
		 font =("monospace", 15) )
placeholder.pack()         

link = Entry(root, width=40)
link.pack()

blank = Label(root, 
		 text="Wait If Program Is Not Responding = (Downloading Video)",
         background="#222",
         padding=10,
		 foreground = "red",
		 font = "monospace").pack()

def downloadVideo():
 url = link.get()
 video = pytube.YouTube(url)
 stream = video.streams.get_highest_resolution()
 stream.download()
 videoTitle = video.title
 videoLabel = Label(root, 
                    text="Video Title:" +videoTitle,
					padding=5,
					foreground= "#fff",
					background= "#222",
					font=("Arial",12) )
 videoLabel.pack()
 downloaded = Label(root,
                     text="Downloaded",
					 padding=5,
					 foreground= "#fff",
					 background= "#222",
					 font=("Arial", 12)).pack()
                       



downloadbutton = Button(root,
                        text='Download Video',
                        command=downloadVideo)

downloadbutton.pack()

codeby = Label(root,text ="© Reboot13",
					foreground= "#fff",
					padding=10,
					font=("monospace",10),
					background= "#222")
 
 
codeby.place(relx = 0.0, 
                 rely = 1.0, 
                 anchor ='sw')


root.mainloop()