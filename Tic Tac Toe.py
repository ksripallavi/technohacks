import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.configure(bg="lightblue")
        self.board = [' ' for _ in range(9)]  # Initialize the board
        self.current_player = 'X'  # 'X' starts the game
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col), bg="lightblue")
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                self.buttons.append(button)

        self.restart_button = tk.Button(self.master, text="Restart", font=('Arial', 16), command=self.restart_game, bg="lightblue")
        self.restart_button.grid(row=3, columnspan=3, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Congratulations!", f"Player {self.current_player} wins!")
                self.restart_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Tie!", "The game is a tie!")
                self.restart_game()
            else:
                self.switch_player()
                if self.current_player == 'O':
                    self.computer_move()

    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i * 3 + j] == player for j in range(3)) or \
                    all(self.board[j * 3 + i] == player for j in range(3)):
                return True
        if all(self.board[i * 3 + i] == player for i in range(3)) or \
                all(self.board[i * 3 + 2 - i] == player for i in range(3)):
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ' ']
        index = random.choice(available_moves)
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)
        if self.check_winner(self.current_player):
            messagebox.showinfo("Congratulations!", "Computer wins!")
            self.restart_game()
        elif ' ' not in self.board:
            messagebox.showinfo("Tie!", "The game is a tie!")
            self.restart_game()
        else:
            self.switch_player()

    def restart_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='')
        self.restart_button.grid_forget()


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
