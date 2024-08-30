import os

from flask import Flask, render_template

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Load config file if it exists, while NOT testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test configs if they are passed
        app.config.from_mapping(test_config)
    
    # Ensuring the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Simple page that says 'Hello!'. Needed for tests
    @app.route('/hello')
    def hello():
        return 'Hello, world!'
    
    # Simple page that shows site is working for normal users
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app