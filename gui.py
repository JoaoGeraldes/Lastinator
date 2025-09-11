import json
from tkinter import Label, Entry, Button, BooleanVar, Checkbutton, Frame
from logic import copy_last_file


class LastinatorGUI:
    def __init__(self, master, copy_callback):
        self.master = master
        self.copy_callback = copy_callback
        self.master.title("Lastinator")
        self.master.geometry("500x250")
        self.master.resizable(False, False)
        self.master.configure(bg="#212121")
        self.container = Frame(master)
        self.container.pack(expand=True)  # expand fills the available space
        self.is_sticky_window = BooleanVar(value=False)

        # UI COMPONENTS
        self.label_from = Label(self.container, text="From (source folder):", bg="#f0f0f0",
                                fg="blue", font=("Arial", 12, "bold"))
        self.label_to = Label(self.container, text="To (target folder):", bg="#f0f0f0",
                              fg="blue", font=("Arial", 12, "bold"))
        self.input_from = Entry(self.container, bg="white",
                                fg="black", font=("Arial", 14))
        self.input_to = Entry(self.container, bg="white",
                              fg="black", font=("Arial", 14))
        self.button = Button(
            self.container,
            text="Copy Last File",
            command=lambda: copy_last_file(
                self.input_from.get(), self.input_to.get()),
            width=20,
            height=2,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.sticky_checkbox = Checkbutton(
            self.container,
            text="Make window sticky (always on top)",
            variable=self.is_sticky_window,
            # bg="#773e3e",
            # fg="black",
            font=("Arial", 10, "bold"),
            command=self.update_sticky  # call a method when toggled
        )

        # UI COMPONENTS POSITIONING
        # Row 0
        self.label_from.grid(row=0, column=0, padx=5, pady=2)
        self.label_to.grid(row=0, column=1, padx=5, pady=2)
        # Row 1
        self.input_from.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.input_to.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        # Row 2
        self.button.grid(row=2, column=0, columnspan=2, pady=15)
        # Row 3
        self.sticky_checkbox.grid(row=3, column=0, columnspan=2, pady=10)

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
            self.input_from.config(bg=style.get(
                "entry_bg", "white"), fg=style.get("entry_fg", "black"))
            self.input_to.config(bg=style.get(
                "entry_bg", "white"), fg=style.get("entry_fg", "black"))
            self.button.config(fg=style.get("btn_fg", "white"),
                               bg=style.get("btn_bg", "green"))
            self.master.config(bg=style.get("bg", "#f0f0f0"))

        except Exception as e:
            print("Error loading style.json:", e)

        # Schedule next check in 1 second
        self.master.after(1000, self.check_style_file)
