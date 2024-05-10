import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
window = tk.Tk()
window.title("Classic Calculator")
window.config(bg="light blue")

# Entry for displaying input and output
entry = tk.Entry(window, width=30, borderwidth=5, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons and place them in the grid
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 12), command=lambda button_text=button_text: button_click(button_text), bg="light blue")
    button.grid(row=row, column=column)
    if button_text in ["0", ".", "=", "/"]:
        button.config(bg="lightgray")
    else:
        button.config(bg="white")

# Clear button
clear_button = tk.Button(window, text="Clear", padx=65, pady=20, font=("Arial", 12), command=button_clear, bg="light gray")
clear_button.grid(row=5, column=0, columnspan=2)

# Equal button
equal_button = tk.Button(window, text="=", padx=65, pady=20, font=("Arial", 12), command=button_equal, bg="light gray")
equal_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
