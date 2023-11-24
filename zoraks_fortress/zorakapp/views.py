from flask import render_template, redirect, request, make_response, session, jsonify, url_for
from zorakapp import app
from zorakapp.parser import Parser
from zorakapp.helper import get_hash_index as ghi, go_home
import sys
import uuid


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # User input command
        try:
            data = request.get_json()
            inner_html = data.get('inner_html', '')

            parser = Parser(data.get('command', ''))
            parts = parser.get_parts()

            if parts["verb"] == "start":
                inner_html = "" #TODO get_story(0)
                parser.verb = ""
            print(f'words: {parser}, {parser.raw_cmd[0]=}', file=sys.stderr)

            if f"{parser}" or parser.raw_cmd[0] == "start":
                output = f"<i>{parser}</i>"
            else:
                output = f"{' '.join(parser.raw_cmd)}?</p><p>I don't know what you mean."
            return f"{inner_html}<p>{output}</p>"

        except Exception as e:
            print(f'Error: {e}', file=sys.stderr)
            return jsonify({'result': 'error', 'error_message': str(e)})
    
    else:
        # Page loads
        user_id = session.get('user_id')
        if user_id is None:
            user_id = str(uuid.uuid4())
            session['user_id'] = user_id

            response = make_response(render_template('game.html'))
            response.set_cookie('user_id', user_id)

            print('new! User ID:', user_id, file=sys.stderr)
            return response

        print('User ID:', user_id, file=sys.stderr)
        map_available = True
        return render_template('game.html', map_available=map_available)
    

@app.route('/map')
def map():
    user_id = session.get('user_id')
    #TODO get map availability
    map_available = True
    if user_id is None or not map_available:
        return go_home()
    

    #TODO get user visited spaces
    visited = {
        130, 131, 132, 133, 273, 274, 147, 148, 149, 150, 151, 152, 153, 294, 168, 169, 170, 
        171, 172, 173, 174, 315, 189, 190, 191, 192, 193, 194, 195, 210, 211, 212, 213, 214, 
        215, 89, 90, 91, 231, 232, 233, 234, 235, 109, 110, 111, 112, 113, 252, 253, 254,
        } #temporary

    map_cols = [[ghi(n) if (n:=i+s) in visited else "x" for i in range(0, 336, 21)] for s in range(21)]
    print(*map_cols, sep="\n", file=sys.stderr)

    return render_template('map.html', map_cols=map_cols)

@app.route('/notes')
def notes():
    user_id = session.get('user_id')
    if user_id is None:
        return go_home()

    map_available = True
    return render_template('notes.html', map_available=map_available)

@app.route('/about')
def about():
    user_id = session.get('user_id')
    if user_id is None:
        return go_home()

    return render_template('about.html')

@app.route('/settings')
def settings():
    user_id = session.get('user_id')
    if user_id is None:
        return go_home()

    return render_template('settings.html')

@app.route('/howto')
def howto():
    user_id = session.get('user_id')
    if user_id is None:
        return go_home()

    return render_template('howto.html')