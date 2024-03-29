import socket
import tkinter as tk
from tkinter import ttk
import socket as s
import json
import datetime as dt
import os

from friendframe import FriendFrame
from model import Model

class Control:

    app = None

    host = "127.0.0.1"
    port = 2402
    clientSocket = None

    @staticmethod
    def establishConnection():

        Control.clientSocket = s.socket(socket.AF_INET, socket.SOCK_STREAM)
        Control.clientSocket.connect((Control.host, Control.port))

        if os.path.isfile("logintoken.txt"):

            username = None
            seriesID = None
            token = None

            with open("logintoken.txt", "r") as f:

                username = f.readline()[:-1]
                seriesID = int(f.readline()[:-1])
                token = int(f.readline())

            Control.send(json.dumps({"type": 3, "username": username, "seriesID": seriesID, "token": token}))

        while True:

            head = Control.clientSocket.recv(2)

            payload = Control.clientSocket.recv(int.from_bytes(head, 'little', signed=False))

            result = json.loads(payload.decode('utf-8'))

            print(result)

            if result["type"] == 2:

                Model.setUsername(result["username"])
                Model.friendsFromList(result["friends"])
                Model.messagesFromList(result["messages"])

                if "seriesID" in result:

                    with open("logintoken.txt", "w") as f:

                        f.write(Model.username + "\n" + str(result["seriesID"]) + "\n" + str(result["token"]))

                Control.app.loadPage("Home")

            elif result["type"] == 5:

                Model.addMessage(result["sender"], result["recipient"], result["message"], result["timeSent"])

                if result["sender"] == Model.username:
                    otherName = result["recipient"]
                else:
                    otherName = result["sender"]

                Control.app.currentPage.content.chatHistoryUpdated(otherName)

    @staticmethod
    def send(payload):

        message = len(payload).to_bytes(2, 'little', signed=False) + payload.encode('utf-8')
        Control.clientSocket.sendall(message)

    @staticmethod
    def loginWithPassword(username, password, rememberMe):

        message = json.dumps({"type": 2, "username": username, "password": password, "rememberMe": rememberMe})

        Control.send(message)

    @staticmethod
    def sendMessage(recipient, message):

        message = json.dumps({"type": 5,
                                  "sender": Model.username,
                                  "recipient": recipient,
                                  "message": message,
                                  "timeSent": dt.datetime.now()},
                                  default=str)

        Control.send(message)

    @staticmethod
    def leftMouseDown(event):

        target = event.widget

        while target != None:

            tType = type(target)

            if tType == FriendFrame:

                Control.app.currentPage.content.setChatParent(target.getFriend())

            target = target.master