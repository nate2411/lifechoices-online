from tkinter import *

window = Tk()
window.title("Life Choices Online")
window.geometry("500x300")

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)


def navigate_to_sign_up():
    window.destroy()
    import sign_up


def navigate_to_sign_in():
    window.destroy()
    import sign_in

def navigate_to_admin_login():
    window.destroy()
    import admin_login

def admin_login(e):
    window.destroy()
    import admin_login

window.bind('<Control-a>', admin_login)



heading_label = Label(window, text="Welcome to life choices online", fg="blue", font=("Helvetica", 18))
heading_label.place(x=80, y=10)

sign_in_btn = Button(window, text="SIGN IN", bg="blue", fg="black", borderwidth=0, height=2, width=20, command=navigate_to_sign_in)
sign_in_btn.place(x=140, y=70)

sign_up_btn = Button(window, text="SIGN UP", bg="blue", fg="black", borderwidth=0, height=2, width=20, command=navigate_to_sign_up)
sign_up_btn.place(x=140, y=130)

admin_login = Button(window, text="Admin", bg="blue", fg="black", borderwidth=0, height=2, width=20, command=navigate_to_admin_login)
admin_login.place(x=140, y=190)
admin_label = Label(window, text="Ctrl + a for ADMIN", fg="blue", font=("Helvetica", 11))
admin_label.place(x=350, y=210)
mainloop()
