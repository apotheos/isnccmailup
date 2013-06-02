import json

__author__ = 'mjholler'

import pymysql

config = json.load(open('config.json', 'r+'))['database']


class Database(object):
    def __init__(self):
        self.db = pymysql.connect(**config)

    def insert_mail_status(self, status):
        c = self.db.cursor()
        c.execute('INSERT INTO mail_status(status) VALUES (%d)', (int(status),))

    def get_mail_uptime(self):
        c = self.db.cursor()
        up = c.execute('SELECT COUNT(*) FROM mail_status WHERE status = 1').fetchone()[0]
        down = c.execute('SELECT COUNT(*) FROM mail_status WHERE status = 0').fetchone()[0]
        return up / (up + down)
