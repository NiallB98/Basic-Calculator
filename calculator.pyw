import tkinter as tk
import ctypes, sys

# Preventing blurry GUI on Windows
if 'win' in sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Tracking first number and last used operator
global f_num, lastOp
f_num = 0
lastOp = "none"

# Creating window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.configure(bg='#343A40')

# Creating text box at top
e = tk.Entry(root, width=35, borderwidth=2, bg="#BCC2C8")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function for applying operators
def applyOp(current):
    global f_num, lastOp
    
    # Saving what is currently in the text box
    first_number = e.get()
    
    # Catching a ValueError (ie. if text box is empty)
    try:
        # Applying previous operator if there is one
        if lastOp == "+": f_num = f_num + float(first_number)
        elif lastOp == "-": f_num = f_num - float(first_number)
        elif lastOp == "*": f_num = f_num * float(first_number)
        elif lastOp == "/":
            if float(first_number) > 0:
                f_num = f_num / float(first_number)
            else: f_num = 0
        else: f_num = float(first_number)
        
        # Clearing text box and updating lastOp
        e.delete(0, tk.END)
        lastOp = current
    except ValueError:
        # Clearing text box; resetting lastOp and f_num on a ValueError
        e.delete(0, tk.END)
        lastOp = "none"
        f_num = 0

# Entering numbers by clicking buttons
def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

# Clear button function
def button_c():
    global f_num, lastOp
    
    e.delete(0, tk.END)
    if lastOp == "c": f_num = 0
    lastOp = "c"

# Equals button function
def button_e():
    global f_num, lastOp
    
    # Catching a ValueError
    try:
        second_number = e.get()
        
        # Applying previous operator if there is one
        if lastOp == "+": f_num = f_num + float(second_number)
        elif lastOp == "-": f_num = f_num - float(second_number)
        elif lastOp == "*": f_num = f_num * float(second_number)
        elif lastOp == "/":
            if float(second_number) > 0:
                f_num = f_num / float(second_number)
            else: f_num = 0
        else: f_num = float(second_number)
        
        # Clearing text box, showing final result in the text box and resetting lastOp
        e.delete(0, tk.END)
        e.insert(0, f_num)
        lastOp = "none"
    
    except ValueError:
        # Clearing text box, showing final result in the text box; resetting lastOp and f_num on a ValueError
        e.delete(0, tk.END)
        e.insert(0, f_num)
        lastOp = "none"
        f_num = 0

# Defining buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#212529", fg="white")# 1
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#212529", fg="white")# 2
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#212529", fg="white")# 3
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#212529", fg="white")# 4
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#212529", fg="white")# 5
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#212529", fg="white")# 6
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#212529", fg="white")# 7
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#212529", fg="white")# 8
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#212529", fg="white")# 9
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#212529", fg="white")# 0

button_plus = tk.Button(root, text="+", padx=39, pady=20, command=lambda: applyOp("+"), bg="#212529", fg="white")# +
button_minus = tk.Button(root, text="-", padx=40, pady=20, command=lambda: applyOp("-"), bg="#212529", fg="white")# -
button_multiply = tk.Button(root, text="x", padx=40, pady=20, command=lambda: applyOp("*"), bg="#212529", fg="white")# *
button_divide = tk.Button(root, text="\'/.", padx=37, pady=20, command=lambda: applyOp("/"), bg="#212529", fg="white")# /
button_clear = tk.Button(root, text="C", padx=130, pady=20, command=button_c, bg="#E06D06", fg="white")# Clear
button_equals = tk.Button(root, text="=", padx=39, pady=20, command=button_e, bg="#E06D06", fg="white")# =

# Putting buttons on screen
button_1.grid(row=4, column=0)# 1
button_2.grid(row=4, column=1)# 2
button_3.grid(row=4, column=2)# 3

button_4.grid(row=3, column=0)# 4
button_5.grid(row=3, column=1)# 5
button_6.grid(row=3, column=2)# 6

button_7.grid(row=2, column=0)# 7
button_8.grid(row=2, column=1)# 8
button_9.grid(row=2, column=2)# 9

button_plus.grid(row=5, column=0)# +
button_0.grid(row=5, column=1)# 0
button_multiply.grid(row=5, column=2)# *

button_minus.grid(row=6, column=0)# -
button_equals.grid(row=6, column=1)# =
button_divide.grid(row=6, column=2)# /

button_clear.grid(row=1,column=0, columnspan=3)# Clear

# Bringing window to front and starting the loop
root.lift()
root.mainloop()
