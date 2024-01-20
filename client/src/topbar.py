import tkinter as tk
from tkinter import ttk

class TopBar(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(height=100)

        self.grid(row=0, column=0, columnspan=2, sticky="we")

        self.grid_columnconfigure(0, weight=1)

        titleLabel = tk.Label(self, text="ChatE2E", font=("Arial", 25))
        # titleLabel.place(x=0, y=0)
        titleLabel.grid(row=0, column=0, sticky="ns")

        separator = ttk.Separator(orient="horizontal")
        separator.grid(in_=self, row=1, column=0, sticky="ew")
        # separator.grid(row=1, column=0)