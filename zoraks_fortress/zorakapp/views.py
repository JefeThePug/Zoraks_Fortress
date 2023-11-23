from flask import render_template, request, make_response, session
from zorakapp import app
import sys
import uuid

@app.route('/')
def index():
    user_id = session.get('user_id')

    if user_id is None:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id

        response = make_response(render_template('game.html'))
        response.set_cookie('user_id', user_id)

        print('new! User ID:', user_id, file=sys.stderr)
        return response

    print('User ID:', user_id, file=sys.stderr)
    return render_template('game.html')

@app.route('/map')
def map():
    user_id = session.get('user_id')

    if user_id is None:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id

        response = make_response(render_template('map.html'))
        response.set_cookie('user_id', user_id)

        print('new! User ID:', user_id, file=sys.stderr)
        return response

    print('User ID:', user_id, file=sys.stderr)
    return render_template('map.html')