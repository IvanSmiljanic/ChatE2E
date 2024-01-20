import tkinter as tk
from tkinter import ttk

from control import Control

class Content(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.configure()

        self.grid(row=1, column=1, sticky="nsew")

        self.messageFrame = None
        self.entryFrame = None

        self.message = tk.StringVar(self)

        self.setChatParent(None)

    def setChatParent(self, chatParent):

        self.chatParent = chatParent

        self.updateChatHistory()

    def chatHistoryUpdated(self, user):

        if user == self.chatParent.username:

            self.addMessage(self.chatParent.chatHistory[-1])

    def addMessage(self, message):

        messageLabel = tk.Label(self.messageFrame, text=f"{message.user}: {message.content}", anchor=tk.W)
        messageLabel.pack(fill=tk.X)

    def updateChatHistory(self):

        if self.chatParent == None:

            pass

        else:

            if self.messageFrame:

                self.messageFrame.destroy()

            if self.entryFrame:

                self.entryFrame.destroy()

            self.messageFrame = tk.Frame(self)
            self.messageFrame.pack(fill=tk.BOTH, expand=True)

            separator = ttk.Separator(self.messageFrame, orient=tk.HORIZONTAL)
            separator.pack(side="bottom", fill="x")

            self.entryFrame = tk.Frame(self, height=100)
            self.entryFrame.pack(fill=tk.X)

            self.messageEntry = tk.Entry(self.entryFrame, textvariable=self.message)
            self.messageEntry.place(anchor=tk.W, relw=.9, height=80, x=10,  rely=.5)

            def sendMessage():

                Control.sendMessage(self.chatParent.username, self.message.get())
                self.message.set("")

            self.sendButton = tk.Button(self.entryFrame, text="Send", command=sendMessage)
            self.sendButton.place(anchor=tk.E, relw=.08, height=60, relx=.994, rely=.5)

            y = 0

            for message in self.chatParent.chatHistory:

                self.addMessage(message)