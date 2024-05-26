import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_var.set(password)
def save_password():
    password = password_var.get()
    label = label_entry.get()
    if not password:
        messagebox.showwarning("Warning", "No password generated to save.")
        return
    save_text = f"{label} : {password}" if label else password
    with open("C:\\Users\\athit\\Documents\\passwords.txt", "a") as file:
        file.write(f"\n{save_text}")
    messagebox.showinfo("Success", "Your password has been successfully saved.")
    label_entry.delete(0, tk.END)
root = tk.Tk()
root.title("Password Generator")
tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=5)
password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").pack(pady=5)
password_display = tk.Entry(root, textvariable=password_var, state='readonly')
password_display.pack(pady=5)
tk.Label(root, text="Enter Label (Optional):").pack(pady=5)
label_entry = tk.Entry(root)
label_entry.pack(pady=5)
save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.pack(pady=20)
root.mainloop()
