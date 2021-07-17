import time
from plyer import *
from tkinter import *
my_root = Tk()
my_root.geometry("610x400")
my_root.title("Desktop Notifier")

l1 = Label(text = "Desktop Notifier")
l1.config(font=("Arial",20,"bold"))
l1.pack()

l2 = Label(text = "Add your reminder here...")
l2.config(font=("Arial",10,"bold"))
l2.pack(anchor = "nw", pady =12)

l3 = Label(text = "Title :")
l3.pack(side = LEFT, anchor = "nw",pady =10)

et1 = Entry(width=35)
et1.pack(pady=10)

l4 = Label(text = "Description :")
l4.pack(side = LEFT, anchor = "nw", pady =10)

et2 = Entry(width=35)
et2.pack(pady=10)

l5 = Label(text= "App icon path :")
l5.pack(side = LEFT, anchor = "nw", pady =10)

et3 = Entry(width=35)
et3.pack(pady=10)

l6 = Label(text="Time Period :")
l6.pack(side = LEFT, anchor = "nw", pady =10)

et4 = Entry(width=35)
et4.pack(pady=10)

def add_reminder():
    ttl = et1.get()
    msg = et2.get()
    icon = et3.get()
    sleep = et4.get()
    if __name__ == "__main__":
        while True:
                notification.notify(
                    title = ttl,
                    message = msg,
                    app_icon = icon,
                    timeout = 10
                )
                time.sleep(int(sleep))

    
btn = Button(text = "Add Reminder", command = add_reminder, bg = "blue")
btn.pack(anchor = "nw",pady=50,padx=0)
