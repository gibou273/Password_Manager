from tkinter import END, messagebox
import random
import data
import pyperclip
import json


def generate_password(password_entry):
    # Number of letters, numbers and symbols to be picked
    number_of_letters = random.randint(8, 10)
    number_of_numbers = random.randint(2, 4)
    number_of_symbols = random.randint(2, 4)
    # Create a list to store the password
    password_list = []
    # Pick x amount of letters and add them to the list
    for _ in range(0, number_of_letters):
        char = random.choice(data.symbols["alphabets"])
        password_list.append(char)
    # Pick x amount of numbers and add them to the list
    for _ in range(0, number_of_numbers):
        number = random.choice(data.symbols["numbers"])
        password_list.append(number)
    # Pick x amount of symbols and add them to the list
    for _ in range(0, number_of_symbols):
        symbol = random.choice(data.symbols["symbols"])
        password_list.append(symbol)
    # Shuffle the list and convert it into a string
    random.shuffle(password_list)
    real_password = "".join(password_list)
    # Copy the password to the clipboard using the copy method from pyperclip module
    pyperclip.copy(real_password)
    password_entry.insert(0, real_password)


def save_password(website_entry, username_entry, password_entry):
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "website": website,
            "username": username,
            "password": password
        }
    }
    if not website or not username or not password:
        messagebox.showinfo("Oops", "Please fill in all fields" )
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?")
        # Save the information to a text field if user clicks on the OK button
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {username} | {password}\n")
            # Clear the website and password entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        try:
            with open("data.json", "r") as data_file:
                # Read data from the file data.json
                json_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update the data with the new data user inputted
            json_data.update(new_data)
            # Save updated data to the file data.json
            with open("data.json", "w") as myFile:
                json.dump(json_data, myFile, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_info(website_entry):
    search_term = website_entry.get()
    try:
        with open("data.json", "r") as myFile:
            json_data = json.load(myFile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if search_term in json_data:
            username = json_data[search_term]["username"]
            password = json_data[search_term]["password"]
            messagebox.showinfo(title=search_term, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details about {search_term} exists")
    finally:
        pass