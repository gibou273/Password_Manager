from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Password Generator App")
window.config(padx=50, pady=50)


heading_text = Label(text="Password Generator", font=("Ariel", 30, "bold"))
heading_text.grid(row=0, column=1)
# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
search_button = Button(text="Search", fg="white", bg="green")
search_button.grid(row=1, column=4)
# Email
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "john.doe@mymail.com")
#Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)
# Generate password button
generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)
# Add Button
add_button = Button(text="Add", width=33, fg="white", bg="blue")
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

