import tkinter as tk

from model import Model
from friendframe import FriendFrame

class FriendsList(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.configure()
        self.place(relw=1, relh=1)

        def key1(friend):

            return friend.username

        def key2(friend):

            if friend.online:

                return 0

            return 1

        friends = Model.getFriends()
        friends.sort(key=key1)
        friends.sort(key=key2)

        for friend in friends:

            fF = FriendFrame(self, friend)