from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------------PASSWORD GENERATOR---------------------------------------------------
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


r_letters = [random.choice(letters) for char in range(nr_letters)]

r_symbols = [random.choice(symbols) for char in range(nr_symbols)]

r_numbers = [random.choice(numbers) for char in range(nr_numbers)]

password_list = r_letters + r_symbols + r_numbers
random.shuffle(password_list)

password = "".join(password_list)


def generate_password():
    password_input.insert(0, password)
    pyperclip.copy(password)


# ----------------------SAVING PASSWORD-------------------------------------------------------------------
def save():
    web_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()
    new_data = {
        web_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Empty Space", message="Please dont leave any fields empty!")

    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
                #  Updating old data with new data
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')


def find_password():
    web_data = website_input.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title='error', message='No data file found')
    else:
        if web_data in data:
            e = data[web_data]['email']
            p = data[web_data]['password']
            messagebox.showinfo(title=web_data, message=f"Email; {e}\nPassword: {p}")

# -------------------------------------UI SETUP-------------------------------------------------
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)

website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.insert(0, "praiseohuegbe@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="w")  # Align the button to the west side of the cell

add_button = Button(text='Add', width=29, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2, sticky='e')

canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1)

window.mainloop()

#

