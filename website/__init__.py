from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
db_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        create_database()

    return app


def create_database():
    if not path.exists('website/' + db_name):
        db.create_all()
        print('Created Database!')


if __name__ == '__main__':
    app = create_app()
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True) 
>>>>>>> f6f0fe58dca47a4a22c0f0af0d6bc8769b6b065d
