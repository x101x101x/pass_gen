import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_gui(event=None):
    """Generate password and display in GUI."""
    password_length = length_entry.get()
    if not password_length.isdigit() or int(password_length) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
        return

    password_length = int(password_length)
    generated_password = generate_password(password_length)
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, generated_password)
    password_display.config(state=tk.DISABLED)


# Create main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='pink')  # Set background color to pink

# Calculate window position to center it
window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set window size and position
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Create widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

password_display = tk.Text(root, height=5, width=30, wrap=tk.WORD, state=tk.DISABLED)
password_display.pack(pady=10)

# Bind Enter key to generate_password_gui function
root.bind('<Return>', generate_password_gui)

# Start the main tkinter event loop
root.mainloop()
