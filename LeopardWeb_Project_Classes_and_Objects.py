# this is the .py file that will contain all the code for the classes and objects of the LeopardWeb project

from ctypes.util import test
from math import e
import re
import sqlite3
import tkinter
from tkinter import *
from tkinter.ttk import * 
from tkinter import ttk
from turtle import reset


conn = sqlite3.connect("LeopardWeb_Project.db")
cursor = conn.cursor()

class User:
    def __init__(self, first_name, last_name, wit_ID, email):
        self.first_name = first_name
        self.last_name = last_name
        self.wit_ID = wit_ID
        self.email = email

    def course_search(self):
        semester = input("What semester are you searching for courses in: ")
        cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ?""", (semester,));
        print("See All Courses Below:\n")
        for row in cursor:
            print(row)
        print("\n\n")
        
    def parameter_search(self):
        semester = input("What semester are you searching for courses in: ")
        additional_search = input("Do you want to search with an additional parameter? (Yes/No) ")
        if additional_search == "Yes":
            print("Year")
            print("Department")
            print("Credits")
            parameter_two = input("Choose One: ")
            parameter_value = input("Enter a value/department: ")
            if parameter_two == "Year":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND YEAR = ?""", (semester, parameter_value));
                print(f"Showing you classes for year: {parameter_value}\n")
                print("CRN | TITLE | DEPARTMENT | TIMES | DAYS OF THE WEEK | INSTRUCTOR | SEMESTER | YEAR | CREDITS")
                for row in cursor:
                    print(row)
                print("\n\n")
            elif parameter_two == "Department":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND DEPARTMENT = ?""", (semester, parameter_value));
                print(f"Showing you classes for department: {parameter_value}\n")
                print("CRN | TITLE | DEPARTMENT | TIMES | DAYS OF THE WEEK | INSTRUCTOR | SEMESTER | YEAR | CREDITS")
                for row in cursor:
                    print(row)
                print("\n\n")
            elif parameter_two == "Credits":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND CREDITS = ?""", (semester, parameter_value));
                print(f"Showing you classes with: {parameter_value} Credits\n")
                print("CRN | TITLE | DEPARTMENT | TIMES | DAYS OF THE WEEK | INSTRUCTOR | SEMESTER | YEAR | CREDITS")
                for row in cursor:
                    print(row)
                print("\n\n")
        else:
            cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ?""", (semester,));
            print("CRN | TITLE | DEPARTMENT | TIMES | DAYS OF THE WEEK | INSTRUCTOR | SEMESTER | YEAR | CREDITS")
            for row in cursor:
                print(row)
            print("\n\n")

class Student(User):
    def __init__(self, wit_ID, first_name, last_name, grad_year, major, email):
        super().__init__(first_name, last_name, wit_ID, email)
        self.grad_year = grad_year
        self.major = major

    def addDrop_course(self):
        print("Add/Drop Courses:")

      # allows the student to add or drop courses from their schedule
        exit = 0;   # exit variable used throughout the method to allow user to exit the loop when they are done adding/dropping courses

        while exit != 1:
            # ask student whether they want to add or drop a course
            print("Would you like to add or drop a course? (A/D)")
            choice = input(f"Choice: ")

            if choice == "A":   # ADD
                # Ask student to enter the CRN of the course they want to add
                print("Please enter the CRN of the course you want to add to your schedule: ")
                crn_choice = input(f"CRN: ")
                # query the database to see if the course exists
                cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (crn_choice,))
                course = cursor.fetchone()
                #DEBUGGING  print(course)

                if course is not None:   # if the course exists
                    # Show the student the course information and ask to confirm if they want to add it to their schedule
                    print("\nCourse information: ")
                    print (f"CRN: {course[0]}, Course Name: {course[1]}, Department: {course[2]}, Time: {course[3]}, Days of the Week: {course[4]} Location: {course[4]}, Instructor: {course[5]}, Semester: {course[6]}, Year: {course[7]}, Credits: {course[8]} ")

                    print("\nAre you sure you want to add this course to your schedule? (Y/N)")
                    choice = input(f"Choice: ")

                    if choice == "Y":   # if student confirms they want to add the course
                        course_to_add = course[0]   # takes the CRN value of the course the student wants to add to their schedule

                        #queries what's currently in the student's schedule and stores it into a list
                        cursor.execute("""SELECT COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENT WHERE ID = ?""", (str(self.wit_ID),),)
                        schedule = cursor.fetchone()
                        #DEBUGGING  print(schedule)

                        columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]    # stores values from columns COURSE_ONE to COURSE_FIVE in a list

                        empty_column = None     # creates a variable to compare if a value from any of the courses above has something already stored in it

                        # loops thru "schedule" to find an open slot in the student's table
                        for i in range(5):
                            if schedule[i] is None:
                                empty_column = columns[i]
                                break
                        
                        # Adds course to the open slot found in the student's table
                        if empty_column is not None:
                            cursor.execute(f"""UPDATE STUDENT SET {empty_column} = ? WHERE ID = ?""", (course_to_add, self.wit_ID),)

                            conn.commit()
                            # print confirmation message that the course has been added to their schedule
                            print(f"\n\nCourse has been added to your schedule!\n")

                            # loop ends - brings them back to the selection screen
                            exit = 1;
                        else:
                            print("\nMaximum amount of courses reached! You cannot add any more to your schedule \n\n")
                    elif choice == "N":   # if student does not want to add the course
                        # prints message that the course has not been added to their schedule and we are sending them back to the add/drop menu screen
                        print("\nCourse NOT added to your schedule.")
                        print("Sending you back to Add/Drop Courses menu...\n\n")    
                else:   # if the course does not exist
                    print("Course does not exist in database. Please try again.\n\n")

            elif choice == "D":  # DROP
                # Ask student to enter the CRN of the course they want to drop
                print("Please enter the CRN of the course you want to drop from your schedule: ")
                crn_choice = int(input(f"CRN: "))

                # look in the student's schedule inside of the student table in the DB -> if that CRN is found, ask student if they would like to remove the course
                cursor.execute("""SELECT COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENT WHERE ID = ?""", (str(self.wit_ID),),)

                schedule = cursor.fetchone()

                if crn_choice not in schedule:
                    print("\nThis course is not in your schedule\n\n")
                else:
                    print("\nCourse was found in your schedule!")
                    print("Are you sure you want to drop this course? (Y/N)")
                    choice = input("Choice: ")

                if choice == "Y":

                    columns = ["COURSE_ONE","COURSE_TWO","COURSE_THREE","COURSE_FOUR","COURSE_FIVE"]

                    for i in range(5):
                        if schedule[i] == crn_choice:
                            course_column = columns[i]
                            break

                    cursor.execute(f"""UPDATE STUDENT SET {course_column} = NULL WHERE ID = ?""", (str(self.wit_ID),),)

                    conn.commit()

                    print("\nCourse has been removed from your schedule!\n\n")

                    exit = 1;

                elif choice == "N":
                    print("\nCourse was not removed.")
                    print("Sending you back to the selection screen...\n\n")
                else:
                    print("\nInvalid Option. Pleae try again\n")

    def check_conflicts(self):
        print("Check Conflicts:")
        # check for conflicting CRN numbers that are stored in the student's table

        # do a query to grab all the CRNs of the classes the student is currently taking
        cursor.execute("""SELECT COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENT WHERE ID = ?""", (str(self.wit_ID),),)
        schedule = cursor.fetchone()   # list to holds onto all the courses a student is taking
        
        classes = [course for course in schedule if course is not None]     # filters out any "None" values
        
        if len(classes) != len(set(classes)):   # checks if length of classes is not equal to the length of set classes (sets CANNOT contain duplicates) 
            print(f"\nATTENTION: Student {self.wit_ID} has duplicate courses in their schedule!\n\n")
        else:
            print("\nNo Duplicate courses were found in your schedule!")


    def print_schedule(self):
        print("Print Schedule:")
        # since the courses are just stored in the student table as the CRN numbers, we need to take each number, look in the COURSES database, find those courses and then print the relevant information on them

        classes = []   # create a list to hold onto the student's classes & to be printed later in this section

        cursor.execute("""SELECT COURSE_ONE FROM STUDENT""")   # course 1 get CRN query
        course1 = cursor.fetchone()     # course 1 assign queried result to variable
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course1),)    # goes into the COURSES table and looks for a course with the relevant course information based on CRN from student's table
        course1_info = cursor.fetchall()    # puts all the information from the query above and puts it into a variable
        classes.append(course1_info)         # adds course 1 information to student's classes list

        # repeat steps for courses 2-5
        cursor.execute("""SELECT COURSE_TWO FROM STUDENT""") 
        course2 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course2),)   
        course2_info = cursor.fetchall() 
        classes.append(course2_info)   
        
        cursor.execute("""SELECT COURSE_THREE FROM STUDENT""")   
        course3 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course3),)   
        course3_info = cursor.fetchall() 
        classes.append(course3_info)

        cursor.execute("""SELECT COURSE_FOUR FROM STUDENT""")   
        course4 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course4),)   
        course4_info = cursor.fetchall() 
        classes.append(course4_info)

        cursor.execute("""SELECT COURSE_FIVE FROM STUDENT""")   
        course5 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course5),)  
        course5_info = cursor.fetchall() 
        classes.append(course5_info)

        # print the student's schedule (based on what's stored in their classes[] list)
        print("Your schedule is as follows: ")
        print("CRN | TITLE | DEPARTMENT | TIMES | DAYS OF THE WEEK | INSTRUCTOR | SEMESTER | YEAR | CREDITS")
        print("--------------------------------------------------------------------------------------------------")

        for row in classes:     # for-loop to go thru student's course and print their schedule
            print(row)


class Instructor(User):
    def __init__(self, wit_ID, first_name, last_name, title, hire_year, department, email):
        super().__init__(first_name, last_name, wit_ID, email)
        self.title = title
        self.hire_year = hire_year
        self.department = department

    def print_teaching_schedule(self):
        print("Your Teaching Schedule:\n")
        cursor.execute("""SELECT * FROM COURSES WHERE INSTRUCTOR_ID = ?""", (str(self.wit_ID),),);
        for row in cursor:
            print(row)
        print("\n")

    def search_student(self):
        print("\nYour Courses:")
        cursor.execute("""SELECT * FROM COURSES WHERE INSTRUCTOR_ID = ?""", (str(self.wit_ID),),);
        for row in cursor:
            print(row)
        print("\n")
        course = input("Enter a CRN from above of the course roster you want to search: ")
        student = int(input("Enter the ID of the student you are searching for: "))

        # checks to see if a student is taking the particular course CRN the user enters above
        cursor.execute("""SELECT ID FROM STUDENT WHERE ID = ? AND (COURSE_ONE = ? OR COURSE_TWO = ? OR COURSE_THREE = ? OR COURSE_FOUR = ? OR COURSE_FIVE = ?)""", (student, course, course, course, course, course));

        # stores this result essentially as a 'Yes' or 'No'
        result = cursor.fetchone()

        if result:
            print("\nThis student is taking your course.\n")
        else:
            print("\nThis student is not taking your course.\n")

    def print_roster(self):
        print("\nYour Courses:")
        cursor.execute("""SELECT * FROM COURSES WHERE INSTRUCTOR_ID = ?""", (str(self.wit_ID),),);
        for row in cursor:
            print(row)
        print("\n")

        courseCRN = input("What is the CRN of the course roster you want to view: ")
      
        cursor.execute("""SELECT NAME, SURNAME, ID FROM STUDENT WHERE COURSE_ONE = ? OR COURSE_TWO = ? OR COURSE_THREE = ? OR COURSE_FOUR = ? OR COURSE_FIVE = ?""", (courseCRN, courseCRN, courseCRN, courseCRN, courseCRN));
        print(f"Course Roster for: {courseCRN}\n")
        print("NAME | SURNAME | ID")
        for row in cursor:
            print(row)
        print("\n")


class Admin(User):
    #Constructor
    def __init__(self, wit_ID, first_name, last_name, title, office, email):
        super().__init__(first_name, last_name, wit_ID, email)
        self.title = title
        self.office = office

    # Add a course to the database
    def add_course_system(self):
        print ("Add a Course")

        # Allows the input of a CRN while checking to make sure it doesn't already exist
        CRN = 1

        while CRN == 1:
            CRN = input("Enter CRN: ")

            cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?;""", (CRN,))

            if cursor.fetchone() is not None or int(CRN) < 0 :
                print ("CRN already exists or value is negative, please enter a new CRN")
                CRN = 1

        # Entering and declaring other variables for insert into courses
        title = input("Enter course title: ")
        dep = input("Enter department: ")
        time = input("Enter time (range): ")
        DoW = input("Enter days of week: ")
        instID = int(input("Enter instructor ID (type 'None' if unassigned): "))
        semester = input("Enter semester: ")
        year = input("Enter year: ")
        creds = int(input("Enter credits: "))

        # Inserts course into database using above declarations
        cursor.execute("""INSERT OR IGNORE INTO COURSES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""", (CRN, title, dep, time, DoW, instID, semester, year, creds,))
        conn.commit()
        print(f"\nCourse: '{title}' Successfully added to the system!")


    # Adds a student to the database
    def add_student(self):
        print ("Add a Student")

        # Variable declaration
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")
        YoG = int(input("Enter year of graduation: "))
        Major = input("Enter major: ")
        Username = lName
        password = input("Enter password: ")

        # Checks if username is unique. If it isn't it adds a number to the end to correspond to number of users with that username
        cursor.execute("""SELECT COUNT(*) FROM STUDENT WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone()
        cursor.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone() + query_result
        cursor.execute("""SELECT COUNT(*) FROM ADMIN WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone() + query_result

        # Adds the corresponding number to the end of the username if relevant. Sets student email to username + @wit.edu
        if query_result[0] > 0:
            Username = (Username.lower()) + fName[0].lower() + str(query_result[0])
        else:
            Username = (Username.lower()) + fName[0].lower()

        email = Username + "@wit.edu"

        
        # Finds the max ID # that currently exists in the database and adds one to it. Sets the new user to that number
        cursor.execute("""SELECT MAX(ID) FROM STUDENT;""")
        maximum = cursor.fetchone()
        idNum = maximum[0] + 1

        
        # Inserts new student into login and student databases using above declarations
        cursor.execute("""INSERT OR IGNORE INTO STUDENT VALUES(?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL, NULL)""", (idNum, fName, lName, YoG, Major, email))
        conn.commit()

        cursor.execute("""INSERT OR IGNORE INTO LOGIN VALUES(?, ?, ?, 1)""" , (idNum, Username, password))
        conn.commit()

        print(f"\nStudent: '{fName} {lName}' successfully added to the system as: '{Username}'!\n")
    

    # Adds an instructor to the database
    def add_instructor(self):
        print ("Add an Instructor")

        # Has user declare relevant variables
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")
        title = input("Enter title: ")
        YoH = input("Enter year of hire: ")
        dept = input("Enter department: ")
        Username = lName
        password = input("Enter password: ")

        # Checks if username is unique. If it isn't it adds a number to the end to correspond to number of users with that username
        cursor.execute("""SELECT COUNT(*) FROM STUDENT WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone()
        cursor.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone() + query_result
        cursor.execute("""SELECT COUNT(*) FROM ADMIN WHERE SURNAME = ?;""", (str(Username),),)
        query_result = cursor.fetchone() + query_result

        # Adds the corresponding number to the end of the username if relevant. Sets instructor email to username + @wit.edu
        if query_result[0] > 0:
            Username = (Username.lower()) + fName[0].lower() + str(query_result[0])
        else:
            Username = (Username.lower()) + fName[0].lower()
        
        email = Username + "@wit.edu"

        # Finds the max ID # that currently exists in the instructor database and adds one to it. Sets the new user to that number
        cursor.execute("""SELECT MAX(ID) FROM INSTRUCTOR;""")
        maximum = cursor.fetchone()
        idNum = maximum[0] + 1

        
        # Inserts new instructor into login and instructor databases using above declarations
        cursor.execute("""INSERT OR IGNORE INTO INSTRUCTOR VALUES(?, ?, ?, ?, ?, ?, ?);""", (idNum, fName, lName, title, YoH, dept, email))
        conn.commit()

        cursor.execute("""INSERT OR IGNORE INTO LOGIN VALUES(?, ?, ?, 2);""", (idNum, Username, password))
        conn.commit()

        print(f"\nInstructor: '{fName} {lName}' successfully added to the system as: '{Username}'!\n")


    # Links an instructor to a course in the database
    def link_instructor(self):

        # Has the user enter the ID of the instructor and the CRN of the course they want to link them to
        regNum = input("Enter CRN of course to link instructor to: ")
        instID = input("Enter ID of instructor to link to course: ")
    

        # checks if instructor exists
        cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?""", (instID,))

        if cursor.fetchone() is None:
            print("\nInstructor not found!\n")
            return
        else:
            # checks if course exists
            cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (regNum,))
            if cursor.fetchone() is None:
                print("\nCourse not found!\n")
                return
            else:
                # Updates the courses table to have the linked instructor
                cursor.execute("""UPDATE COURSES SET INSTRUCTOR_ID = ? WHERE CRN = ?;""", (instID, regNum,))
                conn.commit()

        print(f"\nSuccessfully linked Instructor {instID} to course {regNum}!\n")
    
    # Unlinks an intructor from a course in the database
    def unlink_instructor(self):

        # Sets the instructor linkes to the selected course to NULL
        regNum = input("Enter CRN of course to unlink instructor from: ")
        cursor.execute("""UPDATE COURSES SET INSTRUCTOR_ID = NULL WHERE CRN = ?""", (regNum,))

        print(cursor.rowcount)
        conn.commit()

        print(f"\nSuccessfully unlinked Instructor from course: {regNum}!\n")
    
        
    # Adds a student to a course
    def add_student_course(self):
        # Has the user enter the ID of the student and the CRN of the course they want to add them to
        studentID = input("Enter ID of student to add to course: ")
        CRN = input("Enter CRN of course to add student to: ")


        #checks to make sure the student actually exists
        cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (studentID,))
        student = cursor.fetchone()

        if student is None:
            print("\nStudent not found!\n")
            return
        
        #checks to make sure the course actually exists
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (CRN,))
        course = cursor.fetchone()

        if course is None:
            print("\nCourse not found!\n")
            return

        # Checks to see if student is already enrolled in the course that was entered
        if CRN in student[6:11]:
            print("\nStudent is already enrolled in this course.\n")
            return

        # Finds the first empty spot in the students schedule
        course_columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]

        for i in range(5):

            if student[6 + i] is None:

                cursor.execute(f"""UPDATE STUDENT SET {course_columns[i]} = ? WHERE ID = ?""", (CRN, studentID))
                conn.commit()

            print(f"\nSuccessfully added student {studentID} to course {CRN}!\n")
            return

        # Prints a message that student is already enrolled in max number of courses if there is no empty spot in their schedule
        print("\nStudent is already enrolled in 5 courses.\n")
    
        
    # Removes a student from a course
    def remove_student_course(self):

        # Has the user enter the student ID and the CRN of the course they want to remove the student from
        studentID = input("Enter ID of student to remove from course: ")
        CRN = input("Enter CRN of course to remove student from: ")

        # Checks to make sure the student exists and is enrolled in the selected course then removes them from it
        cursor.execute(f"""SELECT COUNT(*) FROM STUDENT WHERE ID = ?""", (studentID))

        if cursor.fetchone() is not None:
            
            course_columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]

            for column in course_columns:

                cursor.execute(f"""SELECT * FROM STUDENT WHERE ID = ? AND {column} = ?""", (studentID, CRN))

                if cursor.fetchone() is not None:

                    cursor.execute(f"""UPDATE STUDENT SET {column} = NULL WHERE ID = ?""", (studentID,))
                    conn.commit()

                    print(f"\nSuccessfully removed student {studentID} from course {CRN}!\n")
                    return
        else:
            print("\nStudent does not exist\n")
            return

        print("\nStudent is not enrolled in that course.\n")

class Course:
    def __init__(self, CRN, title, department, time, days_of_week, semester, year, credit):
        self.CRN = CRN
        self.title = title
        self.department = department
        self.time = time
        self.days_of_week = days_of_week
        self.semester = semester
        self.year = year
        self.credit = credit
