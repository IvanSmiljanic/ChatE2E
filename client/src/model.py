import datetime as dt

from friend import Friend
from message import Message

class Model:

    username = None
    friends = None

    @staticmethod
    def getFriends():

        return Model.friends

    @staticmethod
    def setUsername(username):

        Model.username = username

    @staticmethod
    def friendsFromList(list):

        Model.friends = []

        for friend in list:

            Model.friends.append(Friend(friend, True))

    @staticmethod
    def addMessage(sender, recipient, message, timeSent):

        if sender == Model.username:
            otherName = recipient
        else:
            otherName = sender
            sender = otherName

        for friend in Model.friends:

            if friend.username == otherName:
                timeSent = dt.datetime.strptime(timeSent, "%Y-%m-%d %H:%M:%S.%f")

                friend.chatHistory.append(Message(sender, message, timeSent))

    @staticmethod
    def messagesFromList(list):

        for message in list:

            Model.addMessage(message["sender"], message["recipient"], message["message"], message["timeSent"])

        def key(message):

            return message.timeSent

        for friend in Model.friends:

            friend.chatHistory.sort(key=key)