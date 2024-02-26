from tkinter import *

root = Tk()
root.geometry("300x200+1200+221")
root.title("Features")

def show_upcoming_events():
    print("Showing upcoming events")

def add_attendance():
    print("Showing attendance")

def show_events_calendar():
    print("Showing events calendar")

def show_students_list():
    print("Showing")

# Add buttons for features directly to the root window
upcoming_events_btn = Button(root, text="Upcoming Events", command=show_upcoming_events)
upcoming_events_btn.pack(pady=5, fill=X, expand=True)

attendance_btn = Button(root, text="Attendance", command=add_attendance)
attendance_btn.pack(pady=5, fill=X, expand=True)

events_calendar_btn = Button(root, text="Events Calendar", command=show_events_calendar)
events_calendar_btn.pack(pady=5, fill=X, expand=True)

student_list_btn = Button(root, text="Student List", command=show_students_list)
student_list_btn.pack(pady=5, fill=X, expand=True)


root.mainloop()