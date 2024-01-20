import psycopg2

def connectToDatabase():

    conn = psycopg2.connect("dbname=chate2edb user=newuser")

    cur = conn.cursor()

    return conn, cur

def getUserRecord(username):

    conn, cur = connectToDatabase()

    cur.execute("SELECT * FROM public.users WHERE username = %s", (username,))
    rec = cur.fetchone()

    conn.close()

    return rec

def addNewUser(username, password, salt):

    conn, cur = connectToDatabase()

    cur.execute("INSERT INTO public.users (username, password, salt) values (%s, %s, %s)",
                (username, password, salt))

    conn.commit()
    conn.close()

def getLoginToken(username, seriesID):

    conn, cur = connectToDatabase()

    cur.execute("SELECT token FROM public.logintokens WHERE username = %s AND series_id = %s", (username, seriesID,))
    token = cur.fetchone()

    if token != None:
        token = token[0]

    conn.close()

    return token

def addLoginToken(username, seriesID, tokenHash):

    conn, cur = connectToDatabase()

    cur.execute("INSERT INTO public.logintokens VALUES (%s, %s, %s)", (username, seriesID, tokenHash,))

    conn.commit()
    conn.close()

def updateLoginToken(username, seriesID, tokenHash):

    conn, cur = connectToDatabase()

    cur.execute("UPDATE public.logintokens SET token = %s WHERE username = %s AND series_id = %s", (tokenHash, username, seriesID,))

    conn.commit()
    conn.close()

def addNewMessage(sender, recipient, message, timestamp):

    conn, cur = connectToDatabase()

    cur.execute("INSERT INTO public.messages (sender, recipient, message, time_sent) VALUES (%s, %s, %s, %s)",
                (sender, recipient, message, timestamp,))

    conn.commit()
    conn.close()

def getUserFriends(username):

    conn, cur = connectToDatabase()

    cur.execute("SELECT username1 FROM public.friendships WHERE username2 = %s", (username,))
    tempFriends = cur.fetchall()

    cur.execute("SELECT username2 FROM public.friendships WHERE username1 = %s", (username,))
    tempFriends += cur.fetchall()

    conn.close()

    friends = []

    for friend in tempFriends:

        friends.append(friend[0])

    return friends

def getUserMessages(username):

    conn, cur = connectToDatabase()

    cur.execute("SELECT sender, recipient, message, time_sent FROM public.messages WHERE sender = %s OR recipient = %s", (username, username,))
    recs = cur.fetchall()

    conn.close()

    messages = []

    for message in recs:

        messages.append({"sender": message[0], "recipient": message[1], "message": message[2], "timeSent": message[3]})

    return messages
