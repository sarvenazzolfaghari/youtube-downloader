from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


win = Tk()
win.title("Youtube Video Downloader")
win.geometry("420x400")
win.resizable(False, False)
win.config(bg="DeepSkyBlue4")

folder_name = ""


def loc_file():
    global folder_name
    folder_name = filedialog.askdirectory()
    location.config(text=folder_name, fg="black")


def dl_video():
    global yt_entry
    url = entryVar.get()
    print(url)
    try:
        yt = YouTube(url)
        print(yt)
        yt.streams.get_highest_resolution().download()
        messagebox.showinfo("Success", "Video Downloaded")

    except:
        messagebox.showerror("Error", "Please insert Url")


label = Label(win, text=" <<Youtube Video Downloader>> ", fg="snow", bg="DeepSkyBlue4", font=("mincho", 20))
label.place(x=23, y=5)

label = Label(win, text="Link :", fg="black", bg="DeepSkyBlue4", font=("mincho", 15, "bold"))
label.place(x=10, y=70)
entryVar = StringVar(win)
yt_entry = Entry(win, width=55, textvariable=entryVar)
yt_entry.place(x=70, y=70)

path = Label(win, text="Save As :", fg="black", bg="DeepSkyBlue4", font=("mincho", 15, "bold"))
path.place(x=10, y=120)
location = Label(win, text="\t\t\t", bg="white", fg="black", font=("mincho", 15))
location.place(x=100, y=120)
save_loc = Button(win, text="...", bg="light gray", fg="black", font=("mincho", 15), command=loc_file)
save_loc.place(x=370, y=120)

dlq = Label(win, text=" Choose Quality: ", fg="black", bg="DeepSkyBlue4", font=("mincho", 15, "bold"))
dlq.place(x=10, y=170)
choices = ["high quality", "low quality", "Only Audio"]
yt_choices = ttk.Combobox(win, values=choices)
yt_choices.current(0)
yt_choices.place(x=170, y=180)

download_btn = Button(win, text="Start Download", width=30, bg="light gray", fg="black", font=("mincho", 15),
                      command=dl_video)
download_btn.place(x=38, y=280)

win.mainloop()
