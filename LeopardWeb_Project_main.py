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

#DEBUGGING
# print("*** User Using System: ***")
# print(vars(systemUser))
# print(systemUser.wit_ID)

while exit != 1:

    # showing selection screen based on role
    if (systemUser.wit_ID > 10000 and systemUser.wit_ID < 20000):     # student has logged in
         print("----------------------LEOPARDWEB APC PROJECT----------------------")
         print("Welcome, " + systemUser.first_name + " " + systemUser.last_name + "!")
         print("Please see below for your options:")

         print("[1] - Search Courses")
         print("[2] - Advanced Course Search")
         print("[3] - Add/Drop")
         print("[4] - Check Conflicts in Schedule")
         print("[5] - Print Schedule")
         print("[0] - Logout")

         print(f"Enter your choice below ")
         choice = input("Choice: ")
         choice = int(choice)

         #DEBUGGING  print(choice)

         if (choice == 1):
             systemUser.course_search()
         elif (choice == 2):
             systemUser.parameter_search()
         elif (choice == 3):
            systemUser.addDrop_course()
         elif (choice == 4):
            systemUser.check_conflicts()
         elif (choice == 5):
            systemUser.print_schedule()
         elif (choice == 0):
             print("Goodbye!")
             exit = 1;
         else:
            print("Invalid option. Please try again")


    elif (systemUser.wit_ID > 20000 and systemUser.wit_ID < 30000):   # instructor has logged in
         print("----------------------LEOPARDWEB APC PROJECT----------------------")
         print("Welcome, Professor " + systemUser.last_name + "!")
         print("Please see below for your options:")

         print("[1] - Search Courses")
         print("[2] - Advanced Course Search")
         print("[3] - Print Teaching Schedule")
         print("[4] - Search Course Roster for Student")
         print("[5] - Print Course Roster")
         print("[0] - Logout")

         print(f"Enter your choice below ")
         choice = input("Choice: ")
         choice = int(choice)

         if (choice == 1):
             systemUser.course_search()
         elif (choice == 2):
             systemUser.parameter_search()
         elif (choice == 3):
            systemUser.print_teaching_schedule()
         elif (choice == 4):
            systemUser.search_student()
         elif (choice == 5):
            systemUser.print_roster()
         elif (choice == 0):
            print("Goodbye!")
            exit = 1;
         else:
            print("Invalid option. Please try again")

    elif (systemUser.wit_ID > 30000):   # admin has logged in
         print("----------------------LEOPARDWEB APC PROJECT----------------------")
         print("Welcome, " + systemUser.title + " " + systemUser.first_name + " " + systemUser.last_name + "!")
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
         choice = int(choice)

         if (choice == 1):
            systemUser.course_search()
         elif (choice == 2):
             systemUser.parameter_search()
         elif (choice == 3):
            systemUser.add_course_system()
         elif (choice == 4):
            systemUser.add_student()
         elif (choice == 5):
            systemUser.add_instructor()
         elif (choice == 6):
             systemUser.link_instructor()
         elif (choice == 7):
            systemUser.unlink_instructor()
         elif (choice == 8):
            systemUser.add_student_course()
         elif (choice == 9):
            systemUser.remove_student_course()
         elif (choice == 0):
            print("Goodbye!")
            exit = 1;
         else:
            print("Invalid option. Please try again")

         




