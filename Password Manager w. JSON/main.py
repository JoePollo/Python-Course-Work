from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas
import os.path
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    password = ""
    password_letters = [choice(letters) for char in range(randint(1,8))]
    password_numbers = [choice(numbers) for char in range(randint(1, 25 - len(password_letters)))]
    password_symbols = [choice(symbols) for char in range(25 - (len(password_letters) + len(password_numbers)))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if os.path.exists("Passwords.json") == True:
        website_json = pandas.read_json("Passwords.json", orient = "split")
        website_list = website_json["Website"].tolist()
        password_list = website_json["Password"].tolist()
        site = website_entry.get()
        password = password_entry.get()
        if website_entry.get() == "" or password_entry.get() == "":
            messagebox.showerror(title = "Oops!", message = "Fields were left blank!")
        elif site in str(website_list):
            messagebox.showerror(title = "Oops!", message = "This website has been already entered!")
        elif password in password_list:
            messagebox.showerror(title = "Oops!", message = "That password is already being used!")
        else:
            append_df = pandas.DataFrame.from_dict(
                {
                    "Website": [site],
                    "Email": [email_entry.get()],
                    "Password": [password],
                }
            )
            website_json = website_json.append(append_df)
            json_from_df = json.loads(website_json.to_json(orient = "split"))
            del json_from_df["index"]
            with open("Passwords.json", "w") as file:
                json.dump(json_from_df, file, indent = 1)
            messagebox.showinfo(title = "Confirmation", message = "Website login added!")
    else:
        website_df = pandas.DataFrame.from_dict({"Website": [website_entry.get()],
                                                 "Email": [email_entry.get()],
                                                 "Password": [password_entry.get()],
                                                 })
        website_json = json.loads(website_df.to_json(orient = "split"))
        del website_json["index"]
        with open("Passwords.json", "w") as file:
            json.dump(website_json, file, indent = 4)
        messagebox.showinfo(title = "Confirmation", message = "Website login added!")
# ---------------------------- GET PASSWORD ------------------------------- #
def get_password():
    if os.path.exists("Passwords.json") == True:
        website_df = pandas.read_json("Passwords.json", orient = "split")
        if website_entry.get() in website_df["Website"].tolist():
            password = website_df.loc[website_df["Website"] == website_entry.get()]["Password"].to_string(index = False)
            password_entry.delete(0, END)
            password_entry.insert(0, str(password))
            pyperclip.copy(password)
        else:
            messagebox.showerror(title = "Oops!", message = "That website does not yet have a password!")
    else:
        messagebox.showerror(title = "Oops!", message = "No passwords have been saved yet!")

# ---------------------------- UI SETUP ------------------------------- #
mainapp = Tk()
mainapp.config(height = 200, width = 200, padx = 20, pady = 20)
mainapp.title("Password Manager")

lock_canvas = Canvas(height = 200, width = 200)
lock_img = PhotoImage(file = "logo.png")
lock_canvas.create_image(100, 100, image = lock_img)
lock_canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:")
website_label.grid(row = 2, column = 0)

website_entry = Entry(width = 55)
website_entry.grid(row = 2, column = 1, columnspan = 2)
website_entry.focus()

email_label = Label(text = "Email/Username:")
email_label.grid(row = 3, column = 0)

email_entry = Entry(width = 55)
email_entry.insert(0, "coolemail@megadomain.com")
email_entry.grid(row = 3, column = 1, columnspan = 2)

password_label = Label(text = "Password:")
password_label.grid(row = 4, column = 0)

password_entry = Entry(width = 37)
password_entry.grid(row = 4, column = 1)

password_generator_button = Button(text = "Generate Password", command = generate_password)
password_generator_button.grid(row = 4, column = 2)

add_button = Button(text = "Add", width = 37, command = save_password)
add_button.grid(row = 5, column = 1, columnspan = 1)

get_password_button = Button(text = "Get Password", width = 17, command = get_password)
get_password_button.grid(row = 5, column = 2)

mainapp.mainloop()