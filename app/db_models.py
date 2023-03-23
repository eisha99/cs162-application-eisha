
#importing libraries
from app import db
from sqlalchemy import Enum


#we begin by defining a User class that inherits from db.Model.

class User(db.Model):
    """
       This is a class for User (table) with the columns password and username respectively
    """
    __tablename__ = 'users' # Define the __tablename__ attribute to specify the name of the database table.
    # __table_args__ = {'extend_existing': True}
    password = db.Column(db.String, nullable  = False) # Define the password column with no maximum length and set it as not nullable.
    username = db.Column(db.String(30), primary_key = True) # Define the username column with a maximum length of 30 and set it as the primary key. We use this for the next table!
    

# then we define a Task class that also inherits from db.Model.

class Task(db.Model):
    """
        This is a class for Task which is connected to the user table above with a 1 to many relationship (foreign key used).
        It includes the column id (primary key), columns for usernames, titles and status for our tasks
    """
    __tablename__ = 'tasks' # Define the __tablename__ attribute to specify the name of the database table.
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True) #defining as the primary key the ID column
    username = db.Column(db.String, db.ForeignKey('users.username')) #creating a username column in the task table 
    #we set it up as a foreign key referencing the username column of the users table.
    title = db.Column(db.String(120), nullable = False) 
    #title column for task titles or names with a 120 character limit
    status = db.Column(Enum('new', 'in_progress', 'finished')) #we create 3 different types of tasks (do, doing, done) as per instructions
    
    
    




db.create_all() #This line creates all the tables that have been defined in the Flask application using the db.Model class.
db.session.commit() #This line commits the changes made to the database by the previous db.create_all() command.