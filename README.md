
# Kanban Board 

## About

This is web application created with Flask that provides the functionality of a 3-step Kanban board. Users can either log in or sign up. Once logged in, users may log out. Users can add, delete or move tasks. Tasks can be of three types: 1) to do 2) doing 3) done. This management tool can help users remain productive and keep track of their tasks.

## File Structure

In the root directory:

- .env includes env variables that need to be set
- `app.py` defines the main Flask application instance. It includes the application routes, configurations, and other setup code.
- `test.py` used to store the unit tests for the web application.
- `requirements.txt` used to store a list of the required packages for the project.


In the `app` folder:

- `templates/` folder which has all the html templates that are to be rendered.
- `__init__.py` defines the initialization code for the package. 
- `db_models.py` defines the SQL connection for the web-app


The structure employed for thsi webapp was (http://flask.pocoo.org/docs/0.12/patterns/packages).

## Installation Instructions

Start virtual environment

    $ python3 -m venv venv
    $ source venv/bin/activate


Install necessary dependencies

    $ pip3 install -r requirements.txt

Start flask server (from the root directory)

    $ python3 app.py

For the above, note: use python + version you are using

The Kanban board should be up and running at http://127.0.0.1:5000/

## Unit Testing

On the project root directory, run

    $ python3 -m unittest discover test


## Resources

The following resources were used in the creation of this web app:

- https://semantic-ui.com/ -- this was used for styling purposes

- https://flask.palletsprojects.com/en/2.0.x/tutorial/

- https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

- https://www.youtube.com/watch?v=QAFL-QOuejk&ab_channel=MayanwolfeStreams

- https://github.com/vuhcl/kanban-board

- Chat GPT -- used to assist in bug fixing, adding inline comments and fixing tests  


## Notes

Coverage is not considered for unittesting