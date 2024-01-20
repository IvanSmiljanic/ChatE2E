import tkinter as tk
from tkinter import ttk

from friendslist import FriendsList

class SideBar(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(width=400)

        self.grid(row=1, column=0, sticky="nsew")

        self.friendsList = FriendsList(self)

        separator = ttk.Separator(orient="vertical")
        # separator.pack(in_=self, fill=tk.Y, expand=True, side=tk.RIGHT, float=True)
        separator.place(in_=self, y=0, relx=1, width=2, relh=1)
