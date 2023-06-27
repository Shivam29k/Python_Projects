from tkinter import *
from tkinter import messagebox
import pandas
from random import randint, shuffle, choice
import pyperclip
import os
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters= [choice(letters) for _ in range(randint(8,10))]
    pass_symbols= [choice(symbols) for _ in range(randint(2,4))]
    pass_numbers= [choice(numbers) for _ in range(randint(2,4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_input.delete(0,'end')
    pass_input.insert(0,password)
    messagebox.showinfo(title='Copied!', message=f'Password "{password}" copied to clipboard')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_input.get().lower()
    username = mail_input.get()
    password = pass_input.get()

    if username == "" or password=="" or password=="":
        messagebox.showinfo(title="Oops!", message="All feilds required!")
        confirm = False
    else:    
        confirm = messagebox.askokcancel(title=website, message=f"These are the details enterd: \nEmail: {username} \nPassword: {password} \n Is it okay to save?")

    if confirm:
        web_input.delete(0, END)
        pass_input.delete(0,END)
        web_input.focus()

    # using CSV format

        # head = True
        # if os.path.isfile('password_data.csv'):
        #     head = False
        
        # new_data = {
        #     'Website' : [website],
        #     'Username' : [username],
        #     'Password':[password]
        # }

        # df = pandas.DataFrame(new_data)
        # df.to_csv('password_data.csv', mode='a', header=head)

    # Using JSON File format
        new_data = {
            website:{
                "email": username,
                "password": password,
            }
        }
        try:
            with open("data.json","r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating data  
            data.update(new_data) 
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)                  #saving data
            
# ----------------------------- SEARCH -------------------------------- #
def find_password():
    website = web_input.get().lower()
    if website == "":
        messagebox.showerror(title="No Input", message="enter the website first.")
        return
    
    try:
        with open("data.json", "r") as data_file:
            website_data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Oops!", message="No Data Found")
        return
    if website in website_data:
        password = website_data[website]["password"]
        username = website_data[website]["email"]
        messagebox.showinfo(title=f"{website}", message=f"Username/Email : {username}\nPassword : {password}")
    else: 
        messagebox.showinfo(title="Password Finder", message=f"No data of {website}")


            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas = Canvas(width= 180, height=200)
background_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)

# website text
web_txt = Label(text="Website:",justify="center")
web_txt.grid(column=0, row=1, sticky=W)

# website input
web_input = Entry(width=30)
web_input.grid(column=1, row=1, sticky=W)
web_input.focus()

# website button
gen_pass = Button(text="Search", command=find_password,width=15, justify="left", bd=1)
gen_pass.grid(column=2, row=1, sticky=W)

# Email/username text
user_txt = Label(text="Email/Username:", justify="right")
user_txt.grid(column=0, row=2, sticky=W)

# Email/username input
mail_input = Entry(width=49)
mail_input.grid(column=1, row=2, columnspan=2, sticky=W)
mail_input.insert(0, 'example@gmail.com')

# password Text
pass_txt = Label(text="Password:")
pass_txt.grid(column=0, row=3, sticky=W)

# password input
pass_input = Entry(width=30)
pass_input.grid(column=1, row=3, sticky=W)

# password button
gen_pass = Button(text="Generate Password", command=generate_pass, width=15, justify="left", bd=1)
gen_pass.grid(column=2, row=3, sticky=W)

# add button
add = Button(text="Add", command=save_pass, width=42, bd=1)
add.grid(column=1, row=4, columnspan=2, sticky=W)


window.mainloop()