import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Global data file
DATA_FILE = "library_data.csv"

# Create initial dataframe if not exists
try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Book_ID", "Title", "Author", "Category", "Issued"])
    df.to_csv(DATA_FILE, index=False)

# ---------- Functions ----------
def save_data():
    df.to_csv(DATA_FILE, index=False)

def add_book():
    global df
    bid = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()
    category = entry_category.get()

    if not (bid and title and author and category):
        messagebox.showerror("Error", "All fields are required!")
        return

    if bid in df["Book_ID"].values:
        messagebox.showerror("Error", "Book ID already exists!")
        return

    new_row = {"Book_ID": bid, "Title": title, "Author": author, "Category": category, "Issued": "No"}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data()
    messagebox.showinfo("Success", "Book added successfully!")
    clear_entries()

def view_books():
    global df
    for row in tree.get_children():
        tree.delete(row)
    for i, row in df.iterrows():
        tree.insert("", "end", values=list(row))

def issue_book():
    global df
    bid = entry_id.get()
    if bid not in df["Book_ID"].values:
        messagebox.showerror("Error", "Book ID not found!")
        return

    df.loc[df["Book_ID"] == bid, "Issued"] = "Yes"
    save_data()
    messagebox.showinfo("Issued", "Book issued successfully!")
    clear_entries()

def return_book():
    global df
    bid = entry_id.get()
    if bid not in df["Book_ID"].values:
        messagebox.showerror("Error", "Book ID not found!")
        return

    df.loc[df["Book_ID"] == bid, "Issued"] = "No"
    save_data()
    messagebox.showinfo("Returned", "Book returned successfully!")
    clear_entries()

def show_stats():
    global df
    if df.empty:
        messagebox.showinfo("No Data", "No books available for analysis.")
        return

    category_counts = df["Category"].value_counts()
    plt.figure(figsize=(6,4))
    plt.bar(category_counts.index, category_counts.values, color="skyblue")
    plt.title("Books per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    issued = (df["Issued"] == "Yes").sum()
    total = len(df)
    issue_ratio = np.round((issued / total) * 100, 2) if total > 0 else 0
    messagebox.showinfo("Stats", f"Total Books: {total}\nIssued Books: {issued}\nIssue %: {issue_ratio}%")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_category.delete(0, tk.END)

# ---------- GUI ----------
root = tk.Tk()
root.title("📚 Library Management System")
root.geometry("750x550")

# Labels and entries
tk.Label(root, text="Book ID").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Title").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Author").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Category").grid(row=3, column=0, padx=10, pady=5)

entry_id = tk.Entry(root)
entry_title = tk.Entry(root)
entry_author = tk.Entry(root)
entry_category = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_title.grid(row=1, column=1)
entry_author.grid(row=2, column=1)
entry_category.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Book", command=add_book, bg="lightgreen").grid(row=0, column=2, padx=10)
tk.Button(root, text="View All", command=view_books, bg="lightblue").grid(row=1, column=2, padx=10)
tk.Button(root, text="Issue Book", command=issue_book, bg="orange").grid(row=2, column=2, padx=10)
tk.Button(root, text="Return Book", command=return_book, bg="yellow").grid(row=3, column=2, padx=10)
tk.Button(root, text="Show Stats", command=show_stats, bg="pink").grid(row=4, column=1, pady=10)

# Treeview (table)
columns = ("Book_ID", "Title", "Author", "Category", "Issued")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

view_books()

root.mainloop()
