import json

__author__ = 'mjholler'

import pymysql

config = json.load(open('config.json', 'r+'))['database']


class Database(object):
    def __init__(self):
        self.db = pymysql.connect(**config)
        self.db.autocommit(True)

    def insert_mail_status(self, status):
        c = self.db.cursor()
        c.execute('INSERT INTO mail_status(status) VALUES (%s)', (int(status),))

    def get_mail_uptime(self):
        c = self.db.cursor()
        c.execute('SELECT COUNT(*) FROM mail_status WHERE status = 1')
        up = c.fetchone()[0]
        print up
        c = self.db.cursor()
        c.execute('SELECT COUNT(*) FROM mail_status WHERE status = 0')
        down = c.fetchone()[0]
        print down
        return (up / float((up + down))) * 100

if __name__ == '__main__':
    print Database().get_mail_uptime()
