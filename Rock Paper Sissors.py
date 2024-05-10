import tkinter as tk
from tkinter import messagebox
import random

def play():
    player_choice = player_var.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="blue", font=("Arial", 20, "bold"))
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win!", fg="green", font=("Arial", 20, "bold"))
    else:
        result_label.config(text="Computer wins!", fg="red", font=("Arial", 20, "bold"))
    messagebox.showinfo("Result", "You chose: " + player_choice + "\nComputer chose: " + computer_choice)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="lightblue")

# Create and pack widgets with larger font size and padding
tk.Label(root, text="Select your choice:", bg="lightblue", font=("Arial", 24)).pack(pady=10)
player_var = tk.StringVar()
options = ["Rock", "Paper", "Scissors"]
for option in options:
    tk.Radiobutton(root, text=option, variable=player_var, value=option, bg="lightblue", font=("Arial", 20)).pack(anchor=tk.W, padx=20)
play_button = tk.Button(root, text="Play", command=play, bg="lightgreen", font=("Arial", 20))
play_button.pack(pady=10)
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 24))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
