from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy library to work with databases
import os  # Import OS library to interact with the operating system
from flask import Flask  # Import Flask framework
import secrets  # Import secrets library to generate secure tokens
# from flask_migrate import Migrate

app = Flask(__name__)  # Create an instance of the Flask application
app.secret_key = secrets.token_hex()  # Set a secret key for the application to use for encryption

path = os.path.join(os.path.dirname(__file__), 'database.db')  # Set a path variable for the database file
URI = 'sqlite:///{}'.format(path)  # Set the URI for the database

app.config['SQLALCHEMY_DATABASE_URI'] = URI  # The database URI that should be used for the connection. 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Set the application to track modifications to the database
#If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals. 
#source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

db = SQLAlchemy(app)  # Create an instance of the SQLAlchemy database
# migrate = Migrate(app, db)

#from app import routing  # Import the routing module for the Flask application


#note: GPT assistance was used in adding in line comments