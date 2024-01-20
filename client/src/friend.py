from message import Message

class Friend:

    def __init__(self, username, online):

        self.username = username
        self.online = online
        self.chatHistory = []