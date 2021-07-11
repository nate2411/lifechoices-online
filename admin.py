from tkinter import *
from tkinter import messagebox
from database_connection import *
from tkinter.ttk import Style, Treeview
from datetime import datetime
from info import *


window = Tk()
window.geometry("1100x550")
window.title("Life Choices Online")

def populate_entries():
    try:

        clear_entries()


        selected_id = tree_view.focus()

        visitor = tree_view.item(selected_id, 'values')

        nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
        nok = select_from_table(nok_query)[0]


        name_entry.insert(0, visitor[1])
        surname_entry.insert(0, visitor[2])
        id_number_entry.insert(0, visitor[3])
        phone_number_entry.insert(0, visitor[4])


        nok_name_entry.insert(0, nok[0])
        nok_phone_number_entry.insert(0, nok[1])

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def edit_visitor():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":

            selected_id = tree_view.focus()

            visitor = tree_view.item(selected_id, 'values')

            nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
            nok = select_from_table(nok_query)[0]


            name = name_entry.get()
            surname = surname_entry.get()
            id_number = id_number_entry.get()
            phone_number = phone_number_entry.get()
            visitor_id = visitor[0]


            nok_name = nok_name_entry.get()
            nok_phone_number = nok_phone_number_entry.get()


            if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):

                    query = "UPDATE visitor SET name = '" + name + "', surname = '" + surname + "', id_number = '" + id_number + "', phone_number = '" + phone_number + "' WHERE id = " + visitor_id
                    update_table(query)


                    nok_query = "UPDATE next_of_kin SET name = '" + nok_name + "', phone_number = '" + nok_phone_number + "' WHERE visitor_id = " + visitor_id
                    update_table(nok_query)

                    populate_treeview()

                    window.geometry("1100x500")

                else:

                    messagebox.showinfo("User exists", "Please try again.")

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


style = Style()

style.configure("Treeview", highlightthickness=0, bd=0, bg="#fffffff", fieldbackground="#ffffff", fg="#8dc63f", font=('Helvetica', 11))
style.map("Treeview", background=[("selected", "#8dc63f")])



def populate_treeview():

    tree_view.delete(*tree_view.get_children())

    index = 0

    database_list = read_table("visitor")

    for database_item in database_list:

        tree_view.insert(parent="", index=index, iid=index, values=database_item)

        index = index + 1



def delete_row():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":

            selected_id = tree_view.focus()

            visitor = tree_view.item(selected_id, 'values')

            delete_entry("next_of_kin", "visitor_id", visitor[0])

            delete_entry("visitor", "id", visitor[0])

            populate_treeview()


    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def populate_entries():
    try:

        clear_entries()


        selected_id = tree_view.focus()

        visitor = tree_view.item(selected_id, 'values')

        nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
        nok = select_from_table(nok_query)[0]


        name_entry.insert(0, visitor[1])
        surname_entry.insert(0, visitor[2])
        id_number_entry.insert(0, visitor[3])
        phone_number_entry.insert(0, visitor[4])


        nok_name_entry.insert(0, nok[0])
        nok_phone_number_entry.insert(0, nok[1])

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def edit_visitor():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":

            selected_id = tree_view.focus()

            visitor = tree_view.item(selected_id, 'values')

            nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
            nok = select_from_table(nok_query)[0]

            name = name_entry.get()
            surname = surname_entry.get()
            id_number = id_number_entry.get()
            phone_number = phone_number_entry.get()
            visitor_id = visitor[0]


            nok_name = nok_name_entry.get()
            nok_phone_number = nok_phone_number_entry.get()


            if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):

                    query = "UPDATE visitors SET name = '" + name + "', surname = '" + surname + "', id_number = '" + id_number + "', phone_number = '" + phone_number + "' WHERE id = " + visitor_id
                    update_table(query)


                    nok_query = "UPDATE next_of_kin SET name = '" + nok_name + "', phone_number = '" + nok_phone_number + "' WHERE visitor_id = " + visitor_id
                    update_table(nok_query)

                    populate_treeview()

                    window.geometry("1100x500")

                else:

                    messagebox.showinfo("User exists", "Please try again.")

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def show_hidden_entries():

    window.geometry("1100x1000")

    hr_label.place(x=10, y=500)
    edit_label.place(x=400, y=550)
    name_label.place(x=10, y=600)
    name_entry.place(x=10, y=620)
    surname_label.place(x=250, y=600)
    surname_entry.place(x=250, y=620)
    id_number_label.place(x=500, y=600)
    id_number_entry.place(x=500, y=620)

    phone_number_label.place(x=750, y=600)
    phone_number_entry.place(x=750, y=620)
    nok_label.place(x=400, y=700)
    nok_name_label.place(x=10, y=750)
    nok_name_entry.place(x=10, y=780)

    nok_phone_number_label.place(x=250, y=750)
    nok_phone_number_entry.place(x=250, y=780)



def edit_row():
    show_hidden_entries()
    edit_visitor_btn.place(x=10, y=850)
    cancel_btn.place(x=500, y=850)


    populate_entries()


def create_row():

    clear_entries()

    visitor_id = IntVar
    show_hidden_entries()
    create_visitor_btn.place(x=10, y=850)
    cancel_btn.place(x=500, y=850)


