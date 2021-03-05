from flask import Flask, render_template, abort, redirect, request, url_for, session
# from werkzeug.contrib.cache import SimpleCache
from cachelib import SimpleCache
from datetime import datetime
import time

CACHE_TIMEOUT = 300

cache = SimpleCache()
cache.timeout = CACHE_TIMEOUT

app = Flask(__name__)

app.secret_key = 'SET_COOKIE'


@app.before_request
def return_cache():
    if not request.values:
        response = cache.get(request.path)
        if response:
            print('Got the page from cache')
            return response
    print('will load the page')


@app.after_request
def cache_response(response):
    if not request.values:
        cache.set(request.path, response, timeout=CACHE_TIMEOUT)
    return response


@app.route('/')
def hello_word():
    # return redirect('/check')
    return render_template('hello.html', name='hello')


# @app.route('/wirte_session')
# def write_session():
#     session['key_time'] = time.time()
#     # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     return str(session.modified)
#
#
# @app.route('/read_session')
# def read_session():
#     return str(session.get('key_time'))
#
#
# @app.route('/add/<int:number>')
# def add_one(number):
#     return str(number + 1)
#
#
# @app.route('/sendMessage', methods=['GET', 'POST'])
# def sendMessage():
#     if request.method == 'POST':
#         return 'post'
#     else:
#         return 'get'
#
#
# @app.route('/check')
# def check():
#     abort(400)
#
#
# @app.route('/industry')
# def f_industry():
#     pass
#
#
# @app.errorhandler(400)
# def bad_request(error):
#     return render_template('bad_request.html')
#
#
# @app.route('/hello')
# @app.route('/hello/<name>')
# def render_hello(name=None):
#     return render_template('hello.html', name=name)
#
#
# with app.test_request_context():
#     print(url_for('f_industry'), '<====')

if __name__ == '__main__':
    app.run()
