#Just a random bloxflip Predictor made with Tkinter.
#Made by drakola001 on discord
#https://discord.gg/QVApSTJWP6



import tkinter as tk
from tkinter import ttk
from time import sleep
import random

used_round_ids = []

def predict():
    round_id = round_id_entry.get()
    num_mines = mines_entry.get()
    robux_amount = robux_entry.get()

    if not num_mines:
        result_text.set("Please enter a number for mines.")
        return

    try:
        num_mines = int(num_mines)
    except ValueError:
        result_text.set("Invalid number for mines.")
        return

    if num_mines < 1 or num_mines > 24:
        result_text.set("Please enter a number between 1 and 24 for mines.")
        return

    if len(round_id) != 36:
        result_text.set("Invalid round ID.")
        return

    if round_id in used_round_ids:
        result_text.set("Round ID already used.")
        return

    if not robux_amount:
        result_text.set("Please enter a number for Robux amount.")
        return

    try:
        robux_amount = int(robux_amount)
    except ValueError:
        result_text.set("Invalid number for Robux amount.")
        return

    result_text.set("Predicting...")
    window.update()

    sleep(3)

    grid = [["💣" for _ in range(5)] for _ in range(5)]

    safe_spots = random.sample(range(25), 25 - num_mines)
    for spot in safe_spots:
        row = spot // 5
        col = spot % 5
        grid[row][col] = "✅"

    result_text.set("Prediction:\n\n")
    result_text.set(result_text.get() + "\n".join([" ".join(row) for row in grid]))
    result_text.set(result_text.get() + f"\n\nRobux Amount: {robux_amount}")

    used_round_ids.append(round_id)

def validate_round_id(input):
    return len(input) <= 36

def validate_mines(input):
    return input.isdigit() and len(input) == 1

def validate_robux_amount(input):
    return input.isdigit()

def clear_round_id():
    round_id_var.set("")

def clear_mines():
    mines_var.set("")

def clear_robux_amount():
    robux_var.set("")

window = tk.Tk()
window.title("Bloxflip Random Predictor By Drakola001")
window.geometry("400x400")

content_frame = ttk.Frame(window)
content_frame.pack(expand=True, padx=20, pady=20)

round_id_label = ttk.Label(content_frame, text="Round ID:")
round_id_label.grid(row=0, column=0, sticky="w")

round_id_var = tk.StringVar()
round_id_entry = ttk.Entry(content_frame, textvariable=round_id_var, validate="key")
round_id_entry['validatecommand'] = (round_id_entry.register(validate_round_id), '%P')
round_id_entry.grid(row=0, column=1, pady=5, padx=10)

round_id_clear_button = ttk.Button(content_frame, text="Clear", command=clear_round_id)
round_id_clear_button.grid(row=0, column=2, padx=5)

mines_label = ttk.Label(content_frame, text="Number of Mines:")
mines_label.grid(row=1, column=0, sticky="w")

mines_var = tk.StringVar()
mines_entry = ttk.Entry(content_frame, textvariable=mines_var, validate="key")
mines_entry['validatecommand'] = (mines_entry.register(validate_mines), '%P')
mines_entry.grid(row=1, column=1, pady=5, padx=10)

mines_clear_button = ttk.Button(content_frame, text="Clear", command=clear_mines)
mines_clear_button.grid(row=1, column=2, padx=5)

robux_label = ttk.Label(content_frame, text="Robux Amount:")
robux_label.grid(row=2, column=0, sticky="w")

robux_var = tk.StringVar()
robux_entry = ttk.Entry(content_frame, textvariable=robux_var, validate="key")
robux_entry['validatecommand'] = (robux_entry.register(validate_robux_amount), '%P')
robux_entry.grid(row=2, column=1, pady=5, padx=10)

robux_clear_button = ttk.Button(content_frame, text="Clear", command=clear_robux_amount)
robux_clear_button.grid(row=2, column=2, padx=5)


predict_button = ttk.Button(content_frame, text="Predict", command=predict)
predict_button.grid(row=3, columnspan=3, pady=10)


result_text = tk.StringVar()
result_label = ttk.Label(content_frame, textvariable=result_text, font=("Courier", 14), justify="left")
result_label.grid(row=4, columnspan=3, pady=10)


window.mainloop()
