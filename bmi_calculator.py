import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
   
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def show_result():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nYou are categorized as: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter your weight in kilograms:").pack(padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.pack(padx=10, pady=10)
root.geometry("400x250")

tk.Label(root, text="Enter your height in meters:").pack(padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.pack(padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=show_result)
calculate_button.pack(padx=10, pady=10)
root.configure(bg="lightblue")
BMI_result = tk.Label( root ,text=f"Your BMI is: {int}", fg="darkblue", bg="lightblue", font=("Helvetica", 12, "bold"))
BMI_result.pack(pady=30)

root.mainloop()
