
#importing libraries
import unittest
import os
from app import app, db
from app.db_models import User, Task
import tempfile
from werkzeug.exceptions import HTTPException
import requests

#chatgpt assistance was used in ensuring some tests are correct



class TestingWebApp(unittest.TestCase):

    def setUp(self):
        """ setUp method is called before running each test. """
        self.base_url = 'http://127.0.0.1:5000/'
        
    # """ tearDown method is called after running each test to clean up the testing environment by removing the database session and dropping all tables. """
    #     # db.session.remove()
    #     # db.drop_all()
    
    def test_registration_page_loads(self):
        """ test_registration_page_loads method tests if the registration page loads successfully """
        response = requests.get(self.base_url + '/register')
        self.assertEqual(response.status_code, 200)

    def test_registration_get(self):
        """ This test simply tests that a registration page works"""
        response = requests.get(self.base_url + '/register')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        """Testing the registration page"""
        data = {'username': 'testuser', 'password': 'testpass'}
        # send a request to the registration endpoint with the username and password
        response = requests.post(self.base_url + '/register', data=data)
        self.assertEqual(response.status_code, 200) # check if the response status code is 200 (success)


    def test_login(self):
        """Test login page"""
        data = {'username': 'testuser', 'password': 'testpass'}
        response = requests.post(self.base_url + '/login', data=data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Test logout functionality"""
        response = requests.get(self.base_url + '/logout')
        self.assertEqual(response.status_code, 200)


#Further tests would explore all the code functionality regarding tasks
#This would include the processes of task creation, adding and deletion
#We may also test fo changing the statuses of tasks (fom new to in progress)
#we can also test invalid data such as >100 character username


if __name__ == '__main__':
    unittest.main()

  