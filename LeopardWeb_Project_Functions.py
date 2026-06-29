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

            #make sure user's entered info is correct
            if user_info is None:
                # user does NOT exist in the system
                print("User not found. Please Try Again\n")
            elif user_info is not None:
                # user exists in the system
                print(f"User Data: {user_info}")

                # extract what is needed from login for main selection menu
                userID = str(user_info[0])
                # print(userID)

                first_ID_num = userID[0]
                # print(first_ID_num)

                if(first_ID_num == "1"):
                    # TESTING:  print("*** TRYING TO RETURN A STUDENT ***")
                    cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (first_ID_num));
                    student_info = cursor.fetchone()
                    return Student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4], student_info[5])
               
                elif(first_ID_num == "2"):
                    cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?""", (first_ID_num));
                    professor_info = cursor.fetchone()
                    systemUser = Instructor(professor_info[0], professor_info[1], professor_info[2], professor_info[3], professor_info[4], professor_info[5], professor_info[6], professor_info[7])
                    return systemUser

                elif(first_ID_num == "3"):
                    cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?""", (first_ID_num));
                    admin_info = cursor.fetchone()
                    systemUser = Admin(admin_info[0], admin_info[1], admin_info[2], admin_info[3], admin_info[4], admin_info[5])
                    return systemUser
                
                break


