import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to create a new file
def create_file():
    file_name = simpledialog.askstring("Create File", "Enter file name:")
    if file_name:
        try:
            with open(file_name, 'x') as f:
                messagebox.showinfo("Success", f"File '{file_name}' created successfully.")
        except FileExistsError:
            messagebox.showwarning("Exists", f"File '{file_name}' already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to view all files
def view_files():
    files = os.listdir()
    if not files:
        messagebox.showinfo("Files", "No files found.")
    else:
        file_list = "\n".join(files)
        messagebox.showinfo("Files in Directory", file_list)

# Function to delete a file
def delete_file():
    file_name = simpledialog.askstring("Delete File", "Enter file name to delete:")
    if file_name:
        try:
            os.remove(file_name)
            messagebox.showinfo("Deleted", f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Not Found", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to read a file
def read_file():
    file_name = simpledialog.askstring("Read File", "Enter file name to read:")
    if file_name:
        try:
            with open(file_name, 'r') as f:
                content = f.read()
                messagebox.showinfo(f"Content of '{file_name}'", content)
        except FileNotFoundError:
            messagebox.showwarning("Not Found", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to append to a file
def edit_file():
    file_name = simpledialog.askstring("Edit File", "Enter file name to edit:")
    if file_name:
        try:
            with open(file_name, 'a') as f:
                data = simpledialog.askstring("Edit File", "Enter content to add:")
                if data:
                    f.write(data + '\n')
                    messagebox.showinfo("Success", "Content added successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Not Found", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Setup GUI
root = tk.Tk()
root.title("File Manager")
root.geometry("300x300")

tk.Button(root, text="Create File", command=create_file).pack(pady=5)
tk.Button(root, text="View All Files", command=view_files).pack(pady=5)
tk.Button(root, text="Delete File", command=delete_file).pack(pady=5)
tk.Button(root, text="Read File", command=read_file).pack(pady=5)
tk.Button(root, text="Edit File", command=edit_file).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()
