from datetime import datetime
from tkinter import *
from info import *
from tkinter import messagebox
from database_connection import *


window = Tk()
window.title("Life Choices Online")
window.geometry("500x440")


# Will check information
def validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
    try:
        # check for empty space
        if not_empty(name) and not_empty(surname) and not_empty(id_number) and not_empty(phone_number) and not_empty(nok_name) and not_empty(nok_phone_number):
            # Check if id and phone number are numbers
            if len(id_number) == 13 and len(phone_number) == 10 and len(nok_phone_number) == 10:
                #   CHECK  valid
                if not id_valid(id_number):
                    messagebox.showerror("INPUT Error", "Your ID Number is invalid")
                    return False
                else:
                    return True
            else:
                messagebox.showerror("INPUT Error", "Please check ID Number or phone numbers")
                return False
    except ValueError:
        messagebox.showerror("INPUT Error", "Please check your inputs")
    except TypeError:
        messagebox.showerror("INPUT Error", "Please check your ID Number")


def sign_user_up():
    try:
        # Get inputs
        name = name_entry.get()
        surname = surname_entry.get()
        id_number = id_number_entry.get()
        phone_number = phone_number_entry.get()
        nok_name = nok_name_entry.get()
        nok_phone_number = nok_phone_number_entry.get()


        if validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):

            if id_valid(id_number):

                if not user_exists(name, id_number):
                    visitor_id = ""
                    time_in = datetime.now()

                    insert_visitor(name, surname, id_number, phone_number, 1, time_in)


                    query = "SELECT id FROM visitor WHERE name='" + name + "' AND id_number='" + id_number + "';"

                    db_rows = select_from_table(query)

                    for i in db_rows[0]:
                        visitor_id = i


                    insert_nok(nok_name, nok_phone_number, visitor_id)


                    window.destroy()
                    import logged_in

                else:

                    messagebox.showinfo("User exists", "Please go login.")
                    window.destroy()
                    import sign_in
    except ValueError:
        messagebox.showerror("INPUT error", "Please check your entries")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)



heading_label = Label(window, text="Your details", fg="blue", font=("Helvetica", 18))
heading_label.place(x=150, y=10)

name_label = Label(window, text="Please enter name", fg="blue", font="Helvetica")
name_label.place(x=150, y=50)
name_entry = Entry(window)
name_entry.place(x=140, y=70)

surname_label = Label(window, text="Please enter surname", fg="blue", font="Helvetica")
surname_label.place(x=150, y=100)
surname_entry = Entry(window)
surname_entry.place(x=140, y=120)

id_number_label = Label(window, text="Please enter ID Number", fg="blue", font="Helvetica")
id_number_label.place(x=140, y=150)
id_number_entry = Entry(window)
id_number_entry.place(x=140, y=170)

phone_number_label = Label(window, text="Please enter phone number", fg="blue", font="Helvetica")
phone_number_label.place(x=140, y=200)
phone_number_entry = Entry(window)
phone_number_entry.place(x=140, y=220)

heading_label = Label(window, text="Your next of kin details", fg="blue", font=("Helvetica", 18))
heading_label.place(x=120, y=270)

nok_name_label = Label(window, text="Please enter name", fg="blue", font="Helvetica")
nok_name_label.place(x=150, y=300)
nok_name_entry = Entry(window)
nok_name_entry.place(x=140, y=320)

nok_phone_number_label = Label(window, text="Please enter phone number", fg="blue", font="Helvetica")
nok_phone_number_label.place(x=140, y=340)
nok_phone_number_entry = Entry(window)
nok_phone_number_entry.place(x=140, y=360)

sign_in_btn = Button(window, text="SIGN UP", width=50, bg="blue", fg="black", borderwidth=0, command=sign_user_up)
sign_in_btn.place(x=15, y=390)


window.mainloop()
