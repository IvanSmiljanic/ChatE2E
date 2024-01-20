import tkinter as tk
import threading as th

from login import LoginPage
from home import HomePage
from control import Control

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        Control.app = self
        self.currentPage = None

        self.geometry("1920x1080")

        self.pages = {"Login": LoginPage, "Home": HomePage}

        self.loadPage("Login")

        self.bind("<1>", Control.leftMouseDown)

        th.Thread(target=Control.establishConnection).start()

        self.mainloop()

    def loadPage(self, page):

        if self.currentPage:

            self.currentPage.destroy()

        self.currentPage = self.pages[page](self)
        self.currentPage.pack(fill=tk.BOTH, expand=True)