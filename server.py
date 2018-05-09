""" Project Skeleton Server - happy building!"""

import sys
import os

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request,
                   flash, session)
from flask_debugtoolbar import DebugToolbarExtension



# if want to source API key into environment every time, do this
# API_KEY = os.environ['API_KEY']

app = Flask(__name__)

app.secret_key = "skeleton_key"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Display Homepage."""

    return render_template("homepage.html")

if __name__ == "__main__":

    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")