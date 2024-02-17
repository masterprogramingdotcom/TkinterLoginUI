import tkinter as tk
import threading
from PIL import ImageTk
import tkinter.messagebox as messagebox
from tkinter import *
import requests

BASE_URL = "http://127.0.0.1:8000/"
LOGIN_URL = "account/login/"


def clear_data(user_entry, pass_entry):
    user_entry.delete(0, END)
    pass_entry.delete(0, END)

def login(win,user_entry, pass_entry):
    username = user_entry.get()
    password = pass_entry.get()

    # POST / accounts
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{BASE_URL}{LOGIN_URL}", data = data)
    
    if response.status_code == 200:
        messagebox.showinfo("Successfully", response.json()['message'])
        win.destroy()
        # Dashboard 
        import dashboard
    else:
        messagebox.showerror("Login failed", response.json()['message'])
  

def login_window():
    win = tk.Tk()
    win.title("iDanish - Login")
    win.iconbitmap("icon.ico")

    # Window Size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    # Background Main Image
    img_head = ImageTk.PhotoImage(file="login_main.jpg")
    head_label = tk.Label(win, image=img_head)
    head_label.place(x=-60, y=-2)

    # Footer Image
    img_footer = ImageTk.PhotoImage(file="login_footer.jpg")
    footer_label = tk.Label(win, image=img_footer)
    footer_label.place(x=25, y=400)

    # Lables 
    username_label = Label(win,  text="User Name :", font="Verdana 10 bold", bg="#e4e4e6", fg="black")
    username_label.place(x=80, y=220)

    password_label = Label(win,  text="Password :", font="Verdana 10 bold", bg="#e4e4e6", fg="black")
    password_label.place(x=80, y=263)

    # Entry Box
    user_name = StringVar()
    password = StringVar()

    user_entry = Entry(win, width=40, bd="5" , textvariable=user_name)
    user_entry.focus()
    user_entry.place(x=200, y=223)

    pass_entry = Entry(win, width=40, bd="5", show="*", textvariable=password)
    pass_entry.place(x=200, y=260)

    # Button
    btn_login = Button(win, text="Login", font="Verdana 10 bold", command=lambda : login(win, user_entry, pass_entry))
    btn_login.place(x=200, y=340)

    btn_clear = Button(win, text="Clear", font="Verdana 10 bold", command= lambda: clear_data(user_entry, pass_entry))
    btn_clear.place(x=260, y=340)




    win.mainloop()

if __name__ == '__main__':
    threading.Thread(target=login_window).start()