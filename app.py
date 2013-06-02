__author__ = 'mjholler'

from flask import Flask
app = Flask(__name__)

import nccmail
from database import Database

@app.route("/")
def index():
    db = Database()
    output = ""
    if nccmail.isup():
        output += "<h1>Yes. NCC mail appears to be working just fine</h1>"
    else:
        output += "<h1>Nope. NCC mail looks down from here! :("
    output += "<br />Uptime: %s percent" % db.get_mail_uptime()
    return output

if __name__ == "__main__":
    app.run()
