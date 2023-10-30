from scrapper import startScraping, get_emails

import tkinter as tk
import webbrowser
from time import sleep
import threading

def authenticated(email, password):
    print(email, password)
    # check if email and password are valid
    return True

# def startScraping(term):
#     # start scrapping with niche and area
#     print(term)
#     for i in range(20):
#         sleep(0.1)
#         print(i)

# def get_emails(deepdive):
#     # get emails with deepdive option
#     print(deepdive)
#     for i in range(20):
#         sleep(0.1)
#         print(i)

def login():

    # get email and password from input fields
    email = email_entry.get()
    password = password_entry.get()

    # check if email and password are valid
    if authenticated(email, password):
        # show main page
        login_window.destroy()
        main_page()


def main_page():
    # create a new window for the main page
    main_window = tk.Tk()
    main_window.title('Business Scrapper')
    main_window.geometry('300x150')

    # create input fields for niche and area
    niche_label = tk.Label(main_window, text='Niche:')
    niche_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
    niche_entry = tk.Entry(main_window, width=30)
    niche_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    area_label = tk.Label(main_window, text='Area:')
    area_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
    area_entry = tk.Entry(main_window, width=30)
    area_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    # create a submit button
    def submit():

        niche = niche_entry.get()
        area = area_entry.get()
        term= f'{niche} near {area}'

        main_window.destroy()
        wait_screen(term)


    submit_button = tk.Button(main_window, text='Submit', command=submit, width=10)
    submit_button.grid(row=2, column=1, padx=10, pady=10)

    # increase distance between lines
    for i in range(8):
        main_window.grid_rowconfigure(i, minsize=20)

    # start the main event loop
    main_window.mainloop()

def wait_screen(term):
    # create a new window for the wait screen
    wait_window = tk.Tk()
    wait_window.title('Scarapping')
    wait_window.geometry('300x100')

    # create a label for the wait screen
    wait_label = tk.Label(wait_window, text='Please wait while we are scrapping...')
    wait_label.pack(padx=10, pady=10)

    threading.Thread(target=startScraping, args=(term,), daemon=True).start()

    while threading.active_count()>1:
        wait_window.update()
        sleep(0.1)

    wait_window.destroy()
    Extract_mail_Screen()


def Extract_mail_Screen():
    main_window = tk.Tk()
    main_window.title('Mail Extractor')
    main_window.geometry('300x200')

    # show scrapping status
    status_label = tk.Label(main_window, text='Scrapping completed', width=15)
    status_label.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
    # show scrapping status
    text_label = tk.Label(main_window, text='Do you want to get the emails ?')
    text_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)

    # create a selection field for deepdive
    deepdive_label = tk.Label(main_window, text='Deepdive:', width=10)
    deepdive_label.grid(row=3, column=0, padx=10, pady=10)

    deepdive_var = tk.StringVar(value='off')
    deepdive_options = ['off', 'auto', 'on']
    deepdive_menu = tk.OptionMenu(main_window, deepdive_var, *deepdive_options)
    deepdive_menu.grid(row=3, column=1, padx=10, pady=10)

    # create a button to get emails
    def get_emails_button():
        deepdive = deepdive_var.get()
        main_window.destroy()
        Extract_mail_wait_Screen(deepdive)

    get_emails_button = tk.Button(main_window, text='Get Emails', command=get_emails_button)
    get_emails_button.grid(row=3, column=2, padx=10, pady=10)

    # increase distance between lines
    for i in range(7):
        main_window.grid_rowconfigure(i, minsize=10)


def Extract_mail_wait_Screen(deepdive):
    wait_window = tk.Tk()
    wait_window.title('Extracting Emails')
    wait_window.geometry('300x100')

    # create a label for the wait screen
    wait_label = tk.Label(wait_window, text='Please wait while we are trying to scrape email...')
    wait_label.pack(padx=10, pady=10)

    threading.Thread(target=get_emails, args=(deepdive,), daemon=True).start()

    while threading.active_count()>1:
        wait_window.update()
        sleep(0.1)

    wait_window.destroy()
    final_screen()

def final_screen():
    # create a new window for the final screen
    final_window = tk.Tk()
    final_window.title('Done')
    final_window.geometry('250x100')

    # create a label for the final screen
    final_label = tk.Label(final_window, text='Scraping complete!')
    final_label.pack(padx=10, pady=10)

    # schedule the window to be destroyed after 3 seconds
    final_window.after(30000, final_window.destroy)

    # start the main event loop for the final screen
    final_window.mainloop()


# create a login window
login_window = tk.Tk()
login_window.title('Login')
login_window.geometry('350x150')

# create input fields for email and password
email_label = tk.Label(login_window, text='Email:', width=10)
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(login_window, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(login_window, text='Password:', width=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_window, show='*', width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# create a login button
login_button = tk.Button(login_window, text='Login', command=login)
login_button.grid(row=2, column=1, padx=10, pady=10)

def create_account():
    # open example.com in a web browser
    webbrowser.open('https://example.com')
# create a create account button
create_account_button = tk.Button(login_window, text='Create Account', command=create_account)
create_account_button.grid(row=2, column=0, padx=10, pady=10)

# start the login event loop
login_window.mainloop()