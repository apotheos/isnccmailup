__author__ = 'mjholler'


import requests
import imaplib
import json
from database import Database


def is_mail_up():
    email_config = json.load(open('config.json', 'r+'))['email']

    try:
        mail = imaplib.IMAP4_SSL(email_config['host'])
        mail.login(email_config['user'], email_config['password'])
    except Exception as e:
        return False

    return True


def is_main_site_up():
    site_config = json.load(open('config.json', 'r+'))['site']
    r = requests.get(site_config['url'])
    return r.ok


if __name__ == '__main__':
    db = Database()
    db.insert_mail_status(is_mail_up())
    print 'inserted mail status'
    db.insert_main_site_status(is_main_site_up())
    print 'inserted main site status'

