# Import necessary libraries
import os
from app import app
from app import db
from dotenv import load_dotenv
from app.db_models import User, Task
from flask_login import current_user, login_user, logout_user, login_required
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_sqlalchemy import SQLAlchemy

load_dotenv() # Load environment variables from .env file

#setting up routes for the app

    
#the route for registration
@app.route('/registration', methods=["GET","POST"])
def registration():
    """ 
        This is the registration page where users can enter an email and a password to create an account.
    """
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        if not user:
            user = User(username = request.form['username'], password = request.form['password'])
            #user is asked to enter a username and a password
            db.session.add(user) #for the current session we add this user
            db.session.commit()
            session['username'] = user.username #the username for this session then becomes this username
            return redirect(url_for('index'))
        else:
            flash('The username you entered is already taken. Please choose a different one.')
            return render_template("registration.html") #if the username exists user gets to fill out the form again to enter a unique username
    else:
        return render_template("registration.html") 
    
#the route for logging in
@app.route('/login', methods = ['GET','POST'])
def login(): 
    """ 
     This is the Log In page where users can login with their existing username and password
    """
    error = None
    if request.method == 'POST': #we first check if the user's username and password match database records
        user = db.session.query(User).filter(User.username==request.form['username']).first()
        #if the username isn't correct
        if not user: 
            flash('Username is invalid')
            error = 'Incorrect email/password combination'
        elif user.password == request.form['password']:
            session['username'] = user.username
            # if the username and password match 
            app.logger.info(session['username']) #user is successfully logged in
            return redirect(url_for("index")) #redirected to the main app page where the Kanban resides
        else: #otherwise if password is the issue
            flash('Password is invalid')
            error = 'Incorrect email/password combination'

    return render_template("login.html", error = error)
    #we redirect to the login page

#the route for the main page for the app
@app.route('/')
def index():
    """ 
        This is the Kanban app home page where users first land. They have the option to sign up or log in.
    """
    #since a new user is "not" logged in
    if 'username' not in session:
        return render_template('home.html') #the user is directed straight to the home page
    else: 
        # if the user is already logged in
        new, in_progress, finished = [],[],[] #we create 3 different lists of new, in_progress and finished statuses for our tasks
        tasks = db.session.query(Task).filter(Task.username==session.get('username'))
        #empty lists for each task type are created and the database is queried for the existing user info
        for a in tasks: #for each task a
            if a.status == 'new': #we add it to new if it was in new
                #print(a)
                #for debugging
                new.append(a)
            elif a.status == 'in_progress': #we add it to in progress if it was in progress
                in_progress.append(a)
            else:
                #print(a)
                finished.append(a) #otherwise we simply say the task is finished
    #otherwise the user goes to the main page where the task board resides
    return render_template("index.html", new = new,in_progress =in_progress, finished=finished, user=session.get('username')) 

#the route for logging out of the app
@app.route('/logout')
def logging_out():
    """
       This is used in the case where a logged in users wishes to log out
    """
    session.pop('username', None) #we pop the username from the session
    return redirect(url_for('index')) #user is redirected to the index which takes it to the home page



#For Tasks

#we create a route for adding tasks
@app.route('/add', methods=['POST'])
def add():
    """
    This is for adding tasks to the Kanban Board.
    """
    #for the users who are logged in
    newtask = Task(
        title=request.form['task'],
        username=session.get('username'),
        status='new'
    )
    db.session.add(newtask)
    db.session.commit()
    return redirect(url_for('index')) #once task is added, the kanban (updated) is shown

#route for removing tasks
@app.route('/delete/task/<id>', methods=['GET', 'POST', 'DELETE'])
def delete(id):
    """ This is for deleting existing tasks """
    #we first check that a task exists in the database
    exist = db.session.query(Task).filter(Task.id==int(id)).first()
    if not exist:
        abort(404)  #gives error if it does not exist
    #otherwise if the task does exist
    db.session.delete(exist) #then the existing task is deleted
    db.session.commit()
    return redirect(url_for('index'))#redirects to home page

#route for changing the statuses of tasks
@app.route('/update/task/<id>/<status>')
def status_update(id, status):
    """
    This is for moving the status of a task from new to in progress or finished.
    
    """
    #we first check that a task exists in the database
    exist = db.session.query(Task).filter(Task.id==int(id)).first()
    if not exist:
        abort(404) #gives error if it does not exist
    # Otherwise
    exist.status = status #the task status is changed to the new one
    db.session.commit()  
    return redirect(url_for('index')) #redirects to home page



if __name__ == '__main__':
    app.run(debug=True) #as required





if __name__ == '__main__': # Define the entry point of the application
    port = int(os.environ.get('PORT', 5000)) 
    # Get the port number from the environment variable or use 5000 as the default
    app.run(host='0.0.0.0', port=port)
    # Run the Flask application on all available network interfaces and the specified port
