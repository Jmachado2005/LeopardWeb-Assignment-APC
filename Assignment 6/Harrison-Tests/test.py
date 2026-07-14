import unittest
import sqlite3
import io
from io import StringIO
from unittest.mock import patch
from contextlib import redirect_stdout

from LeopardWeb_Project_Functions import login
from LeopardWeb_Project_Classes_and_Objects import Student, Instructor, Admin

#test cases for login functionality
class TestLoginFunction(unittest.TestCase):
    # ----------------------------------------- Test Case for Correct Login for a Student. -----------------------------------------

    #@patch("builtins.input", side_effect=["chanceb", "BurtIsDaBest"])
    #def test_login_student(self, mock_input):
        

        #user = login()

        #self.assertIsInstance(user, Student)
        #self.assertEqual(user.wit_ID, 10001)

#unittest.main()

# ----------------------------------------- Test Case for Incorrect Username for a Student. -----------------------------------------

    #@patch("builtins.input", side_effect=["chancep", "BurtIsDaBest",])
    #def test_wrong_username_student(self, mock_input):
        
        #errorMessage = io.StringIO()
        #with redirect_stdout(errorMessage):
            #login()
        #output = errorMessage.getvalue()
        #print(output)
        #self.assertEqual(output, "Log In To System:\nIncorrect Username and/or Password. Please Try Again\n\n")

#unittest.main()

# ----------------------------------------- Test Case for Incorrect Password for a Student. -----------------------------------------

    #@patch("builtins.input", side_effect=["chanceb", "BurtIsTheBest"])
    #def test_invalid_password(self, mock_input):

        #errorMessage = io.StringIO()
        #with redirect_stdout(errorMessage):
            #login()
        #output = errorMessage.getvalue()
        #print(output)
        
        #self.assertEqual(output, "Log In To System:\nIncorrect Username and/or Password. Please Try Again\n\n")
#unittest.main()

    # ----------------------------------------- Test Case for Correct Login for a Instructor. -----------------------------------------

    #@patch("builtins.input", side_effect=["gorboldb", "Manag3mt4L1f3"])
    #def test_login_student(self, mock_input):
        

        #user = login()

        #self.assertIsInstance(user, Instructor)
        #self.assertEqual(user.wit_ID, 20001)

#unittest.main()

    # ----------------------------------------- Test Case for Correct Login for an Admin. -----------------------------------------

    @patch("builtins.input", side_effect=["machadoj", "testing123"])
    def test_login_student(self, mock_input):
        

        user = login()

        self.assertIsInstance(user, Admin)
        self.assertEqual(user.wit_ID, 30002)

unittest.main()