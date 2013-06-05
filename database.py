__author__ = 'mjholler'

import pymysql
from app import config

db_config = config['database']


class Database(object):
    __TABLE_MAIL_STATUS = 'mail_status'
    __TABLE_MAIN_SITE_STATUS = 'main_site_status'

    def __init__(self):
        self.db = pymysql.connect(**db_config)
        self.db.autocommit(True)

    def insert_mail_status(self, status):
        self.__insert_status(status, Database.__TABLE_MAIL_STATUS)

    def insert_main_site_status(self, status):
        self.__insert_status(status, Database.__TABLE_MAIN_SITE_STATUS)

    def get_mail_uptime(self):
        return self.__get_uptime(Database.__TABLE_MAIL_STATUS)

    def get_main_site_uptime(self):
        return self.__get_uptime(Database.__TABLE_MAIN_SITE_STATUS)

    def get_last_sample(self):
        query = "SELECT status, time FROM {0} ORDER BY time DESC LIMIT 1"
        c = self.db.cursor()
        c.execute(query.format(Database.__TABLE_MAIL_STATUS))

        return c.fetchone()

    def __insert_status(self, status, status_table):
        query = 'INSERT INTO {0}(status) VALUES (%s)'.format(status_table)
        c = self.db.cursor()
        c.execute(query, (int(status),))

    def __get_uptime(self, status_table, days=30):
        query = """SELECT COUNT(*) FROM {0} WHERE status = {1}
            AND (time BETWEEN DATE_SUB(NOW(), INTERVAL {2} DAY) AND NOW())"""
        c = self.db.cursor()
        c.execute(query.format(status_table, 1, days))
        up = c.fetchone()[0]
        c = self.db.cursor()
        c.execute(query.format(status_table, 0, days))
        down = c.fetchone()[0]
        return round(((up / float((up + down))) * 100), 2)
