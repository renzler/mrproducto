# Initially created by Renzler.
# Build 0.0.1

# Import the tkinter module so the UI can function.
import tkinter as tk
# Import everything from the tkinter module
from tkinter import *
# Import the time module
from time import strftime


def todowindow():
    # New Member window
    to_do_window = Toplevel()
    # Determine the width of the screen
    windowWidth = to_do_window.winfo_reqwidth()
    # Determine the height of the screen
    windowHeight = to_do_window.winfo_reqheight()
    # Get half the screen width/height and window width/height
    positionRight = int(to_do_window.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(to_do_window.winfo_screenheight() / 2 - windowHeight / 2)
    # Position the window in the center of the page.
    to_do_window.geometry("+{}+{}".format(positionRight, positionDown))
    # New Member window title
    to_do_window.title("Mr. Producto")
    # A Label widget to show in toplevel
    tk.Label(to_do_window,
          text="Mr. Producto - To-Do").grid(row=0, column=0, columnspan=2)


    def labels():
        # Define firstname label and properties
        tasknamelabel = Label(to_do_window,
                               text='Name', fg='black', width=8, font=["Trebuchet MS", 10]).grid(row=2, sticky=E)
        typelabel = tk.Label(to_do_window,
                                 text="Type", fg="black", width=8, font=("Trebuchet MS", 10)).grid(row=3, sticky=E)
        # Define gamertaglabel label and properties
        gamertaglabel = tk.Label(to_do_window,
                                 text="Gamertag", fg="black", width=8, font=("Trebuchet MS", 10)).grid(row=4, sticky=E)
        # Define emaillabel label and properties
        emaillabel = tk.Label(to_do_window,
                              text="Email Address", fg="black", width=12, font=("Trebuchet MS", 10)).grid(
                                row=5,sticky=E, padx=13)
        # Define emaillabel label and properties
        # password1label = tk.Label(to_do_window,
        #                           text="Password", fg="black", width=12, font=("Trebuchet MS", 10)).grid(row=5, sticky=E)
        # password2label = tk.Label(to_do_window,
        #                           text="Confirm Password", fg="black", width=16, font=("Trebuchet MS", 10)).grid(row=6,
        #                                                                                                          sticky=E,
        #                                                                                                          padx=11)
        # missingfeatures = tk.Label(to_do_window,
        #                            text="Missing Features:\nSubmission Result Messages", fg="black", width=32,
        #                            font=("Trebuchet MS", 10)).grid(row=5, sticky=W, columnspan=2)
        # requirements = tk.Label(to_do_window,
        #                         text='Requirements:\nGamertags:\nMust be unique and be between 3 and 24 '
        #                              'alphanumeric characters\nCannot contain symbols\nEmail addresses:\nMust '
        #                              'be unique, Must be a valid format\nPasswords must be at least 15 '
        #                              'characters\nPasswords must contain at least one of the following:\nUppercase '
        #                              'letter, Lowercase letter, Number\nA symbol, but not a semicolon or an exclamation '
        #                              'point',
        #                         fg="black", width=54, font=("Trebuchet MS", 10)).grid(row=6, column=0,
        #                                                                               sticky=W, columnspan=2)
        global validatefaillabel
        validatefaillabel = tk.Label(to_do_window,
                                     text="Invalid Entry; Not Submitted", fg="black", font=("Trebuchet MS", 10))
        global validatepasslabel
        validatepasslabel = tk.Label(to_do_window,
                                     text="Entry Submission Attempted", fg="black", font=("Trebuchet MS", 10))
        global validateonlylabel
        validateonlylabel = tk.Label(to_do_window,
                                     text="Valid Entry; Ready for Submission", fg="black", font=("Trebuchet MS", 10))


    def entries():
        # Define firstnameentry as a global variable
        global firstnameentry
        # Define firstnameentry as text input field
        firstnameentry = tk.Entry(to_do_window,
                                  fg="black", bg="white", width=32)
        # Define firstnameentry location
        firstnameentry.grid(row=1, column=1, sticky=W)
        # Define typeentry as a global variable
        global typeentry
        # Define typeentry as text input field
        typeentry = tk.Entry(to_do_window,
                                 fg="black", bg="white", width=32)
        typeentry.grid(row=2, column=1, sticky=W)
        # Define gamertagentry as a global variable
        global gamertagentry
        # Define gamertagentry as text input field
        gamertagentry = tk.Entry(to_do_window,
                                 fg="black", bg="white", width=32)
        # Define gamertagentry location
        gamertagentry.grid(row=3, column=1, sticky=W)
        # Define emaillabel label and properties
        # emaillabel = tk.Label(to_do_window,
        #                       text="Email Address", fg="black", width=12, font=("Trebuchet MS", 10)).grid(row=4, sticky=E,
        #                                                                                                   padx=13)
        # Define emailentry as a global variable
        # global emailentry
        # Define emailentry as text input field
        global emailentry
        emailentry = tk.Entry(to_do_window,
                              fg="black", bg="white", width=32)
        # Define emailentry location
        emailentry.grid(row=4, column=1, sticky=W)

        # # Define password1entry as a global variable
        # global password1entry
        # # Define password1entry as text input field
        # password1entry = tk.Entry(to_do_window,
        #                           fg="black", bg="white", show="*", width=32)
        # # Define password1entry location
        # password1entry.grid(row=5, column=1, sticky=W)
        #
        # # Define password2entry as a global variable
        # # global password2entry
        # # Define password2entry as text input field
        # password2entry = tk.Entry(to_do_window,
        #                           fg="black", bg="white", show="*", width=32)
        # # Define password2entry location
        # password2entry.grid(row=6, column=1, sticky=W)
        # # Define function for New Member Submit button

    # global validateentry
    # validateentry = 0
    def buttons():
        # Create do-do button
        newitembutton = Button(to_do_window,
                               text="New Item",
                               width=10,
                               height=5,
                               bg="white",
                               fg="black",
                               # state=DISABLED,
                               # Assign button action function
                               command=todowindow
                               )
        # Define desired location of button
        newitembutton.grid(row=1, column=0, pady=1, padx=5)

        # Create do-do button
        listitemsbutton = Button(to_do_window,
                               text="List Items",
                               width=10,
                               height=5,
                               bg="white",
                               fg="black",
                               # state=DISABLED,
                               # Assign button action function
                               # command=todowindow
                               )
        # Define desired location of button
        listitemsbutton.grid(row=1, column=1, pady=1)

    buttons()
    #entries()
    labels()
