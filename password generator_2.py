
import tkinter as tk
from tkinter import messagebox
import random
import string


# ------------------------------------------
# Generate Password
# ------------------------------------------

def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Invalid Length",
                "Password length must be at least 4."
            )
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )


# ------------------------------------------
# Save Password
# ------------------------------------------

def save_password():

    password = password_entry.get()

    if not password:
        messagebox.showerror(
            "No Password",
            "Generate a password first."
        )
        return

    try:
        with open("generated_passwords.txt", "a") as file:

            file.write("-" * 40 + "\n")
            file.write("PASSWORD GENERATOR\n")
            file.write("-" * 40 + "\n")
            file.write(f"Password: {password}\n")
            file.write("-" * 40 + "\n")

        messagebox.showinfo(
            "Saved",
            "Password saved successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Save Error",
            f"Failed to save password:\n{error}"
        )


# ------------------------------------------
# View Saved Passwords
# ------------------------------------------

def view_saved_passwords():

    try:

        with open("generated_passwords.txt", "r") as file:
            data = file.read().strip()

        if not data:
            data = "No passwords saved yet."

    except FileNotFoundError:

        data = "No passwords saved yet."

    password_window = tk.Toplevel(root)

    password_window.title("Saved Passwords")
    password_window.geometry("600x400")

    text_box = tk.Text(
        password_window,
        width=70,
        height=25,
        font=("Arial", 11)
    )

    text_box.pack(
        padx=10,
        pady=10
    )

    text_box.insert(
        tk.END,
        data
    )

    text_box.config(
        state="disabled"
    )


# ------------------------------------------
# Clear
# ------------------------------------------

def clear_fields():

    length_entry.delete(
        0,
        tk.END
    )

    password_entry.delete(
        0,
        tk.END
    )


# ------------------------------------------
# Main Window
# ------------------------------------------

root = tk.Tk()

root.title("Password Generator")

root.geometry("600x500")

root.resizable(
    False,
    False
)


# ------------------------------------------
# Title
# ------------------------------------------

tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 22, "bold")
).pack(
    pady=25
)


# ------------------------------------------
# Password Length
# ------------------------------------------

length_frame = tk.Frame(root)

length_frame.pack(
    pady=10
)


tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 13)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


length_entry = tk.Entry(
    length_frame,
    width=15,
    font=("Arial", 13)
)

length_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


# ------------------------------------------
# Generate Button
# ------------------------------------------

tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password,
    width=22
).pack(
    pady=15
)


# ------------------------------------------
# Password Display
# ------------------------------------------

password_frame = tk.LabelFrame(
    root,
    text="Generated Password",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)

password_frame.pack(
    pady=15
)


password_entry = tk.Entry(
    password_frame,
    width=40,
    font=("Arial", 13)
)

password_entry.pack(
    padx=10,
    pady=10
)


# ------------------------------------------
# Buttons
# ------------------------------------------

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)


tk.Button(
    button_frame,
    text="Save Password",
    font=("Arial", 12, "bold"),
    command=save_password,
    width=16
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    command=clear_fields,
    width=10
).grid(
    row=0,
    column=1,
    padx=5
)


# ------------------------------------------
# View Saved Passwords
# ------------------------------------------

tk.Button(
    root,
    text="View Saved Passwords",
    font=("Arial", 12, "bold"),
    command=view_saved_passwords,
    width=22
).pack(
    pady=10
)


# ------------------------------------------
# Start GUI
# ------------------------------------------

root.mainloop()

