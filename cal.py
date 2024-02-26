from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar
from datetime import date


def toggle_menu():
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.place(x=10,y=2)

def show_notifications():
    features_window = Toplevel(root)
    features_window.title("Notifications")
    features_window.geometry("200x200+800+213")


root=Tk()
root.geometry("1500x1500")


header= Canvas(root, width= 1500, height= 300, bg="#001F3F")

header.create_text(850, 140, text="KASA - The Event Manager", fill="white", font=('Cochin',70))
logo= (Image.open("KASA.png"))
resized_image= logo.resize((150,150))
new_image= ImageTk.PhotoImage(resized_image)


header.create_image(30,60, anchor=NW, image=new_image)

header.pack()


# Create a button to show features
features_button = Button(root, text="☰")
features_button.place(x=1350,y=320)

notification_button = Button(root, text="🔔", command=show_notifications)
notification_button.place(x=1300,y=320)

#Calendar Start
mid=Frame(root, width= 1500, height= 1450, bg="white")
name=Label(text="Event Calendar", font=("Georgia",50), background="white", fg="black")
name.pack()

cal= Calendar(root, selectmode = 'day',
               year = 2024, month = 2,
               day = 25)
 
cal.pack(pady = 5)

todays_event="Holi"

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date()+ " and the event for today is: " + todays_event)
 

Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)

mid.pack()







root.mainloop()