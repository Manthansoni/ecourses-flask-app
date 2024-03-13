'''
Main Database connection is done here
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_msearch import Search
from flask_mail import Mail, Message

SECRET_KEY = os.urandom(32)

app = Flask(
    __name__,
    template_folder="../../templates",
    static_folder="../../static",
    static_url_path="/",
)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost/flaskDB"
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

app.config['SECRET_KEY'] = SECRET_KEY

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'manthan0404soni@gmail.com'
app.config['MAIL_PASSWORD'] = 'ydbvvkqkcmmbajlm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = SQLAlchemy(app)

search = Search()
search.init_app(app)

def create_db():
    ''' it will create model table if not exist.'''
    from app.model.auth import Profile, Course, Enrollments

    with app.app_context():
        db.create_all()
