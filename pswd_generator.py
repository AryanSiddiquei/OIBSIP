import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    
    if length < 4:  # Ensure the length is enough to include all character types
        raise ValueError("Password length should be at least 4 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

def show_password():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        result_window = tk.Toplevel(root)
        result_window.title("Generated Password")
        result_window.geometry("300x150")
        result_window.configure(bg="lightblue")
        password_label = tk.Label(result_window, text=f"Your password is: {password}", fg="darkblue", bg="lightblue", font=("Helvetica", 12, "bold"))
        password_label.pack(pady=30)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length for the password:").pack(padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.pack(padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=show_password)
generate_button.pack(pady=20)

root.mainloop()
