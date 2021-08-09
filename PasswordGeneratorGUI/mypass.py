from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_input.delete(0, END)

    password_list = []

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ["!", "#", "$", "%", "&",
               "(", ")", "*", "+", "@", "-", "=", "/", "^"]

    # My new Password Generator Logic

    # password_input.delete(0, END)
    # password = []

    # for n in range(random.randint(4, 8)):
    #     password.append(random.choice(letters))
    #     password.append(random.choice(numbers))
    #     password.append(random.choice(symbols))

    # random.shuffle(password)

    # password = ""
    # for char in password_list:
    #     password += char

    # It cuts down all the above code

    # password_text = "".join(password)

    # password_input.insert(0, password_text)

    # Password Generator Project

    password_list = [random.choice(letters)
                     for n in range(random.randint(8, 10))]

    password_list = password_list + \
        [random.choice(numbers) for n in range(random.randint(3, 5))]

    password_list = password_list + \
        [random.choice(symbols) for n in range(random.randint(3, 5))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- Search Functionality------------------------------- #

def search():
    website = website_input.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        # This code is using try except block.. But it should be ommitted where the program can be checked with a simple if and else statement.

        # try:
        #     pass_word = data[website]["password"]
        #     e_mail = data[website]['email']

        # except KeyError:
        #     messagebox.showinfo(title="Oops", message=f"The data for the website {website} doesn't exist!!")

        # else:
        #     password_input.delete(0, END)
        #     password_input.insert(0, pass_word)
        #     pyperclip.copy(pass_word)
        #     messagebox.showinfo(title=f"Login Credentials for {website}", message=f"Your email is : {e_mail}\nYour password is : {pass_word}")

        if website in data:
            pass_word = data[website]["password"]
            e_mail = data[website]['email']

            password_input.delete(0, END)
            password_input.insert(0, pass_word)

            pyperclip.copy(pass_word)

            messagebox.showinfo(
                title=f"Login Credentials for {website}", message=f"Your email is : {e_mail}\nYour password is : {pass_word}")

        else:
            messagebox.showinfo(title="Oops", message=f"The data for the website {website} doesn't exist!!")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def create_data():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Oops", message=f"Please do not leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}")

        if is_ok:

            # My way of doing it

            # try:
            #     with open("data.json", "r") as data_file:
            #         data = json.load(data_file)
            #         data.update(new_data)
            #     with open("data.json", "w") as data_file:
            #         json.dump(data, data_file, indent=5)

            # except FileNotFoundError:
            #     with open("data.json", "w") as data_file:
            #         json.dump(new_data, data_file, indent=5)

            # Angela's way of doing it

            try:
                with open("data.json", "r") as data_file:
                    # Reading the old data
                    data = json.load(data_file)
            except FileNotFoundError:
                # Writing the first data into the data file
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=5)
            else:
                # Updating the old data with a new one

                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=5)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website name
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)


website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()


# Search Functionality

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)


# Email Name

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "sugamtele111@gmail.com")

# Password

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)


# Generate Password Button

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)


# Add Button
add_button = Button(text="Add", width=44, command=create_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
