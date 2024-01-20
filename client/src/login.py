import tkinter as tk

from control import Control

class LoginPage(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.username = tk.StringVar(self)
        self.password = tk.StringVar(self)
        self.rememberMe = tk.IntVar(self)

        loginFrame = tk.Frame(self)
        loginFrame.place(anchor=tk.N, relx=.5, rely=.15, width=500, relh=.8)

        label = tk.Label(loginFrame, text="ChatE2E", font=("Arial", 25))
        label.place(anchor=tk.N, relx=.5)

        uSNFrame = tk.Frame(loginFrame)
        uSNFrame.place(anchor=tk.N, relw=1, relh=.2, relx=.5, y=200)

        pWDFrame = tk.Frame(loginFrame)
        pWDFrame.place(anchor=tk.N, relw=1, relh=.2, relx=.5, y=340)

        self.uSNLabel = tk.Label(uSNFrame, text="Username:")
        self.uSNLabel.place(x=0, y=0)

        self.uSNEntry = tk.Entry(uSNFrame, textvariable=self.username)
        self.uSNEntry.place(x=0, y=50, relw=1)

        self.pWDLabel = tk.Label(pWDFrame, text="Password:")
        self.pWDLabel.place(x=0, y=0)

        self.pWDEntry = tk.Entry(pWDFrame, textvariable=self.password)
        self.pWDEntry.place(x=0, y=50, relw=1)

        self.rememberMeButton = tk.Checkbutton(loginFrame, justify=tk.CENTER, text="Remember Me", var=self.rememberMe)
        self.rememberMeButton.place(anchor=tk.N, relx=.5, y=500)

        self.loginButton = tk.Button(loginFrame, text="Log In", command=(lambda: Control.loginWithPassword(self.username.get(), self.password.get(), self.rememberMe.get())))
        self.loginButton.place(anchor=tk.N, relx=.5, y=600)