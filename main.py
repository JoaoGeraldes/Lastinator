import os
import shutil
from tkinter import Tk, Button, Entry, Label, messagebox


def copy_last_file():
    source_dir = source_entry.get()
    dest_dir = dest_entry.get()

    if not source_dir or not dest_dir:
        messagebox.showwarning(
            "Missing input", "Please enter both source and destination folders.")
        return

    try:
        # Get list of files in source
        files = [f for f in os.listdir(source_dir) if os.path.isfile(
            os.path.join(source_dir, f))]
        if not files:
            messagebox.showwarning(
                "No files", "No files found in source folder.")
            return

        # Sort by modification time, get the last one
        files.sort(key=lambda f: os.path.getmtime(os.path.join(source_dir, f)))
        last_file = files[-1]

        src_path = os.path.join(source_dir, last_file)
        dest_path = os.path.join(dest_dir, last_file)

        # Copy the file
        shutil.copy2(src_path, dest_path)

        messagebox.showinfo("Success", f"Copied {last_file} to {dest_dir}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = Tk()
root.title("File Copier")
root.geometry("400x200")

# Labels + Inputs
Label(root, text="From (source folder):").pack(pady=5)
source_entry = Entry(root, width=50)
source_entry.pack()

Label(root, text="To (target folder):").pack(pady=5)
dest_entry = Entry(root, width=50)
dest_entry.pack()

# Button
btn = Button(root, text="Copy Last File",
             command=copy_last_file, width=20, height=2)
btn.pack(pady=20)

# Run the window loop
root.mainloop()
