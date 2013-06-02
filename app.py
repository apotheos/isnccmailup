__author__ = 'mjholler'

from flask import Flask
app = Flask(__name__)

import nccmail


@app.route("/")
def index():
    if nccmail.isup():
        return "<h1>Yes. NCC mail appears to be working just fine</h1>"
    else:
        return "<h1>Nope. NCC mail looks down from here! :("

if __name__ == "__main__":
    app.run()
