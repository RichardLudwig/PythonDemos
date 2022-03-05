# Imports
from tkinter import *

# Setup
root = Tk()
root.title("Cookie Clicker")
root.resizable(False, False)

# Starting score
point = 0

# Clicker function, increases score by 1 point
def clicker():
    global point
    point += 1
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

# Create cookie with canvas, assign clicker function to cookie, run function if cookie clicked
cookie = canvas.create_oval(50,50,350,350, fill="brown")
canvas.tag_bind(cookie, "<Button-1>", lambda e: clicker())

# Reset cookie clicker score if button clicked
reset_button = Button(root, text="Reset Score", command=reset)
reset_button.pack()

root.mainloop()
