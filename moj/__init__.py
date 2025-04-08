import os
from flask import Flask, redirect

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), 'templates')  # 👈 force it!
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'moj.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import jokes          
    app.register_blueprint(jokes.bp)

    @app.route('/hello')
    def hello():
        return 'Hello, Master of Jokes!'
    
    @app.route('/')
    def root():
        return redirect('/joke')

    return app
