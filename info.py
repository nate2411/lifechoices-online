from tkinter import END, messagebox
from database_connection import select_from_table


def clear_entry(test_entry):
    test_entry.delete(0, END)



def id_valid(id_number):

    import rsaidnumber

    try:
        id_number = rsaidnumber.parse(id_number)

        return id_number.valid
    except ValueError:
        return False



def not_empty(test_entry):
    try:

        if test_entry == "":
            raise ValueError()

        else:
            return True
    except ValueError:
        return False


def exit_program(window):
    exit = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')

    if exit == 'yes':
        window.destroy()

def user_exists(name, id_number):

    query = "SELECT * FROM visitor WHERE name='" + name + "' AND id_number='" + id_number + "';"

    database_rows = select_from_table(query)

    if len(database_rows) > 0:
        return True
    else:
        return False



def admin_exists(name, id_number):

    query = "SELECT * FROM visitor WHERE name = '" + name + "' AND id_number = '" + id_number + "' AND is_admin = 'true';"

    database_rows = select_from_table(query)

    if len(database_rows) > 0:
        return True
    else:
        return False


def validate_min_entries(name, id_number):
    try:

        if not_empty(name) and not_empty(id_number):

            if len(id_number) == 13:

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



def validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
    try:

        if not_empty(name) and not_empty(surname) and not_empty(id_number) and not_empty(phone_number) and not_empty(
                nok_name) and not_empty(nok_phone_number):

            if len(id_number) == 13 and len(phone_number) == 10 and len(nok_phone_number) == 10:

                if id_valid(id_number):
                    return True
                else:
                    messagebox.showerror("INPUT Error", "Your ID Number is invalid")
                    return False
            else:
                messagebox.showerror("INPUT Error", "Please check ID Number or phone numbers")
                return False
        else:
            messagebox.showerror("INPUT Error", "Inputs cannot be empty")
    except ValueError:
        messagebox.showerror("INPUT Error", "Please check your inputs")
    except TypeError:
        messagebox.showerror("INPUT Error", "Please check your ID Number")
