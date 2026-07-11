# this will be the file that I do all my tests in:
# *** MAKE SURE TO PUT THIS FILE INTO THE MAIN BRANCH BEFORE RUNNING TESTS OTHERWISE IT WILL NOT WORK. *** 

import unittest
import sqlite3
import io

from unittest.mock import patch
from contextlib import redirect_stdout

from LeopardWeb_Project_Classes_and_Objects import Student, User

# doing test cases for Add/remove course from semester schedule (student)
class TestAddDrop(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            10001,
            "Burt",
            "Chance",
            2027,
            "Applied Science",
            "chanceb@wit.edu"
        )

        self.conn = sqlite3.connect("LeopardWeb_Project.db")
        self.cursor = self.conn.cursor()

        # clear schedule first
        self.cursor.execute("""
        UPDATE STUDENT
        SET COURSE_ONE=NULL,
            COURSE_TWO=NULL,
            COURSE_THREE=NULL,
            COURSE_FOUR=NULL,
            COURSE_FIVE=NULL
        WHERE ID=10001
        """)

        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    # *** Comment out the test cases below that you don't want to run, and uncomment the ones you do want to run. ***
    # TEST 1: Student adds a valid course
    # @patch("builtins.input", side_effect=[
    #     "A",        # add
    #     "17242",    # crn
    #     "Y"         # confirm
    # ])
    # def test_add_valid_course(self, mock_input):

    #     self.student.addDrop_course()

    #     self.cursor.execute("""
    #     SELECT COURSE_ONE
    #     FROM STUDENT
    #     WHERE ID=10001
    #     """)

    #     result = self.cursor.fetchone()[0]

    #     self.assertEqual(str(result), "17242")

# unittest.main()

    # ************************************************************************** #

    # # TEST 2: Attempt to add a course that doesn't exist.
    # @patch("builtins.input", side_effect=[
    #     "A",
    #     "99999"
    # ])
    # def test_add_invalid_course(self, mock_input):

    #     output = io.StringIO()

    #     with redirect_stdout(output):
    #         self.student.addDrop_course()

    #     self.assertIn(
    #         "Course does not exist in database. Please try again",
    #         output.getvalue()
    #     )

# unittest.main()

    #*************************************************************************** #

    # # TEST 3: Student drops an existing course.
    # @patch("builtins.input", side_effect=[
    #     "D",
    #     "17242",
    #     "Y"
    # ])
    # def test_drop_course(self, mock_input):

    #     self.cursor.execute("""
    #     UPDATE STUDENT
    #     SET COURSE_ONE='17242'
    #     WHERE ID=10001
    #     """)

    #     self.conn.commit()

    #     self.student.addDrop_course()

    #     self.cursor.execute("""
    #     SELECT COURSE_ONE
    #     FROM STUDENT
    #     WHERE ID=10001
    #     """)

    #     result = self.cursor.fetchone()[0]

    #     self.assertIsNone(result)

# unittest.main()

 #*************************************************************************** #

 # TEST 4: Student attempts to drop a course that isn't in their schedule
#     @patch("builtins.input", side_effect=[
#         "D",
#         "17020"
#     ])
#     def test_drop_course_not_enrolled(self, mock_input):

#         output = io.StringIO()

#         with redirect_stdout(output):
#             self.student.addDrop_course()

#         self.assertIn(
#             "not in your schedule",
#             output.getvalue()
#         )

# unittest.main()

#******************************* END OF FIRST FUNCTION TEST ******************************* #

# doing test cases for Search all courses (default search) (all users)
# class TestSearch(unittest.TestCase):

#     def setUp(self):

#         self.user = User(
#             "Joe",
#             "Machado",
#             1,
#             "joe@wit.edu"
#         )

#     @patch("builtins.input", side_effect=[
#         "Fall"
#     ])
#     def test_course_search(self, mock_input):

#         output = io.StringIO()

#         with redirect_stdout(output):
#             self.user.course_search()

#         text = output.getvalue()

#         self.assertIn("Fall", text)
#         self.assertIn("Computer", text)

# unittest.main()

#******************************* END OF SECOND FUNCTION TEST ******************************* #

# doing test cases for Search courses based on parameters (all users)
class TestParameterSearch(unittest.TestCase):

    def setUp(self):

        self.user = User(
            "Joe",
            "Machado",
            1,
            "joe@wit.edu"
        )
    # TEST 1: Deparment Search
#     @patch("builtins.input", side_effect=[
#         "Fall",
#         "Yes",
#         "Department",
#         "ELEC"
#     ])
#     def test_department_search(self, mock_input):

#         output = io.StringIO()

#         with redirect_stdout(output):
#             self.user.parameter_search()

#         text = output.getvalue()

#         self.assertIn("ELEC", text)
#         self.assertIn("Digital Logic", text)

# unittest.main()

 #*************************************************************************** #
    # TEST 2: Credits Search
#     @patch("builtins.input", side_effect=[
#         "Fall",
#         "Yes",
#         "Credits",
#         "4"
#     ])
#     def test_credit_search(self, mock_input):

#         output = io.StringIO()

#         with redirect_stdout(output):
#             self.user.parameter_search()

#         self.assertIn("Credits", output.getvalue())

# unittest.main()

 #*************************************************************************** #

    # TEST 3: Year Search
#     @patch("builtins.input", side_effect=[
#         "Fall",
#         "Yes",
#         "Year",
#         "2026"
#     ])
#     def test_year_search(self, mock_input):

#         output = io.StringIO()

#         with redirect_stdout(output):
#             self.user.parameter_search()

#         self.assertIn("2026", output.getvalue())

# unittest.main()

 #*************************************************************************** #

    # TEST 4: Search without an additional paramater
    @patch("builtins.input", side_effect=[
        "Fall",
        "No"
    ])
    def test_search_without_parameter(self, mock_input):

        output = io.StringIO()

        with redirect_stdout(output):
            self.user.parameter_search()

        self.assertIn("CRN", output.getvalue())

unittest.main()

#******************************* END OF THIRD FUNCTION TEST ******************************* #