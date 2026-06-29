# this will be the main file where everything will be run from. 
# This is the file that the end user will interact with.

from LeopardWeb_Project_Functions import login
import LeopardWeb_Project_DB_Commands
import LeopardWeb_Project_GUI_Commands
from LeopardWeb_Project_Classes_and_Objects import User, Student, Instructor, Admin
import sqlite3
import tkinter

conn = sqlite3.connect("LeopardWeb_Project.db")
cursor = conn.cursor()

test = User
studentTest = Student 
instructorTest = Instructor
adminTest = Admin

exit = 0    # variable used to exit loop when the user wants to logout

 # *** TO DO: figure out how to get past the login part and show the selection screen for end-user based on their role ***

systemUser = login()

print("*** User Using System: ***")
print(systemUser)

while exit != 1:

    # showing selection screen based on role

    if (role == 1):     # student has logged in
         print("Welcome, [name here]!")
         print("Please see below for your options:")

         print("[1] - Search Courses")
         print("[2] - Advanced Course Search")
         print("[3] - Add/Drop")
         print("[4] - Check Conflicts in Schedule")
         print("[5] - Print Schedule")
         print("[0] - Logout")

         print(f"Enter your choice below ")
         choice = input("Choice: ")

         if (choice == 1):
             studentTest.course_search()
         elif (choice == 2):
             studentTest.parameter_search()
         elif (choice == 3):
            studentTest.addDrop_course()
         elif (choice == 4):
            studentTest.check_conflicts()
         elif (choice == 5):
            studentTest.print_schedule()
         elif (choice == 0):
            studentTest.logout
            exit = 1;
         else:
            print("Invalid option. Pleas try again")


    elif (role == 2):   # instructor has logged in
         print("Welcome, [name here]!")
         print("Please see below for your options:")

         print("[1] - Search Courses")
         print("[2] - Advanced Course Search")
         print("[3] - Print Teaching Schedule")
         print("[4] - Search Course Roster for Student")
         print("[5] - Print Course Roster")
         print("[0] - Logout")

         print(f"Enter your choice below ")
         choice = input("Choice: ")

         if (choice == 1):
             instructorTest.course_search()
         elif (choice == 2):
             instructorTest.parameter_search()
         elif (choice == 3):
            instructorTest.print_teaching_schedule()
         elif (choice == 4):
            instructorTest.search_student()
         elif (choice == 5):
            instructorTest.print_roster()
         elif (choice == 0):
            instructorTest.logout
            exit = 1;
         else:
            print("Invalid option. Pleas try again")

    elif (role == 3):   # admin has logged in
         print("Welcome, [name here]!")
         print("Please see below for your options:")

         print("[1] - Search Courses")
         print("[2] - Advanced Course Search")
         print("[3] - Add Courses to the System")
         print("[4] - Add Student to System")
         print("[5] - Add Instructor to System")
         print("[6] - Link Instructor to Course")
         print("[7] - Unlink Instructor from Course")
         print("[8] - Add Student to a Course")
         print("[9] - Remove Student from a Course")
         print("[0] - Logout")
         print(f"Enter your choice below ")
         choice = input("Choice: ")

         if (choice == 1):
            adminTest.course_search()
         elif (choice == 2):
             adminTest.parameter_search()
         elif (choice == 3):
            adminTest.add_course_system
         elif (choice == 4):
            adminTest.add_student
         elif (choice == 5):
            adminTest.add_instructor
         elif (choice == 6):
             adminTest.link_instructor
         elif (choice == 7):
            adminTest.unlink_instructor
         elif (choice == 8):
            adminTest.add_student_course
         elif (choice == 9):
            adminTest.remove_student_course
         elif (choice == 0):
            adminTest.logout
            exit = 1;
         else:
            print("Invalid option. Pleas try again")

         




