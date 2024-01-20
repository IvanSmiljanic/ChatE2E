import crypto as c
import db

def verifyUserUsingPassword(username, password):

    rec = db.getUserRecord(username)

    if rec == None:

        return False

    if c.hashPasswordWithSalt(password, rec[2]) == rec[1]:

        return rec

    return False