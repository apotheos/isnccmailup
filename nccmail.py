import json

__author__ = 'mjholler'


import imaplib

config = json.load(open('config.json', 'r+'))['email']


def isup():
    try:
        nccmail = imaplib.IMAP4_SSL(config['host'])
        nccmail.login(config['user'], config['password'])
        nccmail.list()
    except Exception as e:
        return False

    return True


def log_status(status):
    pass


if __name__ == '__main__':
    log_status(isup())

