# this is the .py file that will contain all the code for the classes and objects of the LeopardWeb project

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

    def login(self):
        print("login");
        username = input("Username: ")
        password = input ("Password: ")
        cursor.execute("""SELECT * FROM LOGIN WHERE USERNAME = ? AND PASSWORD = ?""", (username, password)); #Use this to pass variables into a query
        user_info = cursor.fetchone()

        if(str(user_info[0])[0] == 1):
            cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (user_info[0]));
            student_info = cursor.fetchone()
            user = Student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4], student_info[5])

        elif(str(user_info[0])[0] == 2):
            cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?""", (user_info[0]));
            professor_info = cursor.fetchone()
            user = Instructor(professor_info[0], professor_info[1], professor_info[2], professor_info[3], professor_info[4], professor_info[5], professor_info[6], professor_info[7])

        elif(str(user_info[0])[0] == 3):
            cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?""", (user_info[0]));
            admin_info = cursor.fetchone()
            user = Admin(admin_info[0], admin_info[1], admin_info[2], admin_info[3], admin_info[4], admin_info[5])

        return user

    def course_search(self):
        semester = input("What semester are you searching for courses in: ")
        cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ?""", (semester));
        for row in cursor:
            print(row)
        
    def parameter_search(self):
        semester = input("What semester are you searching for courses in: ")
        additional_search = input("Do you want to search with an additional parameter: ")
        if additional_search == "Yes":
            print("Year")
            print("Department")
            print("Credits")
            parameter_two = input("Choose One: ")
            parameter_value = input("Enter a value/department: ")
            if parameter_two == "Year":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND YEAR = ?""", (semester, parameter_value));
                for row in cursor:
                    print(row)
            elif parameter_two == "Department":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND DEPARTMENT = ?""", (semester, parameter_value));
                for row in cursor:
                    print(row)
            elif parameter_two == "Credits":
                cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ? AND CREDITS = ?""", (semester, parameter_value));
                for row in cursor:
                    print(row)
        else:
            cursor.execute("""SELECT * FROM COURSES WHERE SEMESTER = ?""", (semester));
            for row in cursor:
                print(row)

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
                crn_choice = int(input(f"CRN: "))
                # query the database to see if the course exists
                cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn_choice))
                course = cursor.fetchone()

                if cursor.fetchone() is not None:   # if the course exists
                    # Show the student the course information and ask to confirm if they want to add it to their schedule
                    print("Course information: ")
                    print (f"CRN: {course[0]}, Course Name: {course[1]}, Department: {course[2]}, Time: {course[3]}, Days of the Week: {course[4]} Location: {course[4]}, Instructor: {course[5]}, Semester: {course[6]}, Year: {course[7]}, Credits: {course[8]} ")

                    print("Are you sure you want to add this course to your schedule? (Y/N)")
                    choice = input(f"Choice: ")

                    if choice == "Y":   # if student confirms they want to add the course
                        course_to_add = course[0]   # takes the CRN value of the course the student wants to add to their schedule

                        #queries what's currently in the student's schedule and stores it into a list
                        cursor.execute("""SELECT COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENT WHERE ID = ?""", (self.wit_ID))
                        schedule = cursor.fetchone()

                        columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]    # stores values from columns COURSE_ONE to COURSE_FIVE in a list

                        empty_column = None     # creates a variable to compare if a value from any of the courses above has something already stored in it

                        # loops thru "schedule" to find an open slot in the student's table
                        for i in range[5]:
                            if schedule[i] is None:
                                empty_column = columns[i]
                                break
                        
                        # Adds course to the open slot found in the student's table
                        if empty_column is not None:
                            cursor.execute(f"""UPDATE STUDENT SET {empty_column} = ? WHERE ID = ?""", (course_to_add, self.wit_ID))

                            conn.commit()
                            # print confirmation message that the course has been added to their schedule
                            print(f"Course has been added to your schedule!")

                            # loop ends - brings them back to the selection screen
                            exit = 1;
                        else:
                            print("Maximum amount of courses reached! You cannot add any more to your schedule ")
                    elif choice == "N":   # if student does not want to add the course
                        # prints message that the course has not been added to their schedule and we are sending them back to the add/drop menu screen
                        print("Course NOT added to your schedule.")
                        print("Sending you back to Add/Drop Courses menu...")    
                elif cursor.fetchone() is None:   # if the course does not exist
                    print("Course does not exist in database. Please try again.")

            elif choice == "D":  # DROP
                # Ask student to enter the CRN of the course they want to drop
                print("Please enter the CRN of the course you want to drop from your schedule: ")
                crn_choice = int(input(f"CRN: "))

                # look in the student's schedule inside of the student table in the DB -> if that CRN is found, ask student if they would like to remove the course
                cursor.execute("""SELECT COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENT WHERE ID = ?""", (self.wit_ID))

                schedule = cursor.fetchone()

                if crn_choice not in schedule:
                    print("This course is not in your schedule")
                else:
                    print("Course was found in your schedule!")
                    print("Are you sure you want to drop this course? (Y/N)")
                    choice = input("Choice: ")

                if choice == "Y":

                    columns = ["COURSE_ONE","COURSE_TWO","COURSE_THREE","COURSE_FOUR","COURSE_FIVE"]

                    for i in range(5):
                        if schedule[i] == crn_choice:
                            course_column = columns[i]
                            break

                    cursor.execute(f"""UPDATE STUDENT SET {course_column} = NULL WHERE STUDENT_ID = ?""", (self.wit_ID,))

                    conn.commit()

                    print("Course has been removed from your schedule!")

                    exit = 1;

                elif choice == "N":
                    print("Course was not removed.")
                    print("Sending you back to the selection screen...")
                else:
                    print("Invalid Option. Pleae try again")

    def check_conflicts(self):
        print("Check Conflicts:")
        # check for conflicting CRN numbers that are stored in the student's table

        # do a query to grab all the CRNs of the classes the student is currently taking
        cursor.execute("""SELECT ?, COURSE_ONE, COURSE_TWO, COURSE_THREE, COURSE_FOUR, COURSE_FIVE FROM STUDENTS""", (self.wit_ID))
        conflicts = cursor.fetchall()   # list to holds onto all the courses a student is taking

        # loop through each row to check for duplicates
        for rows in conflicts:
            self.wit.id = conflicts[0]
            classes = conflicts[1:6]    # creates an individual list for just the classes the student is taking

            if len(set(classes) < len(classes)):    # using "set" removes duplicate values in a list: so in our case, if the set() function is called, then that means there's a duplicate in the student's schedule
                print(f"ATTENTION: Student {self.wit_ID} has duplicate classes in their schedule!")


    def print_schedule(self):
        print("Print Schedule:")
        # since the courses are just stored in the student table as the CRN numbers, we need to take each number, look in the COURSES database, find those courses and then print the relevant information on them

        classes = []   # create a list to hold onto the student's classes & to be printed later in this section

        cursor.execute("""SELECT COURSE_ONE FROM STUDENTS""")   # course 1 get CRN query
        course1 = cursor.fetchone()     # course 1 assign queried result to variable
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course1))    # goes into the COURSES table and looks for a course with the relevant course information based on CRN from student's table
        course1_info = cursor.fetchall()    # puts all the information from the query above and puts it into a variable
        classes.append(course1_info)         # adds course 1 information to student's classes list

        # repeat steps for courses 2-5
        cursor.execute("""SELECT COURSE_TWO FROM STUDENTS""") 
        course2 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course2))   
        course2_info = cursor.fetchall() 
        classes.append(course2_info)   
        
        cursor.execute("""SELECT COURSE_THREE FROM STUDENTS""")   
        course3 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course3))   
        course3_info = cursor.fetchall() 
        classes.append(course3_info)

        cursor.execute("""SELECT COURSE_FOUR FROM STUDENTS""")   
        course4 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course4))   
        course4_info = cursor.fetchall() 
        classes.append(course4_info)

        cursor.execute("""SELECT COURSE_FIVE FROM STUDENTS""")   
        course5 = cursor.fetchone()     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (course5))  
        course5_info = cursor.fetchall() 
        classes.append(course5_info)

        # print the student's schedule (based on what's stored in their classes[] list)
        print("Your schedule is as follows: ")
        print("CRN\tTITLE\tDEPARTMENT\tTIMES\tDAYS OF THE WEEK\tINSTRUCTOR\tSEMESTER\tYEAR\tCREDITS")
        print("--------------------------------------------------------------------------------------------------")

        for row in classes:     # for-loop to go thru student's course and print their schedule
            print(row)


