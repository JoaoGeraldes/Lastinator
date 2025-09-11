import json
from tkinter import Label, Entry, Button, BooleanVar, Checkbutton
from logic import copy_last_file


class LastinatorGUI:
    def __init__(self, master, copy_callback):
        self.master = master
        self.copy_callback = copy_callback
        self.master.title("Lastinator")
        self.master.geometry("500x250")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f0f0")
        self.is_sticky_window = BooleanVar(value=False)

        # Labels
        self.label_from = Label(master, text="From (source folder):", bg="#f0f0f0",
                                fg="blue", font=("Arial", 12, "bold"))
        self.label_from.pack(pady=5)

        self.source_entry = Entry(
            master, width=60, bg="white", fg="black", font=("Arial", 10))
        self.source_entry.pack()

        self.label_to = Label(master, text="To (target folder):", bg="#f0f0f0",
                              fg="blue", font=("Arial", 12, "bold"))
        self.label_to.pack(pady=5)

        self.dest_entry = Entry(
            master, width=60, bg="white", fg="black", font=("Arial", 10))
        self.dest_entry.pack()

        # Create the checkbox (alwauys on top)
        self.sticky_checkbox = Checkbutton(
            master,
            text="Make window sticky (always on top)",
            variable=self.is_sticky_window,
            bg="#773e3e",
            fg="black",
            font=("Arial", 10, "bold"),
            command=self.update_sticky  # call a method when toggled
        )
        self.sticky_checkbox.pack(pady=10)

        # Button
        self.button = Button(master, text="Copy Last File", command=copy_last_file,
                             width=20, height=2, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.button.pack(pady=20)

        # Start checking style
        self.check_style_file()

    def update_sticky(self):
        """
        Toggle 'always on top' based on checkbox state.
        """
        self.master.attributes("-topmost", self.is_sticky_window.get())

    def check_style_file(self):
        try:
            with open("style.json") as styles_file:
                style = json.load(styles_file)

            self.label_from.config(fg=style.get(
                "fg", "black"), bg=style.get("bg", "#f0f0f0"))
            self.label_to.config(fg=style.get("fg", "black"),
                                 bg=style.get("bg", "#f0f0f0"))
            self.source_entry.config(bg=style.get(
                "entry_bg", "white"), fg=style.get("entry_fg", "black"))
            self.dest_entry.config(bg=style.get(
                "entry_bg", "white"), fg=style.get("entry_fg", "black"))
            self.button.config(fg=style.get("btn_fg", "white"),
                               bg=style.get("btn_bg", "green"))
            self.master.config(bg=style.get("bg", "#f0f0f0"))

        except Exception as e:
            print("Error loading style.json:", e)

        # Schedule next check in 1 second
        self.master.after(1000, self.check_style_file)
