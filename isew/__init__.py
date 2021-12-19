import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',   #change to a random value for deployment
        DATABASE=os.path.join(app.instance_path, 'isew.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # a simple page that welcomes the API
    @app.route('/')
    def home():
        return """Esta es la API REST de ISEW, tenemos los siguientes métodos disponibles: /hello, /auth/register """


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # start DB
    from . import db
    db.init_app(app)

    #add blueprints and views for authentication 
    from . import auth
    app.register_blueprint(auth.bp)

    

    return app