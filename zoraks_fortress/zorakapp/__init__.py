from flask import Flask


app = Flask(__name__)
app.secret_key = 'abcdefg1234567'
#?? app.config.from_pyfile('config.py', silent=True)
#?? app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app.db'
#?? db = SQLAlchemy(app)

from zorakapp import views