from tkinter import *
from tkinter import messagebox
from database_connection import select_from_table

window = Tk()
window.title("Life Choices Online")
window.geometry("500x440")


message = StringVar()


def sign_out():
    sign_out = messagebox.askquestion("Sign out?", "Are you sure you want to sign out?")

    if sign_out == "yes":

        visitor = select_from_table("SELECT * FROM visitor WHERE logged_in = 'true' AND time_out = 'false'")[0]
        ("UPDATE visitor SET logged_in " + str(visitor[0]))
        window.destroy()
        import sign_in

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)



heading_label = Label(window, text="WELCOME BACK", fg="blue", font=("Helvetica", 18))
heading_label.place(x=140, y=120)

sign_out_btn = Button(window, text="SIGN OUT", width=55, bg="blue", fg="black", borderwidth=0, command=sign_out)
sign_out_btn.place(x=10, y=200)

window.mainloop()
