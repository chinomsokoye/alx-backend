#!/usr/bin/env python3
''' Basic Flask app and Babel setup, Get Locale from request
Parameterized templates, Force locale with URL parameter '''

from typing import Union
from flask import Flask, render_template, request, g
from os import getenv
from flask_babel import Babel
from pytz import timezone

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('7-app.Config')


@app.before_request
def before_request():
    ''' Function before request '''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    ''' Determine best match with supported languages '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    ''' Output templates '''
    return render_template('7-index.html')


def get_user() -> Union[dict, None]:
    ''' Returns a user dictionary or None '''
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@babel.timezoneselector
def get_timezone():
    ''' Infer appropriate timezone '''
    user = getattr(g, 'locale', None)
    if user is not None:
        return user.timezone


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
