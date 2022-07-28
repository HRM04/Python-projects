from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    from random import randint, choice, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbol = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_symbol + password_numbers + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# with open("Passwords Data", "a") as passwords:
#     passwords.write("Website-||-Email/Username-||-Password\n")
#


def add_password():
    website_name = website_input.get().title()
    email_name = email_input.get()
    password_used = password_input.get()

    new_data = {
        website_name:{
            "email": email_name,
            "password": password_used
        }
    }

    if len(website_name) == 0 or len(password_used) == 0:
        messagebox.showinfo(title="Error", message="You have left some required fields empty."
                                                   " Please go back and fill them")
    else:
        try:
            with open("Passwords_Data.json", "r") as passwords:
                # reading data file
                data = json.load(passwords)
        except FileNotFoundError:
            with open("Passwords_Data.json", "a") as passwords:
                json.dump(new_data, passwords, indent=4)
        else:
            with open("Passwords_Data.json", "w")as passwords:
                # updating data file
                data.update(new_data)
                # writing updated data
                json.dump(data, passwords, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website_name = website_input.get().title()

    try:
        with open("Passwords_Data.json", "r") as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Date File Found")
    else:
        try:
            web = data.get(website_name)
            web_pass = web["password"]

        except TypeError:
            messagebox.showinfo(title="Error", message=f"No details for {website_name} exists")
        else:
            web_email = web["email"]
            messagebox.showinfo(title=website_name, message=f"Email:{web_email}\n"
                                                       f"Password:{web_pass}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="/Users/HP/Downloads/password-manager-start/logo.png")
canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0)

# "website" label
website_label = Label(text="Website:", font=("Calibri", 12))
website_label.grid(column=0, row=1)

# "email/username" label
email_label = Label(text="Email/Username:", font=("Calibri", 12))
email_label.grid(column=0, row=2)

# "password" label
password_label = Label(text="Password:", font=("Calibri", 12))
password_label.grid(column=0, row=3)

# website entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

# email entry
email_input = Entry(width=58)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "onigemohameeda@gmail.com")

# password entry
password_input = Entry(width=35)
password_input.grid(column=1, row=3)

# Search button
search_button = Button(text="Search", font=("Calibri", 12), width=15, command=find_password)
search_button.grid(column=2, row=1)

# password button
password_button = Button(text="Generate Password", font=("Calibri", 12), command=generate_password)
password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", font=("Calibri", 12), width=43, command=add_password)
add_button.grid(column=1, row=4, columnspan=3)





window.mainloop()

