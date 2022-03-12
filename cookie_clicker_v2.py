# Imports
from tkinter import *

# Setup
root = Tk()
root.title("Cookie Clicker v2")
root.resizable(False, False)

# Starting score
point = 0

# Add one point function
def addOne():
    canvas.tag_bind(cookie, "<Button-1>", lambda e: addOne())
    global point
    point += 1
    score.configure(text="Score = " + str(point))

# Add five points function
def addFive():
    canvas.tag_bind(cookie, "<Button-1>", lambda e: addFive())
    global point
    point += 5
    score.configure(text="Score = " + str(point))

# Reset function, resets score to 0 points
def reset():
    global point
    point = 0
    score.configure(text="Score = " + str(point))

# Initial label for score
score = Label(root, text="Score = 0")
score.pack()

# Setup canvas size
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# Add one point to cookie clicker score if button clicked
addOne_button = Button(root, text="Add One", command=addOne, width=15, height=2)
addOne_button.pack(side=LEFT)

# Add five points to cookie clicker score if button clicked
addFive_button = Button(root, text="Add Five", command=addFive, width=15, height=2)
addFive_button.pack(side=LEFT)

# Create cookie with canvas
cookie = canvas.create_oval(50,50,350,350, fill="brown")

# Reset cookie clicker score if button clicked
reset_button = Button(root, text="Reset Score", command=reset, width=15, height=2)
reset_button.pack(side=LEFT)

root.mainloop()
