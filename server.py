"""FEMA disaster declarations summaries."""

from jinja2 import StrictUndefined

from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

import fema_api as fema
from disaster_helper import count_disasters

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "\x92V\xae\x14\xbfT\xc4\x17\x8f\xd5;\x08"

app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Homepage."""
    return render_template("homepage.html")


@app.route("/filters.json", methods=['POST'])
def get_filters():
    """Uses form values to filter disaster data from API."""
    fd = request.form.get("fd")
    td = request.form.get("td")
    disasters = request.form.get("disasters")

    uri = fema.format_all(fd, td, disasters)
    resp = fema.request(uri)
    count = count_disasters(resp)

    return jsonify(count)


if __name__ == "__main__":
    # Set debug=True if invoking the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    # DebugToolbarExtension(app)


    app.run(port=5000, host='0.0.0.0')
