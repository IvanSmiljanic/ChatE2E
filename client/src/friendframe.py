import tkinter as tk
from tkinter import ttk

class FriendFrame(tk.Frame):

    def __init__(self, master, friend):

        super().__init__(master)

        self.friend = friend

        self.configure(height=100)

        self.pack(fill=tk.X, expand=False)

        uSNLabel = tk.Label(self, text=friend.username, font=("Arial", 12))
        uSNLabel.place(anchor=tk.W, x=80, rely=.5)

        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self, x=0, rely=1, height=2, relw=1)

    def getFriend(self):

        return self.friend

    def getUsername(self):

        return self.friend.username