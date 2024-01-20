import socket
import threading as th
import json
import db
import crypto as c
import auth
import datetime as dt

HOST = "127.0.0.1"
PORT = 2402

users = {}

def send(conn, payload):

    message = len(payload).to_bytes(2, 'little', signed=False) + payload.encode('utf-8')
    conn.sendall(message)

def stringToDatetime(string):

    return dt.datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")

def handleConnection(conn):

    username = None

    try:

        while True:

            head = conn.recv(2)

            payload = conn.recv(int.from_bytes(head, 'little', signed=False))

            result = json.loads(payload.decode('utf-8'))

            print(result)
            print(username)
            print("")

            if result["type"] == 1:

                break

            elif result["type"] == 2:

                user = auth.verifyUserUsingPassword(result["username"], result["password"])

                if user:

                    username = result["username"]
                    users[username] = conn

                    userDict = {"type": 2,
                                "username": result["username"],
                                "friends": db.getUserFriends(result["username"]),
                                "messages": db.getUserMessages(result["username"])}

                    if result["rememberMe"]:

                        userDict["seriesID"], userDict["token"] = auth.createLoginToken(username)

                    send(conn, json.dumps(userDict, default=str))

                else:

                    send(conn, json.dumps({"type": 0, "errorMessage": "Invalid username or password"}))

            elif result["type"] == 3:

                user = auth.verifyUserUsingToken(result["username"], result["seriesID"], result["token"])

                if user:

                    username = result["username"]
                    users[username] = conn

                    userDict = {"type": 2,
                                "username": result["username"],
                                "friends": db.getUserFriends(result["username"]),
                                "messages": db.getUserMessages(result["username"]),
                                "seriesID": result["seriesID"]}

                    userDict["token"] = auth.updateLoginToken(result["username"], result["seriesID"])

                    send(conn, json.dumps(userDict, default=str))

                else:

                    send(conn, json.dumps({"type": 0, "errorMessage": "Invalid token"}))

            if username:

                if result["type"] == 5 and username == result["sender"]:

                    db.addNewMessage(result["sender"], result["recipient"], result["message"], stringToDatetime(result["timeSent"]))

                    send(conn, json.dumps({"type": 5,
                                           "sender": username,
                                           "recipient": result["recipient"],
                                           "message": result["message"],
                                           "timeSent": result["timeSent"]}))

                    if result["recipient"] in users:

                        send(users[result["recipient"]], json.dumps({"type": 5,
                                                                     "sender": username,
                                                                     "recipient": result["recipient"],
                                                                     "message": result["message"],
                                                                     "timeSent": result["timeSent"]}))

        conn.close()

        if username:

            users.pop(username)

    except Exception as error:

        print(f"error occurred: {error}")

        if username:

            users.pop(username)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()

    print(f"Listening on host {HOST} and port {PORT}")

    while True:

        conn, addr = s.accept()

        print(f"Connection with {addr}")

        th.Thread(target=handleConnection, args=(conn,)).start()

