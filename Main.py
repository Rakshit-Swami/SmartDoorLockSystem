from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
 

splash_root = Tk()
 
#icon
image_icon=PhotoImage(file="Images/logo.png")
splash_root.iconphoto(False,image_icon)
splash_root.geometry("1200x680+150+100")
 
back_image=PhotoImage(file="Images/background_design.png")
Label(splash_root,image=back_image).pack()



def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        pb['value'] += 30
        
    else:
        messagebox.showinfo(message='The progress completed!')

pb = ttk.Progressbar(
    splash_root,
    orient='horizontal',
    mode='determinate',
    length=280
)

pb.place(x=465,y=400)

pb.start()
 
 
def main():

    splash_root.destroy()
 
    os.system("Register.py")
 
 

splash_root.after(3800, main)
 

mainloop()