class Instructor(User):
    def __init__(self, wit_ID, first_name, last_name, title, hire_year, department, email, course):
        super().__init__(first_name, last_name, wit_ID, email)
        self.title = title
        self.hire_year = hire_year
        self.department = department
        self.course = course

    def print_teaching_schedule(self):
        cursor.execute("""SELECT * FROM COURSES WHERE ID = ?""", (self.wit_ID));
        for row in cursor:
            print(row)

    def search_student(self):
        cursor.execute("""SELECT * FROM COURSES WHERE ID = ?""", (self.wit_ID));
        for row in cursor:
            print(row)
        course = input("Enter the CRN of the course whose roster you want to search: ")
        cursor.execute("""SELECT ID FROM STUDENT WHERE COURSE_ONE = ? OR COURSE_TWO = ? OR COURSE_THREE = ? OR COURSE_FOUR = ? OR COURSE_FIVE = ?""", (course, course, course, course, course));
        student = input("What is the ID of the student you are searching for: ")
        for row in cursor:
            if row == student:
                print("This student is taking your course.")
                return

        print("This student is not taking your course.")

    def print_roster(self):
        courseName = input("What is the name of the course whose roster you want to view: ")
        cursor.execute("""SELECT CRN FROM COURSES WHERE NAME = ?""", (courseName));
        courseCRN = cursor.fetchone()
        cursor.execute("""SELECT * FROM STUDENT WHERE COURSE_ONE = ? OR COURSE_TWO = ? OR COURSE_THREE = ? OR COURSE_FOUR = ? OR COURSE_FIVE = ?""", (courseCRN, courseCRN, courseCRN, courseCRN, courseCRN));
        for row in cursor:
            print(row)


