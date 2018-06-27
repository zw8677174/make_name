# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from model.Name import Name

app = Flask(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/name/get')
def get():
    return Name.get_name()


@app.route('/test')
def test():
    return 'Hello World!2'


if __name__ == '__main__':
    app.run(debug=True)
