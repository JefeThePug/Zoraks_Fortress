# config.py

# Flask app configuration
DEBUG = True  # Set to False in production
SECRET_KEY = 'I am the Lone Locust of the apocalypse'

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
