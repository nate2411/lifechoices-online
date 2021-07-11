from tkinter import *
from tkinter import messagebox
from info import *
login_screen = Tk()
login_screen.geometry("500x450")
login_screen.title("Lifechoices online")


def clear():
    username.delete(0, END)
    password.delete(0, END)
    email.delete(0, END)

def confirm():  # function to make sure correct details are entered
    if username.get() == "Ethan" and password.get() == "ethan001" and email.get() == "ethan1234@gmail.com":
        login_screen.destroy()
        import admin
    else:  # if incorrect name or password entered will tell user details are incorrect
        messagebox.showerror("ERROR", "Incorrect details entered")


email_var = StringVar()
username_var = StringVar()
password_var = StringVar()
message_var = StringVar()
Label(login_screen, text="WELCOME BACK", fg="blue", font=("Helvetica", 18)).place(x=150, y=20)
#Username Label
Label(login_screen, text="Username", fg="blue", font=("Helvetica")).place(x=190,y=90)
#Username textbox
username = Entry(login_screen, textvariable=username_var)
username.place(x=140,y=110)
#Password Label
Label(login_screen, text="Password", fg="blue", font=("Helvetica")).place(x=190,y=140)
#Password textbox
password = Entry(login_screen, textvariable=password_var ,show="*")
password.place(x=140,y=160)
 #Email Label
Label(login_screen, text="Email", fg="blue", font=("Helvetica")).place(x=200,y=200)
#Email textbox
email = Entry(login_screen)
email.place(x=140,y=220)

#Login button
Button(login_screen, text="Login", width=50, height=1, bg="blue", command=confirm).place(x=40,y=290)
Button(login_screen, text="Clear", width=50, height=1, bg="blue", command=clear).place(x=40,y=340)

login_screen.mainloop()













