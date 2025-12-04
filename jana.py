import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Café GUI")
root.geometry("300x300")

# Title Label
title_label = tk.Label(root, text="Welcome to My Café", font=("Arial", 14))
title_label.pack(pady=10)

# Buttons Functions
def order_coffee():
    messagebox.showinfo("Order", "Coffee Added!")

def order_tea():
    messagebox.showinfo("Order", "Tea Added!")

def show_bill():
    messagebox.showinfo("Bill", "Total: 50 LE")

# Buttons
btn1 = tk.Button(root, text="Order Coffee", width=15, command=order_coffee)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Order Tea", width=15, command=order_tea)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Show Bill", width=15, command=show_bill)
btn3.pack(pady=20)

# Run GUI
root.mainloop()
