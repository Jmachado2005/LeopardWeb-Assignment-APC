# this is the .py file that will contain all the code for the classes and objects of the LeopardWeb project
# Written by Harrison Brown

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


    def logout(self):
        print("logout");
    def course_search(self):
        print("course search");
    def parameter_search(self):
        print("parameter search");

class Student(User):
    def __init__(self, wit_ID, first_name, last_name, grad_year, major, email):
        super().__init__(first_name, last_name, wit_ID, email)
        self.grad_year = grad_year
        self.major = major

    def addDrop_course(self):

    def check_conflicts(self):

    def print_schedule(self):


class Instructor(User):
    def __init__(self, wit_ID, first_name, last_name, title, hire_year, department, email, course):
        super().__init__(first_name, last_name, wit_ID, email)
        self.title = title
        self.hire_year = hire_year
        self.department = department
        self.course = course

    def print_teaching_schedule(self):

    def search_student(self):

    def print_roster(self):


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