class Admin(User):
    def __init__(self, wit_ID, first_name, last_name, title, office, email):
        super().__init__(first_name, last_name, wit_ID, email)
        self.title = title
        self.office = office

    def add_course_system(self):
        print ("add later")

    def add_student(self):
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")
        YoG = input("Enter year of graduation: ")
        Major = input("Enter major: ")
        Username = lName + fName[0]

        cursor.execute("""SELECT COUNT FROM STUDENT WHERE SURNAME = Username;""")
        querey_result = cursor.fetchall()

        if querey_result > 0:
            Username = Username + str(querey_result)

        password = input("Enter password: ")

        cursor.execute("""SELECT MAX(ID) FROM STUDENT;""")
        maximum = cursor.fetch()

        idNum = maximum + 1

        sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(idNum, fName, lName, YoG, Major, Username + '@wit.edu');"""
        cursor.execute(sql_command)
        cursor.commit()


        sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(idNum, Username, password, 1);"""
        cursor.exectute(sql_command)
        cursor.commit()

    def add_instructor(self):
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")
        YoG = input("Enter year of graduation: ")
        Major = input("Enter major: ")
        Username = lName + fName[0]

        cursor.execute()("""SELECT COUNT FROM STUDENT WHERE SURNAME = Username;""")
        querey_result = cursor.fetchall()

        if querey_result > 0:
            Username = Username + str(querey_result)

        password = input("Enter password: ")

        sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20001, 'Bram', 'Gorbold', 'Dean of SoM', 2020, 'MGMT', 'gorboldb@wit.edu');"""
        cursor.execute(sql_command)

        sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20001, 'gorboldb', 'Manag3mt4L1f3', 2);"""
        cursor.exectute(sql_command)

    def link_instructor(self):

    def unlink_instructor(self):

    def add_student_course(self):

    def remove_student_course(self):
        

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
