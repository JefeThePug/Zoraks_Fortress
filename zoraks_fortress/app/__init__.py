from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import zoraks_fortress.views


# Define your Flask extensions here
db = SQLAlchemy()

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('config.py', silent=True)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from your_app.routes import main_bp
    app.register_blueprint(main_bp)

    # Add more configurations and extensions as needed

    return app
