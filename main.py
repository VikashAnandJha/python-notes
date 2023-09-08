import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import os
import uuid

# Create an empty list to store user data from CSV
user_data = []

# Create random image paths for testing


def generate_random_image_path():
    return f"{uuid.uuid4()}.jpg"

# Function to update the Treeview with new data


def update_treeview():
    # Clear the existing data in the Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Clear the old user data
    user_data.clear()
    image_references.clear()

    # Read user data from CSV file
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user_data.append(row)

    # Load and store images and insert user data
    for user in user_data:
        name = user["name"]
        age = user.get("age", "")
        image_path = user["image_path"]

        # Load and resize the image
        img = Image.open(image_path)
        img = img.resize((50, 50))
        img = ImageTk.PhotoImage(img)

        # Store the reference to the PhotoImage object
        image_references[generate_random_image_path()] = img

        # Insert a new row with image, name, and age
        treeview.insert(parent="", index=tk.END, text="",
                        image=img, values=(name, age))

    # Update the display
    treeview.update_idletasks()

    # Schedule the next auto-refresh after a certain interval (e.g., 5000 milliseconds or 5 seconds)
    root.after(2000, update_treeview)


# Dictionary to store references to PhotoImage objects
image_references = {}

root = tk.Tk()
column_names = ("Name", "Age")
treeview = ttk.Treeview(root, columns=column_names)
treeview.heading("#0", text="Image")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")

# Customize the Treeview style to set row height (adjust the 'padding' value as needed)
style = ttk.Style()
# Set the row height (e.g., 60 pixels)
style.configure("Treeview", rowheight=60)

# Create and configure vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=vsb.set)

# Pack the Treeview and Scrollbar
treeview.pack(fill=tk.BOTH, expand=True)
vsb.pack(side="right", fill="y")

# Initial data load and auto-refresh
update_treeview()

root.mainloop()
