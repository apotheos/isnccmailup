__author__ = 'mjholler'

import os
basedir = os.path.dirname(os.path.realpath(__file__))

import json
config = json.load(open(os.path.join(basedir, 'config.json'), 'r+'))

from flask import Flask, render_template
app = Flask(__name__)

from dateutil import tz

import helper
from database import Database
from datetime import datetime
import time


@app.route("/")
def index():
    to_zone = tz.gettz(config['application']['timezone'])
    db = Database()
    kwargs = dict()
    kwargs['mail_up'], kwargs['sample_time'] = db.get_last_sample()
    # print type(kwargs['sample_time'])
    kwargs['sample_time'] = datetime.fromtimestamp(time.mktime(kwargs['sample_time'].timetuple()), tz=to_zone)
    # print kwargs['sample_time']
    kwargs['sample_time'] = kwargs['sample_time'].strftime('%B %d, %Y at %I:%M %p')
    kwargs['webmail_url'] = config['email']['webmail_url']
    kwargs['mail_uptime'] = db.get_mail_uptime()
    kwargs['mail_level'] = helper.get_level(kwargs['mail_uptime'])
    kwargs['site_url']= config['site']['url']
    kwargs['site_uptime'] = db.get_main_site_uptime()
    kwargs['site_level'] = helper.get_level(kwargs['site_uptime'])
    return render_template('index.html',
                           **kwargs)
                           ## mail_up=uptime.is_mail_up(),
                           #mail_up=mail_up,
                           #sample_time=sample_time,
                           #webmail_url=config['email']['webmail_url'],
                           #mail_level=mail_level,
                           #mail_uptime=db.get_mail_uptime(),
                           #site_url=config['site']['url'],
                           #site_level=site_level,
                           #site_uptime=db.get_main_site_uptime())

if __name__ == "__main__":
    app_config = config['application']
    app.run(port=app_config['port'], debug=app_config['debug'])
