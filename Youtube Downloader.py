from tkinter import *
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader")
root.geometry("1024x720")

Label(root, text="Youtube videoDownloader").pack()
link = StringVar()
Label(root, text="Paste Link Here:").pack()
link_enter = Entry(root, width=70, textvariable=link).pack()

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="DOWNLOADED", font='arial').pack()

Button(root, text='DOWNLOAD', bg='grey', command=Downloader).pack()

root.mainloop()