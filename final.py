from tkinter import *
from time import strftime



root=Tk()
root.title("Smart Door ")
root.geometry("1000x520+290+98")
root.config(bg="#242424")
root.resizable(False,False)

#icon image
icon_image=PhotoImage(file="images/icon.png")
root.iconphoto(False,icon_image)


#background image
background_image=PhotoImage(file="images/smart door.png")
Label(root,image=background_image,background="#242424").place(x=-2,y=-2)




# #logo
# logo=PhotoImage(file="images/logo.png")
# myimage1=Label(root,image=logo,background="#111111")
# myimage1.place(x=60,y=35)






# ###
# user_image=PhotoImage(file="images/smart door.png")
# user_button=Button(root,image=user_image,background="#111111",activebackground="#bcdeff",bd=0,cursor='hand2')
# user_button.place(x=940,y=50)




Label(root,text="Eye:",font="Arial 15",bg="#383838",fg="#171717").place(x=500,y=540)
eye_label=Label(root,font="Arial 30 bold",bg="#383838",fg="lightpink")
eye_label.place(x=550,y=530)


door_open=PhotoImage(file="Images/open.png")
door_close=PhotoImage(file="Images/close.png")

door_image=Label(root,image=door_close)
door_image.place(x=700,y=150)

root.mainloop()
