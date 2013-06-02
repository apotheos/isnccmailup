__author__ = 'mjholler'


import imaplib
import json
from database import Database

config = json.load(open('config.json', 'r+'))['email']


def isup():
    try:
        nccmail = imaplib.IMAP4_SSL(config['host'])
        nccmail.login(config['user'], config['password'])
        nccmail.list()
    except Exception as e:
        return False

    return True


if __name__ == '__main__':
    db = Database()
    db.insert_mail_status(isup())

