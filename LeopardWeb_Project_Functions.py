# this is the file that will store all the misc functions that this project

from LeopardWeb_Project_Classes_and_Objects import User, Student, Instructor, Admin
import sqlite3

conn = sqlite3.connect("LeopardWeb_Project.db")
cursor = conn.cursor()

def login():
        exit = 0

        while (exit != 1):
            print("Log In To System:")
            username = input("Username: ")
            password = input ("Password: ")
            cursor.execute("""SELECT * FROM LOGIN WHERE USERNAME = ? AND PASSWORD = ?""", (username, password)); #Use this to pass variables into a query
            user_info = cursor.fetchone()

            # make sure user's entered info is correct
            if user_info is None:
                # user does NOT exist in the system
                print("Incorrect Username and/or Password. Please Try Again\n")
            elif user_info is not None:
                # user exists in the system
                print(f"User Data: {user_info}\n\n")

                # get the user ID to fetch the correct information from the database
                userID = int(user_info[0])

                if(user_info[3] == 1):
                    cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (userID,));
                    student_info = cursor.fetchone()
                    systemUser = Student(wit_ID=student_info[0], first_name=student_info[1], last_name=student_info[2], grad_year=student_info[3], major=student_info[4], email=student_info[5])
                    return systemUser

                elif(user_info[3] == 2):
                    cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?""", (userID,));
                    professor_info = cursor.fetchone()
                    systemUser = Instructor(professor_info[0], professor_info[1], professor_info[2], professor_info[3], professor_info[4], professor_info[5], professor_info[6])
                    return systemUser

                elif(user_info[3] == 3):
                    cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?""", (userID,));
                    admin_info = cursor.fetchone()
                    systemUser = Admin(admin_info[0], admin_info[1], admin_info[2], admin_info[3], admin_info[4], admin_info[5])
                    return systemUser
                
                break


