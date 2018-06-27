# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from service.PoemNameService import PoemNameService
from service.PoetryNameService import PoetryNameService
from random import *

app = Flask(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/name/get')
def get():
    names = []
    for i in range(8):
        if randint(0, 10) == 9:
            ret = PoemNameService.get()
        else:
            ret = PoetryNameService.get()
        names.append(ret)

    return render_template('index.html', names=names)


@app.route('/test')
def test():
    return 'Hello World!2'


if __name__ == '__main__':
    app.run(debug=True)
