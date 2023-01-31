#!/usr/bin/env python3
''' Basic Flask app '''

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    ''' Output templates '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
