#!/usr/bin/env python3
''' Basic Flask app and Babel setup
Get Locale from request
Parameterized templates'''

from flask import Flask, request, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    ''' Determine best match with supported languages '''
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' Output templates '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
