import string
from hashlib import sha256
import random as r

def generateSalt():

    return ('').join([r.choice(string.ascii_letters) for c in range(8)])

def hashPasswordWithoutSalt(pwd):

    salt = generateSalt()

    return hashPasswordWithSalt(pwd, salt), salt

def hashPasswordWithSalt(pwd, salt):

    return sha256((pwd + salt).encode('utf-8')).hexdigest()