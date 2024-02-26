#Importing Necessary modules
from tkinter import *
from PIL import Image,ImageTk

#Defining functions

def show_features():
    # Create a new window to display features
    features_window = Toplevel(root)
    features_window.title("Features")
    features_window.geometry("200x200+1200+200")

    # Add buttons for features
    upcoming_events_btn = Button(features_window, text="Upcoming Events")
    upcoming_events_btn.pack(pady=5, fill=X, expand=True)

    attendance_btn = Button(features_window, text="Attendance")
    attendance_btn.pack(pady=5, fill=X, expand=True)

    events_calendar_btn = Button(features_window, text="Events Calendar")
    events_calendar_btn.pack(pady=5, fill=X, expand=True)

    more_btn = Button(features_window, text="More")
    more_btn.pack(pady=5, fill=X, expand=True)


def toggle_menu():
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.place(x=10,y=2)

def show_notifications():
    features_window = Toplevel(root)
    features_window.title("Notifications")
    features_window.geometry("200x200+1200+200")

#Creating a new window
root=Tk()
root.geometry("1500x1500")

#For the top header with navy blue color
header= Canvas(root, width= 1500, height= 120, bg="#001F3F")

header.create_text(550, 70, text="KASA - The Event Manager", fill="white", font=('Cochin',70))
logo= (Image.open("KASA.png"))
resized_image= logo.resize((60,60))
new_image= ImageTk.PhotoImage(resized_image)


header.create_image(30,30, anchor=NW, image=new_image)

header.pack()

mid=Canvas(height=1450, width=1500, bg="white")

# Create a button to show features
features_button = Button(root, text="☰", command=show_features)
features_button.place(x=1350,y=130)

#Create a button to show notifications
notification_button = Button(root, text="🔔", command=show_notifications)
notification_button.place(x=1300,y=130)

#Adding things in mid part
mid.create_text(700,60,text="Event Attendance",fill="black", font=("Cochin",60), anchor="center")

#Addin grey boxes 
mid.create_rectangle(100,150, 650, 700, fill="grey")
mid.create_rectangle(700,150, 1250, 700, fill="grey")

#Adding text in grey boxes
mid.create_text(380,200,text="Holi",fill="black", font=("Cochin",60))
mid.create_text(980,200,text="Christmas",fill="black", font=("Cochin",60))

#Adding Holi picture
holi_photo= (Image.open("Holi.jpg"))
naya_image= holi_photo.resize((150,150))
final_image= ImageTk.PhotoImage(naya_image)


mid.create_image(320,250, anchor=NW, image=final_image)

#Adding Christmas Picture
christmas_photo= (Image.open("Christmas.jpg"))
feri_image= christmas_photo.resize((150,150))
last_image= ImageTk.PhotoImage(feri_image)


mid.create_image(900,250, anchor=NW, image=last_image)

#Checkbox for Present and Absent
#GreyBox 1

from tkinter.ttk import *

v = StringVar(root, "1") 
 
# Dictionary to create multiple buttons 
values = {"Present ✅" : "1", 
        "Absent ❌" : "2", } 
 

for (text, value) in values.items(): 
    Radiobutton(root, text = text, variable = v, 
        value = value).pack(side = TOP, ipady = 5) 


mid.pack()

root.mainloop()