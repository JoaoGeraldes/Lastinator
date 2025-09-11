# Lastinator Logic
import os
import shutil
import datetime
from tkinter import messagebox

# Copy file from path A to path B with timestamped filename


def copy_last_file(source_dir, dest_dir):
    if not source_dir or not dest_dir:
        messagebox.showwarning(
            "Missing input", "Please enter both source and destination folders.")
        return

    if not os.path.isdir(source_dir):
        messagebox.showerror(
            "Error", f"Source folder does not exist: {source_dir}")
        return

    if not os.path.isdir(dest_dir):
        messagebox.showerror(
            "Error", f"Destination folder does not exist: {dest_dir}")
        return

    try:
        files = [f for f in os.listdir(source_dir) if os.path.isfile(
            os.path.join(source_dir, f))]
        if not files:
            messagebox.showwarning(
                "No files", "No files found in source folder.")
            return

        # Get last modified file
        files.sort(key=lambda f: os.path.getmtime(os.path.join(source_dir, f)))
        last_file = files[-1]
        src_path = os.path.join(source_dir, last_file)

        # Timestamped filename
        ext = os.path.splitext(last_file)[1]
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        new_name = f"{timestamp}{ext}"
        dest_path = os.path.join(dest_dir, new_name)

        shutil.copy2(src_path, dest_path)
        messagebox.showinfo(
            "Success", f"Copied {last_file} to {dest_dir} as {new_name}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Make the window sticky (always on top)


def make_sticky(self):
    """
    Keeps the window always on top of other windows.
    """
    self.master.attributes("-topmost", True)
