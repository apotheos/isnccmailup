import json

__author__ = 'mjholler'

from flask import Flask, render_template
app = Flask(__name__)

import uptime
from database import Database


@app.route("/")
def index():
    db = Database()
    return render_template('index.html',
                           is_mail_up=uptime.is_mail_up(),
                           mail_uptime=db.get_mail_uptime(),
                           is_main_site_up=uptime.is_main_site_up(),
                           main_site_uptime=db.get_main_site_uptime())

if __name__ == "__main__":
    config = json.load(open('config.json', 'r+'))['application']
    app.run(port=config['port'], debug=config['debug'])
