import tkinter as tk

from topbar import TopBar
from sidebar import SideBar
from content import Content

class HomePage(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.topBar = TopBar(self)
        self.sideBar = SideBar(self)
        self.content = Content(self)