# Imports
from tkinter import *
from PIL import Image, ImageTk

# Setup
root = Tk()
root.title("Cookie Clicker v3")
root.resizable(False, False)

# Variables
button_width = 15
button_height = 2

# Starting score
point = 0

# Add one point function
def add_one():
    canvas.tag_bind(cookie_button, "<Button-1>", lambda e: add_one())
    global point
    point += 1
    score.configure(text="Score = " + str(point))

# Add five points function
def add_five():
    canvas.tag_bind(cookie_button, "<Button-1>", lambda e: add_five())
    global point
    point += 5
    score.configure(text="Score = " + str(point))

# Reset function, resets score to 0 points
def reset():
    global point
    point = 0
    score.configure(text="Score = " + str(point))

# Initial label for score
score = Label(root, text="Score = " + str(point))
score.pack()

# Setup canvas size
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# Add one point to cookie clicker score if button clicked
add_one_button = Button(root, text="Add One Point", command=add_one, width=button_width, height=button_height)
add_one_button.pack(side=LEFT)

# Add five points to cookie clicker score if button clicked
add_five_button = Button(root, text="Add Five Points", command=add_five, width=button_width, height=button_height)
add_five_button.pack(side=LEFT)

# Create cookie with imported image and canvas
img = Image.open("cookie.png") # Add a "cookie.png" to your project folder to make your code workable
img = img.resize((200, 200), Image.ANTIALIAS)
cookie_image = ImageTk.PhotoImage(img)
cookie_button = canvas.create_image(200, 200, anchor=CENTER, image=cookie_image, state=NORMAL)

# Default add 1 point to score per cookie click, can change by clicking add_five_button in GUI
canvas.tag_bind(cookie_button, "<Button-1>", lambda e: add_one())

# Reset cookie clicker score if button clicked
reset_button = Button(root, text="Reset Score", command=reset, width=button_width, height=button_height)
reset_button.pack(side=LEFT)

root.mainloop()
