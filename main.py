# Initially created by Renzler.
# Build 0.0.1

# Import the tkinter module so the UI can function.
import tkinter as tk
# Import everything from the tkinter module
from tkinter import *
# Import the time module
from time import strftime
from todo import todowindow

mainwindow = tk.Tk()
# DEFINE THE MAIN SCREEN
def main():

    # Determine the width of the screen
    windowwidth = mainwindow.winfo_reqwidth()
    # Determine the height of the screen
    windowheight = mainwindow.winfo_reqheight()
    # Get half the screen width/height and window width/height
    positionright = int(mainwindow.winfo_screenwidth() / 2 - windowwidth / 2)
    positiondown = int(mainwindow.winfo_screenheight() / 2 - windowheight / 2)
    # Position the window in the center of the page.
    mainwindow.geometry("+{}+{}".format(positionright, positiondown))
    # Add title to mainwindow window
    mainwindow.title("Mr. Producto")
    # Define greeting variable as a text label and align it to the top center of the window
    tk.Label(text="Mr. Producto - Main").grid(row=0, column=0, columnspan=2)

def buttons():
    # Create do-do button
    todobutton = Button(
        text="To-Do",
        width=10,
        height=5,
        bg="white",
        fg="black",
        # state=DISABLED,
        # Assign button action function
        command=todowindow
    )
    # Define desired location of button
    todobutton.grid(row=1, column=0, padx=5)
    timetrackerbutton = Button(
        text="Time Tracker",
        width=10,
        height=5,
        bg="white",
        fg="black",
        state=DISABLED,
        # command=opentournamentswindow
    )
    timetrackerbutton.grid(row=1, column=1)
    # Create do-do button
    calendarbutton = Button(
        text="Calendar",
        width=10,
        height=5,
        bg="white",
        fg="black",
        state=DISABLED,
        # Assign button action function
        # command=openadminwindow
    )
    # Define desired location of button
    calendarbutton.grid(row=2, column=0, padx=5, pady=5)
    remindersbutton = Button(
        text="Reminders",
        width=10,
        height=5,
        bg="white",
        fg="black",
        state=DISABLED,
        # command=opentournamentswindow
    )
    remindersbutton.grid(row=2, column=1)

    # Define the time function
def time():
    # Define the string variable as an understandable time format
    string = strftime('%H:%M:%S')
    # Define the label config as a text string
    lbl.config(text=string)
    # Run the time function every 1000 milliseconds, or every 1 second
    lbl.after(1000, time)

# Define the lbl variable as a Label widget, then define the text font, size, bold it, and make it black
lbl = Label(mainwindow, font=('Trebuchet MS', 12),
            fg='black')
# Define desired location of the widget
lbl.grid(row=0, column=2)
# Call the time function
time()


# Call the mainwindow function
main()
buttons()
time()
# ALL STUFF MUST COME BEFORE THIS LINE
mainloop()
