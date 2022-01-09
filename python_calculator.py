# Imports
import tkinter as tk

root = tk.Tk()

# Common Variables
btn_height = 4
btn_width = 4
font = "Georgia"
font_size = 20

# Title
root.title('Python Calculator')

# Basic Design Dimensions
root.geometry('350x560')
root.resizable(height=False, width=False)  # Delete line to make app dimensions resizable

# Colors
# Background Color
root.configure(background="white")

calc_input = tk.Text(root, height=1, width=26, font=(font, font_size))
calc_input.grid(columnspan=4)

result = ""


def calc():
    calc_result = eval(retrieve_user_input())
    calc_input.delete(1.0, tk.END)
    calc_result = format(calc_result, '.2f')  # Limit result to 2 decimal places
    calc_input.insert(1.0, str(calc_result))


def retrieve_user_input():
    input_result = calc_input.get(1.0, tk.END)
    return input_result


def user_input(number):
    calc_input.insert(tk.END, str(number))


def clear():
    calc_input.delete(1.0, tk.END)


def calc_btn(calc_root, btn_text, btn_command, height, width, btn_font, btn_font_size, btn_row, btn_column):
    calc_btn_template = tk.Button(calc_root,
                                  text=btn_text,
                                  command=btn_command,
                                  height=height,
                                  width=width,
                                  font=(btn_font, btn_font_size))
    calc_btn_template.grid(row=btn_row, column=btn_column)
    return calc_btn_template


# BUTTONS
# ROW 1
btn_clear = calc_btn(root, "C", lambda: clear(), btn_height, btn_width, font, font_size, 1, 0)
# Exponent btn
btn_exponent = calc_btn(root, "e", lambda: user_input("**"), btn_height, btn_width, font, font_size, 1, 1)
# Pi btn
btn_pi = calc_btn(root, "pi", lambda: user_input(3.14), btn_height, btn_width, font, font_size, 1, 2)
# Percentage btn
btn_percentage = calc_btn(root, "%", lambda: user_input("%"), btn_height, btn_width, font, font_size, 1, 3)

#  Row 2
# 7 btn
btn_7 = calc_btn(root, "7", lambda: user_input(7), btn_height, btn_width, font, font_size, 2, 0)
# 8 btn
btn_8 = calc_btn(root, "8", lambda: user_input(8), btn_height, btn_width, font, font_size, 2, 1)
# 9 btn
btn_9 = calc_btn(root, "9", lambda: user_input(9), btn_height, btn_width, font, font_size, 2, 2)
# Division btn
btn_division = calc_btn(root, "/", lambda: user_input("/"), btn_height, btn_width, font, font_size, 2, 3)

# ROW 3
# 4 btn
btn_4 = calc_btn(root, "4", lambda: user_input(4), btn_height, btn_width, font, font_size, 3, 0)
# 5 btn
btn_5 = calc_btn(root, "5", lambda: user_input(5), btn_height, btn_width, font, font_size, 3, 1)
# 6 btn
btn_6 = calc_btn(root, "6", lambda: user_input(6), btn_height, btn_width, font, font_size, 3, 2)
# Division btn
btn_multiplication = calc_btn(root, "X", lambda: user_input("*"), btn_height, btn_width, font, font_size, 3, 3)

# ROW 4
# 1 btn
btn_1 = calc_btn(root, "1", lambda: user_input(1), btn_height, btn_width, font, font_size, 4, 0)
# 2 btn
btn_2 = calc_btn(root, "2", lambda: user_input(2), btn_height, btn_width, font, font_size, 4, 1)
# 3 btn
btn_3 = calc_btn(root, "3", lambda: user_input(3), btn_height, btn_width, font, font_size, 4, 2)
# Subtraction btn
btn_subtraction = calc_btn(root, "-", lambda: user_input("-"), btn_height, btn_width, font, font_size, 4, 3)

# ROW 5
# 0 btn
btn_0 = calc_btn(root, "0", lambda: user_input("0"), btn_height, btn_width, font, font_size, 5, 0)
# Decimal btn
btn_decimal = calc_btn(root, ".", lambda: user_input("."), btn_height, btn_width, font, font_size, 5, 1)
# Equate btn
btn_equate = calc_btn(root, "=", lambda: calc(), btn_height, btn_width, font, font_size, 5, 2)
# Addition btn
btn_addition = calc_btn(root, "+", lambda: user_input("+"), btn_height, btn_width, font, font_size, 5, 3)

# Run main loop
root.mainloop()
