import crypto as c
import db
import random as r

def verifyUserUsingPassword(username, password):

    rec = db.getUserRecord(username)

    if rec == None:

        return False

    if c.hashPasswordWithSalt(password, rec[2]) == rec[1]:

        return rec

    return False

def verifyUserUsingToken(username, seriesID, token):

    t = db.getLoginToken(username, seriesID)

    if t is None:

        return False

    if t == c.hashToken(token):

        return db.getUserRecord(username)

    return False

def createLoginToken(username):

    seriesID = r.randint(0, 2_147_483_647)
    token = r.randint(0, 2_147_483_647)

    db.addLoginToken(username, seriesID, c.hashToken(token))

    return seriesID, token

def updateLoginToken(username, seriesID):

    token = r.randint(0, 2_147_483_647)

    print("a")

    db.updateLoginToken(username, seriesID, c.hashToken(token))

    print("b")

    return token