def add_visitor():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":

            name = name_entry.get()
            surname = surname_entry.get()
            id_number = id_number_entry.get()
            phone_number = phone_number_entry.get()


            nok_name = nok_name_entry.get()
            nok_phone_number = nok_phone_number_entry.get()


            if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):
                    time_in = datetime.now()

                    insert_visitor(name, surname, id_number, phone_number, 1, time_in)

                    query = "SELECT id FROM visitor WHERE name='" + name + "' AND id_number='" + id_number + "';"

                    db_rows = select_from_table(query)

                    for i in db_rows[0]:
                        visitor_id = i


                    insert_nok(nok_name, nok_phone_number, visitor_id)

                    populate_treeview()

                    clear_entries()


                else:

                    messagebox.showinfo("User exists", "Please try again.")
    except ValueError:
        messagebox.showerror("Validation", "Please check your inputs")


def clear_entries():
    clear_entry(name_entry)
    clear_entry(surname_entry)
    clear_entry(phone_number_entry)
    clear_entry(id_number_entry)
    clear_entry(nok_name_entry)
    clear_entry(nok_phone_number_entry)


def cancel():
    permission = messagebox.askquestion("Cancel operation", "Are you sure you want to continue?")

    if permission == "yes":
        clear_entries()
        window.geometry("1100x500")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=300, y=10)


heading_label = Label(window, text="WELCOME BACK ADMIN", fg="blue", font=("Helvetica", 18))
heading_label.place(x=400, y=30)

tree_view = Treeview(window)

tree_view['columns'] = ('ID', 'Name', 'Surname', "ID Number", "Phone Number", "Logged In", "Time In", "Time Out")

tree_view.column("#0", width=0, stretch=NO)
tree_view.column("ID", anchor=CENTER, width=80)
tree_view.column("Name", anchor=CENTER, width=100)
tree_view.column("Surname", anchor=CENTER, width=100)
tree_view.column("ID Number", anchor=CENTER, width=150)
tree_view.column("Phone Number", anchor=CENTER, width=150)
tree_view.column("Logged In", anchor=CENTER, width=150)
tree_view.column("Time In", anchor=CENTER, width=150)
tree_view.column("Time Out", anchor=CENTER, width=150)

tree_view.heading("#0")
tree_view.heading("ID", text="ID", anchor=CENTER)
tree_view.heading("Name", text="Name", anchor=CENTER)
tree_view.heading("Surname", text="Surname", anchor=CENTER)
tree_view.heading("ID Number", text="ID Number", anchor=CENTER)
tree_view.heading("Phone Number", text="Phone Number", anchor=CENTER)
tree_view.heading("Logged In", text="Logged In", anchor=CENTER)
tree_view.heading("Time In", text="Time In", anchor=CENTER)
tree_view.heading("Time Out", text="Time Out", anchor=CENTER)

populate_treeview()
tree_view.place(x=10, y=120)

create_btn = Button(window, text="CREATE NEW VISITOR", bg="blue", fg="black", borderwidth=0, width=30, command=create_row)
create_btn.place(x=10, y=450)

edit_btn = Button(window, text="EDIT VISITOR", bg="blue", fg="black", borderwidth=0, width=30, command=edit_row)
edit_btn.place(x=380, y=450)

delete_btn = Button(window, text="DELETE VISITOR", bg="blue", fg="black", borderwidth=0, width=30, command=delete_row)
delete_btn.place(x=775, y=450)

hr_label = Label(window, text="____________________________________________________________________________________________________________________________________________________", fg="blue")

edit_label = Label(window, text="EDIT ", fg="blue", font=("Helvetica", 18)).place(x=490, y=550)

name_label = Label(window, text="Please enter name", fg="blue", font="Helvetica").place(x=100, y=600)
name_entry = Entry(window).place(x=100, y=618)

surname_label = Label(window, text="Please enter surname", fg="blue", font="Helvetica").place(x=350, y=600)
surname_entry = Entry(window).place(x=350, y=618)

id_number_label = Label(window, text="Please enter ID Number", fg="blue", font="Helvetica").place(x=600, y=600)
id_number_entry = Entry(window).place(x=600, y=618)

phone_number_label = Label(window, text="Please enter phone number", fg="blue", font="Helvetica").place(x=850, y=600)
phone_number_entry = Entry(window).place(x=850, y=618)

nok_label = Label(window, text="Next of kin details", fg="blue", font=("Helvetica", 18)).place(x=450, y=690)

nok_name_label = Label(window, text="Please enter name", fg="blue", font="Helvetica").place(x=300, y=780)
nok_name_entry = Entry(window).place(x=300, y=800)

nok_phone_number_label = Label(window, text="Please enter phone number", fg="blue", font="Helvetica").place(x=650, y=780)
nok_phone_number_entry = Entry(window).place(x=650, y=800)

edit_visitor_btn = Button(window, text="UPDATE VISITOR", bg="blue", fg="black", borderwidth=0, width=30, command=edit_visitor).place(x=100, y=860)

create_visitor_btn = Button(window, text="ADD NEW VISITOR", bg="blue", fg="black", borderwidth=0, width=30, command=add_visitor).place(x=400, y=860)


cancel_btn = Button(window, text="CANCEL", bg="blue", fg="black", borderwidth=0, width=30, command=cancel).place(x=700, y=860)
window.mainloop()
