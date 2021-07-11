from tkinter import *
from database_connection import read_table
from info import *


window = Tk()
window.title("Life Choices Online")
window.geometry("490x340")



# Function will check content and data types
def sign_user_in():
    try:

        name = name_entry.get()
        id_number = id_number_entry.get()


        if validate_min_entries(name, id_number):

            if user_exists(name, id_number):

                visitor = select_from_table("SELECT * FROM visitor WHERE name='" + name + "' AND id_number='" + id_number + "';")[0]
                ("UPDATE visitor SET logged_in = 'true' WHERE id = " + str(visitor[0]))
                messagebox.showinfo("Login successful", "You have successfully logged in")

                window.destroy()
                import logged_in

            else:

                register = messagebox.askquestion('User not found', "Would you like to register an account")


                if register == "yes":

                    window.destroy()
                    import sign_up
                else:

                    pass
        else:
            messagebox.showerror("Validation error", "Entries are not valid, please check your inputs")
    except ValueError:
        messagebox.showerror("Validation error", "Please check your entries")

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)



heading_label = Label(window, text="SIGN IN", fg="blue", font=("Helvetica", 18))
heading_label.place(x=190, y=20)

name_label = Label(window, text="Please enter name!", fg="blue", font="Helvetica")
name_label.place(x=160, y=70)
name_entry = Entry(window)
name_entry.place(x=160, y=100)

id_number_label = Label(window, text="Please enter ID Number!", fg="blue", font="Helvetica")
id_number_label.place(x=160, y=150)
id_number_entry = Entry(window)
id_number_entry.place(x=160, y=180)

sign_in_btn = Button(window, text="SIGN IN", width=50, bg="blue", fg="black", borderwidth=0, command=sign_user_in)
sign_in_btn.place(x=50, y=230)
window.mainloop()
