import string
from hashlib import sha256
import random as r

def generateSalt():

    return ('').join([r.choice(string.ascii_letters) for c in range(8)])

def hashPassword(pwd):

    salt = generateSalt()

    return sha256((pwd + salt).encode('utf-8')).hexdigest()