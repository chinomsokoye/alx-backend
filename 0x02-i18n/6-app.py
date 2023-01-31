#!/usr/bin/env python3
''' Basic Flask app and Babel setup, Get Locale from request
Parameterized templates, Force locale with URL parameter
Use user locale '''

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    ''' Function before request '''
    g.user = get_user()


@babel.localeselector
def get_locale():
    ''' Determine best match with supported languages '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' Output templates '''
    return render_template('6-index.html')


def get_user():
    ''' Returns a user dictionary or None '''
    Id = request.args.get('login_as')
    if Id and int(Id) in users:
        return users[int(Id)]
    else:
        return None


if __name__ == '__main__':
    app.run()
