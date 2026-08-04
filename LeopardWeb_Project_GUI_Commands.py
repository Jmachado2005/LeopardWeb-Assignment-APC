# commands for the GUI

import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
# from PTL import Image, ImageTk
from LeopardWeb_Project_Functions import login
from LeopardWeb_Project_Classes_and_Objects import Course, User, Student, Instructor, Admin


# "logout" function
def open_exit_window():
    exit_win = tk.Toplevel()
    exit_win.title("Logout")
    exit_win.geometry("300x150")

    label = tk.Label(
        exit_win,
        text="You have been logged out.\nGoodbye!",
        font=("Arial", 12)
    )
    label.pack(pady=30)

    btn = tk.Button(exit_win, text="Close", command=exit_win.destroy)
    btn.pack()
# adds a course to the database(completed)
def GUIeditCourseDB(user):
    nWin = tk.Toplevel()
    nWin.title("Add a New Course")
    nWin.geometry("1200x800")

    # CRN
    crnTitle = tk.Label(nWin, text = "Enter New CRN")
    CRN = tk.Entry(nWin, width = 30)
    crnTitle.pack(pady = 10)
    CRN.pack(pady = 10)

    # Title
    titleTitle = tk.Label(nWin, text = "Enter Course Title")
    title = tk.Entry(nWin, width = 30)
    titleTitle.pack(pady = 10)
    title.pack(pady = 10)

    # dep
    depTitle = tk.Label(nWin, text = "Enter Department abbriviation")
    dep = tk.Entry(nWin, width = 30)
    depTitle.pack(pady = 10)
    dep.pack(pady = 10)

    # time
    timeTitle = tk.Label(nWin, text = "Enter Course Time (range)")
    time = tk.Entry(nWin, width = 30)
    timeTitle.pack(pady = 10)
    time.pack(pady = 10)

    # DoW
    DoWTitle = tk.Label(nWin, text = "Enter Days of the Week")
    DoW = tk.Entry(nWin, width = 30)
    DoWTitle.pack(pady = 10)
    DoW.pack(pady = 10)

    # semester
    semesterTitle = tk.Label(nWin, text = "Enter Semester")
    semester = tk.Entry(nWin, width = 30)
    semesterTitle.pack(pady = 10)
    semester.pack(pady = 10)

    # year
    yearTitle = tk.Label(nWin, text = "Enter Year")
    year = tk.Entry(nWin, width = 30)
    yearTitle.pack(pady = 10)
    year.pack(pady = 10)

    # credits
    creditTitle = tk.Label(nWin, text = "Enter # of Credits")
    credit = tk.Entry(nWin, width = 30)
    creditTitle.pack(pady = 10)
    credit.pack(pady = 10)

    def createCourse(time, CRN, title, dep, DoW, semester, year, credit):
     

        if (time == "" or CRN == "" or title == "" or dep == "" or DoW == "" or semester == "" or year == "" or credit == ""):
            win = tk.Toplevel()
            win.title("Error")
            win.geometry("600x300")

            error = tk.Label(win, text = "Error creating course. One or more data entries empty")
            error.pack()
        else:
            win = tk.Toplevel()
            win.title("Error")
            win.geometry("600x300")


            cursor.execute("""INSERT OR IGNORE INTO COURSES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""", (CRN, title, dep, time, DoW, None, semester, year, credit))
            conn.commit()

            success = tk.Label(win, text = "Successfully added course to database")
            success.pack()




    crnConfirmation = tk.Button(nWin, text = "confirm course", command = lambda: [createCourse(time.get(), CRN.get(), title.get(), dep.get(), DoW.get(), semester.get(), year.get(), credit.get())])
    crnConfirmation.pack(pady = 10)

    
    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)

# adds a student to the database(completed)
def GUIeditStudentDB(user):
    nWin = tk.Toplevel()
    nWin.title("Add a New Student")
    nWin.geometry("1200x800")



    # first Name
    fNameTitle = tk.Label(nWin, text = "Enter Student's First Name")
    fName = tk.Entry(nWin, width = 30)
    fNameTitle.pack(pady = 10)
    fName.pack(pady = 10)

    # last Name
    lNameTitle = tk.Label(nWin, text = "Enter Student's Last Name")
    lName = tk.Entry(nWin, width = 30)
    lNameTitle.pack(pady = 10)
    lName.pack(pady = 10)

    # year of graduation
    YoGTitle = tk.Label(nWin, text = "Enter Year of Graduation")
    YoG = tk.Entry(nWin, width = 30)
    YoGTitle.pack(pady = 10)
    YoG.pack(pady = 10)

    # major
    majorTitle = tk.Label(nWin, text = "Enter Major")
    Major = tk.Entry(nWin, width = 30)
    majorTitle.pack(pady = 10)
    Major.pack(pady = 10)

    # password
    passwordTitle = tk.Label(nWin, text = "Enter Student Password")
    password = tk.Entry(nWin, width = 30)
    passwordTitle.pack(pady = 10)
    password.pack(pady = 10)


    def createStudent(fName, lName, YoG, Major, password):
        Win = tk.Toplevel()
        Win.title("Add a New Student")
        Win.geometry("1200x800")

        Username = lName
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

        confirmation = tk.Label(Win, text = "Successfully added student to database")
        confirmation.pack()



    crnConfirmation = tk.Button(nWin, text = "confirm Student", command = lambda: [createStudent(fName.get(), lName.get(), YoG.get(), Major.get(), password.get())])
    crnConfirmation.pack(pady = 10)

    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)

# adds an instructor to the database(completed)
def GUIeditInstructorDB(user):
    nWin = tk.Toplevel()
    nWin.title("Add a New Instructor")
    nWin.geometry("1200x800")

    # first Name
    fNameTitle = tk.Label(nWin, text = "Enter Instructor's First Name")
    fName = tk.Entry(nWin, width = 30)
    fNameTitle.pack(pady = 10)
    fName.pack(pady = 10)

    # last Name
    lNameTitle = tk.Label(nWin, text = "Enter Instructor's Last Name")
    lName = tk.Entry(nWin, width = 30)
    lNameTitle.pack(pady = 10)
    lName.pack(pady = 10)

    # title
    titleTitle = tk.Label(nWin, text = "Enter Instructor's Title")
    title = tk.Entry(nWin, width = 30)
    titleTitle.pack(pady = 10)
    title.pack(pady = 10)

    # year of hire
    YoHTitle = tk.Label(nWin, text = "Enter Instructor's Year of Hire")
    YoH = tk.Entry(nWin, width = 30)
    YoHTitle.pack(pady = 10)
    YoH.pack(pady = 10)

    # department
    deptTitle = tk.Label(nWin, text = "Enter Instructor's Department")
    dept = tk.Entry(nWin, width = 30)
    deptTitle.pack(pady = 10)
    dept.pack(pady = 10)

    # password
    passwordTitle = tk.Label(nWin, text = "Enter instructor Password")
    password = tk.Entry(nWin, width = 30)
    passwordTitle.pack(pady = 10)
    password.pack(pady = 10)


    def createInstructor(fName, lName, title, YoH, dept, password):
        Win = tk.Toplevel()
        Win.title("Add a New Instructor")
        Win.geometry("1200x800")

        Username = lName
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

        
        # Finds the max ID # that currently exists in the instructor database and adds one to it. Sets the new user to that number
        cursor.execute("""SELECT MAX(ID) FROM INSTRUCTOR;""")
        maximum = cursor.fetchone()
        idNum = maximum[0] + 1

        
        # Inserts new instructor into login and instructor databases using above declarations
        cursor.execute("""INSERT OR IGNORE INTO INSTRUCTOR VALUES(?, ?, ?, ?, ?, ?, ?);""", (idNum, fName, lName, title, YoH, dept, email))
        conn.commit()

        cursor.execute("""INSERT OR IGNORE INTO LOGIN VALUES(?, ?, ?, 2);""", (idNum, Username, password))
        conn.commit()

        confirmation = tk.Label(Win, text = "Successfully added Instructor to database")
        confirmation.pack()



    crnConfirmation = tk.Button(nWin, text = "confirm Instructor", command = lambda: [createInstructor(fName.get(), lName.get(), title.get(), YoH.get(), dept.get(), password.get())])
    crnConfirmation.pack(pady = 10)

    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)

# links or unlinks an instructor to a course (completed)
def GUIlinkUnlinkInstructor(user):
    nWin = tk.Toplevel()
    nWin.title("Link/Unlink Instructor")
    nWin.geometry("1200x800")




    def linkInstructor():
        # Has the user enter the ID of the instructor and the CRN of the course they want to link them to
        Win = tk.Toplevel()
        Win.title("Link Instructor")
        Win.geometry("1200x800")
        # CRN
        fNameTitle = tk.Label(Win, text = "Enter Course CRN")
        regNum = tk.Entry(Win, width = 30)
        fNameTitle.pack(pady = 10)
        regNum.pack(pady = 10)

        # Instructor ID
        lNameTitle = tk.Label(Win, text = "Enter Instructor's ID")
        instID = tk.Entry(Win, width = 30)
        lNameTitle.pack(pady = 10)
        instID.pack(pady = 10)


        def linkCourse(regNum, instID):
            # checks if instructor exists
            cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID = ?""", (instID,))

            if cursor.fetchone() is None:
                wWin = tk.Toplevel()
                wWin.title("Error")
                wWin.geometry("1200x800")
                error = tk.Label(wWin, text = "Instructor not found")
                error.pack()
                return
            else:
                # checks if course exists
                cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (regNum,))

            if cursor.fetchone() is None:
                wWin = tk.Toplevel()
                wWin.title("Error")
                wWin.geometry("1200x800")
                error = tk.Label(wWin, text = "Course not found")
                error.pack()
                return
            else:
                # Updates the courses table to have the linked instructor
                cursor.execute("""UPDATE COURSES SET INSTRUCTOR_ID = ? WHERE CRN = ?;""", (instID, regNum,))
                conn.commit()
            wWin = tk.Toplevel()
            wWin.title("Add a New Instructor")
            wWin.geometry("1200x800")
            confirmation = tk.Label(wWin, text = "Successfully linked instructor to course")
            confirmation.pack()

            

        crnConfirmation = tk.Button(Win, text = "confirm Information", command = lambda: [linkCourse(regNum.get(), instID.get())])
        crnConfirmation.pack(pady = 10)
    


    # Unlinks an intructor from a course in the database
    def unlinkInstructor():
        # Has the user enter the ID of the instructor and the CRN of the course they want to link them to
        Win = tk.Toplevel()
        Win.title("Unlink Instructor")
        Win.geometry("1200x800")

        # CRN
        fNameTitle = tk.Label(Win, text = "Enter Course CRN")
        regNum = tk.Entry(Win, width = 30)
        fNameTitle.pack(pady = 10)
        regNum.pack(pady = 10)


        def unlinkCourse(regNum):
            
            cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (regNum,))
            
            cursor.execute("""UPDATE COURSES SET INSTRUCTOR_ID = NULL WHERE CRN = ?""", (regNum,))
            print(cursor.rowcount)
            conn.commit()
            
            wWin = tk.Toplevel()
            wWin.title("Add a New Instructor")
            wWin.geometry("1200x800")
            confirmation = tk.Label(wWin, text = "Successfully unlinked course")
            confirmation.pack()

            

        crnConfirmation = tk.Button(Win, text = "confirm Information", command = lambda: [unlinkCourse(regNum.get())])
        crnConfirmation.pack(pady = 10)

        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (regNum,))
        if cursor.fetchone() is None:
            wWin = tk.Toplevel()
            wWin.title("Register Student")
            wWin.geometry("1200x800")
            error = tk.Label(wWin, text = "Course not found")
            error.pack()
            return
        else:
            cursor.execute("""UPDATE COURSES SET INSTRUCTOR_ID = NULL WHERE CRN = ?""", (regNum,))
            print(cursor.rowcount)
            conn.commit()

        

        print(f"\nSuccessfully unlinked Instructor from course: {regNum}!\n")

    btn1 = tk.Button(nWin, text = "Link Instructor", command = linkInstructor)
    btn1.pack(pady = 10)
    btn2 = tk.Button(nWin, text = "Unlink Instructor", command = unlinkInstructor)
    btn2.pack(pady = 10)

    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)

# adds or removes a student from a course (completed)
def GUIeditStudentSchedule(user):

    nWin = tk.Toplevel()
    nWin.title("Link/Unlink Instructor")
    nWin.geometry("1200x800")

    # Adds a student to a course
    def add_student_course():
        # Has the user enter the ID of the student and the CRN of the course they want to add them to
        Win = tk.Toplevel()
        Win.title("Unlink Instructor")
        Win.geometry("1200x800")

        # Student ID
        fNameTitle = tk.Label(Win, text = "Enter the Student's ID")
        studentID = tk.Entry(Win, width = 30)
        fNameTitle.pack(pady = 10)
        studentID.pack(pady = 10)

        # CRN
        lNameTitle = tk.Label(Win, text = "Enter Course CRN")
        CRN = tk.Entry(Win, width = 30)
        lNameTitle.pack(pady = 10)
        CRN.pack(pady = 10)

        def addCourse(studentID, CRN):
            #checks to make sure the student actually exists
            cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (studentID,))
            student = cursor.fetchone()

            if student is None:
                wWin = tk.Toplevel()
                wWin.title("Register Student")
                wWin.geometry("1200x800")
                error = tk.Label(wWin, text = "Student not found")
                error.pack()
                return
        
            #checks to make sure the course actually exists
            cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?""", (CRN,))
            course = cursor.fetchone()

            if course is None:
                wWin = tk.Toplevel()
                wWin.title("Error")
                wWin.geometry("1200x800")
                error = tk.Label(wWin, text = "Course not found")
                error.pack()
                return


            course_columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]


            for i in range(5):
                # Checks to see if student is already enrolled in the course that was entered
                if student[6+i] is CRN:
                    wWin = tk.Toplevel()
                    wWin.title("Register Student")
                    wWin.geometry("1200x800")
                    error = tk.Label(wWin, text = "Student is already enrolled in this course.")
                    error.pack()
                    return

            # Finds the first empty spot in the students schedule
        

            for i in range(5):

                if student[6 + i] is None:

                    cursor.execute(f"""UPDATE STUDENT SET {course_columns[i]} = ? WHERE ID = ?""", (CRN, studentID))
                    conn.commit()
                wWin = tk.Toplevel()
                wWin.title("Register Student")
                wWin.geometry("1200x800")

                message = tk.Label(wWin, text = "Successfully added student " + studentID + " to course " + CRN)
                message.pack()
                return

            # Prints a message that student is already enrolled in max number of courses if there is no empty spot in their schedule
            wWin = tk.Toplevel()
            wWin.title("Register Student")
            wWin.geometry("1200x800")
            error = tk.Label(wWin, text = "Student is already enrolled in 5 courses.")
            error.pack()


            

        btn1 = tk.Button(Win, text = "Submit data", command = lambda: [addCourse(studentID.get(), CRN.get())])
        btn1.pack()
    
        
    # Removes a student from a course
    def remove_student_course():

        # Has the user enter the student ID and the CRN of the course they want to remove the student from
        Win = tk.Toplevel()
        Win.title("Unlink Instructor")
        Win.geometry("1200x800")

        # Student ID
        fNameTitle = tk.Label(Win, text = "Enter the Student's ID")
        studentID = tk.Entry(Win, width = 30)
        fNameTitle.pack(pady = 10)
        studentID.pack(pady = 10)

        # CRN
        lNameTitle = tk.Label(Win, text = "Enter Course CRN")
        CRN = tk.Entry(Win, width = 30)
        lNameTitle.pack(pady = 10)
        CRN.pack(pady = 10)
        
        studentID = studentID.get()
        CRN = CRN.get()

        def removeStudent(studentID, CRN):
            # Checks to make sure the student exists and is enrolled in the selected course then removes them from it
            cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (studentID,))

            if cursor.fetchone() is None:
                wWin = tk.Toplevel()
                wWin.title("Error")
                wWin.geometry("1200x800")
                error = tk.Label(wWin, text = "Student not found")
                error.pack()
                return

            else:
           
                course_columns = ["COURSE_ONE", "COURSE_TWO", "COURSE_THREE", "COURSE_FOUR", "COURSE_FIVE"]

                for column in course_columns:

                    cursor.execute(f"""SELECT * FROM STUDENT WHERE ID = ? AND {column} = ?""", (studentID, CRN))

                    if cursor.fetchone() is not None:

                        cursor.execute(f"""UPDATE STUDENT SET {column} = NULL WHERE ID = ?""", (studentID,))
                        conn.commit()
                        wWin = tk.Toplevel()
                        wWin.title("Success")
                        wWin.geometry("1200x800")
                        error = tk.Label(wWin, text = "Successfully removed student " + studentID + " from course " + CRN)
                        error.pack()
                        return
            wWin = tk.Toplevel()
            wWin.title("Error")
            wWin.geometry("1200x800")
            error = tk.Label(wWin, text = "Student is not enrolled in that course.")
            error.pack()
        btn = tk.Button(Win, text = "Submit Data", command = lambda: [removeStudent(studentID, CRN)])
        btn.pack()

    btn1 = tk.Button(nWin, text = "Add Student to Course", command = add_student_course)
    btn1.pack(pady = 10)
    btn2 = tk.Button(nWin, text = "Remove Student From Course", command = remove_student_course)
    btn2.pack(pady = 10)

    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)
#MODIFY LATER - this will be the main portal the user will interact with based on their role
def open_portal(user):

    if (isinstance(user, Student)):     # student logs into the system
         
        portal = tk.Toplevel()
        portal.title("Student Portal")
        portal.geometry("1280x720")

        # Branding title inside the window
        title_label = tk.Label(portal,
            text="STUDENT PORTAL",
            font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # welcome message
        welcome_label = tk.Label(portal,
            text=f"Welcome {user.first_name}",
            font=("Arial", 12))
        welcome_label.pack(pady=5)

        # creates course search button
        courseSearch_button = tk.Button(portal, text="Course Search", width=40, command=lambda: [portal.destroy(), GUIcourseSearch(user)])
        courseSearch_button.pack (pady=10)

        # creates Add/Drop button
        addDrop_button = tk.Button(portal, text="Add/Drop Course", width=40, command=lambda: [portal.destroy(), GUIaddDrop(user)])  # add drop function not added yet
        addDrop_button.pack (pady=10)

        # creates check conflicts button
        checkConflicts_button = tk.Button(portal, text="Check Conflicts in Schedule", width=40, command=lambda: [portal.destroy(), GUIcheckConflicts(user)])  # check conflict function not added yet
        checkConflicts_button.pack (pady=10)

        # creates print schedule button
        printSchedule_button = tk.Button(portal, text="Print Schedule", width=40, command=lambda: [portal.destroy(), GUIprintSchedule(user)])  # print schedule function not added yet
        printSchedule_button.pack (pady=10)

        # Exit/Logout button
        exit_button = tk.Button(portal, text="Exit", width=20, command=lambda: [portal.destroy(), open_exit_window()])
        exit_button.pack(pady=50)
        
    elif (isinstance (user, Instructor)):       # instructor logs into system
        portal = tk.Toplevel()
        portal.title("Instructor Portal")
        portal.geometry("1280x720")

        title_label = tk.Label(portal,
            text="INSTRUCTOR PORTAL",
            font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # welcome message
        welcome_label = tk.Label(portal,
            text=f"Welcome Professor {user.last_name}",
            font=("Arial", 12))
        welcome_label.pack(pady=5)

        # creates course search button
        courseSearch_button = tk.Button(portal, text="Course Search", width=40, command=lambda: [portal.destroy(), GUIcourseSearch(user)])
        courseSearch_button.pack (pady=10)

        # creates print teaching schedule button
        printTeachSchedule_button = tk.Button(portal, text="Print Teaching Schedule", width=40, command=lambda: [portal.destroy(), GUIprintTeachSchedule(user)])  # print teaching schedule function not added yet
        printTeachSchedule_button.pack (pady=10)

        # creates search student button
        searchStudent_button = tk.Button(portal, text="Search for Student", width=40, command=lambda: [portal.destroy(), GUIsearchStudent(user)])  # search student function not created yet
        searchStudent_button.pack (pady=10)

        # creates print roster button
        printRoster_button = tk.Button(portal, text="Print Roster", width=40, command=lambda: [portal.destroy(), GUIprintRoster(user)])  # print schedule function not added yet
        printRoster_button.pack (pady=10)

        # Exit/Logout button
        exit_button = tk.Button(portal, text="Exit", width=20, command=lambda: [portal.destroy(), open_exit_window()])
        exit_button.pack(pady=50)


    elif (isinstance (user, Admin)):        # admin logs into the system
        portal = tk.Toplevel()
        portal.title("Admin Portal")
        portal.geometry("1280x720")

        title_label = tk.Label(portal,
            text="ADMINISTRATOR PORTAL",
            font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # welcome message
        welcome_label = tk.Label(portal,
            text=f"Welcome {user.title}, {user.first_name} {user.last_name}",
            font=("Arial", 12))
        welcome_label.pack(pady=5)

       # creates course search button
        courseSearch_button = tk.Button(portal, text="Course Search", width=40, command=lambda: [portal.destroy(), GUIcourseSearch(user)])
        courseSearch_button.pack (pady=10)

        # creates add/remove course to system button
        editCourseDB_button = tk.Button(portal, text="Edit Course Database (Add/Remove Course)", width=40, command=lambda: [portal.destroy(), GUIeditCourseDB(user)])   # add/remove courses from DB function not added yet
        editCourseDB_button.pack (pady=10)

        # creates add/remove student to system button
        editStudentDB_button = tk.Button(portal, text="Edit Student Database (Add/Remove Student)", width=40, command=lambda: [portal.destroy(), GUIeditStudentDB(user)])  # add/remove student from DB function not added yet
        editStudentDB_button.pack (pady=10)

        # creates add/remove instructor to system button
        editInstructorDB_button = tk.Button(portal, text="Edit Instructor Database (Add/Remove Instructor)", width=40, command=lambda: [portal.destroy(), GUIeditInstructorDB(user)])  # add/remove instructor from DB function not added yet
        editInstructorDB_button.pack (pady=10)

        # creates Link/Unlink instructor to course button
        linkUnlinkInstructor_button = tk.Button(portal, text="Link/Unlink Instructor to Course", width=40, command=lambda: [portal.destroy(), GUIlinkUnlinkInstructor(user)])  # link/unlink instructor from course function not added yet
        linkUnlinkInstructor_button.pack (pady=10)

        # creates add/remove student from course button
        editStudentSchedule_button = tk.Button(portal, text="Add/Remove Student from Course", width=40, command=lambda: [portal.destroy(), GUIeditStudentSchedule(user)])  # add/remove course from student schedule not added yet
        editStudentSchedule_button.pack (pady=10)

        # Exit/Logout button
        exit_button = tk.Button(portal, text="Exit", width=20, command=lambda: [portal.destroy(), open_exit_window()])
        exit_button.pack(pady=50)

     

   

    # # image logo (optional)
    # try:
    #     image = Image.open("logo.png")
    #     image = image.resize((30, 30))  # small logo size
    #     logo = ImageTk.PhotoImage(image)

    #     # place in top-left corner
    #     logo_label = tk.Label(portal, image=logo)
    #     logo_label.place(x=5, y=5)

    #     # prevent garbage collection
    #     portal.logo = logo
    # except:
    #     pass

def GUIlogin(event=None):
    # get username and PW from user
    username = username_entry.get()
    password = password_entry.get()

    systemUser = login(username, password)

    if systemUser is not None:
        # successful login - open a new window
        window.withdraw()

        # call open portal function to open the correct login window based on the returned user's role
        open_portal(systemUser)

    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username and/or password.")

        #clears password box
        password_entry.delete(0, tk.END)

        #puts cursor back to the beginning of password box
        password_entry.focus()

def GUIcourseSearch(user):
    def searchCourses():
        # get the selected semester, dept, year, and credit values
        selected_semester = selectVal.get()
        selected_dept = selectDept.get()
        selectedYear = selectYear.get()
        credit = credit_entry.get()

        courses = user.course_search(selected_semester)  # call the course_search method with the selected semester
        
        courseList = tk.Listbox(searchWindow, height=25, width=100, activestyle= 'dotbox', font=("Arial", 8))
        courseList.grid(row = 2, column = 1, padx=10, pady=10, sticky='w')

        entry = 1
        for row in courses:
            courseList.insert(entry, row)
            entry += 1

    #initialize the course search window
    searchWindow = tk.Tk()

    searchWindow.title("Course Search")
    searchWindow.geometry("960x540")

    semesters = ['Fall', 'Spring', 'Summer']
    department = ['---', 'ARCH', 'BMED', 'CIVL', 'COMM', 'COMP', 'ELEC', 'ENGR', 'HUMN', 'MECH', 'MGMT', 'PHYS']
    year = ['---', '2030', '2026', '2025']

    credit_label = tk.Label(searchWindow, text="Credits", font=("Arial", 12))
    credit_label.grid(row=3, column=0, padx=10, pady=0)
    credit_entry = tk.Entry(searchWindow, width=10, font=("Arial", 12))
    credit_entry.grid(row=4, column=0, padx=10, pady=10)

    # show semester selection
    selectVal = tk.StringVar(searchWindow)
    selectVal.set(semesters[0])  # default value

    # show dept. selection
    selectDept = tk.StringVar(searchWindow)
    selectDept.set(department[0])  # default value

    # show year selection
    selectYear = tk.StringVar(searchWindow)
    selectYear.set(year[0])  # default value


    # places semester selection box
    defaultParameter = tk.OptionMenu(searchWindow, selectVal, *semesters)
    defaultParameter.grid(row=0, column=0, padx=10, pady=10)

    # places dept. selection box
    searchParameter1 = tk.OptionMenu(searchWindow, selectDept, *department)
    searchParameter1.grid(row=1, column=0, padx=10, pady=10)

    # places year selection box
    searchParameter2 = tk.OptionMenu(searchWindow, selectYear, *year)
    searchParameter2.grid(row=2, column=0, padx=10, pady=10)
    
    # places search button
    search_button = tk.Button(searchWindow, text="Search", command=searchCourses, width= 15, font=("" , 10, "bold"))
    search_button.grid(row=0, column=1, padx=10, pady=10)
    
    # back button
    back_button = tk.Button(searchWindow, text= "Home", command= lambda: [searchWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.grid(row=0, column=2, padx=10, pady=10)

    searchWindow.mainloop()

   

# **************************** start of GUI code that runs this program ************************************* #

# declare the system user as a GLOBAL variable to be used in the functions above
systemUser = None

# ** Login Window ** #
window = tk.Tk()

window.title("Login Portal")
window.geometry("640x360")

#creating label for username box
username_label = tk.Label(window, text="Username: ", font=("Arial", 12))
username_label.grid(row=0, column=0, padx=50, pady=10, sticky="e")

#creating text entry for username box
username_entry = tk.Entry(window, width=30, font=("Arial", 12))
username_entry.grid(row=0, column=1, padx=0, pady=10)

#creating label for password box
password_label = tk.Label(window, text="Password:", font=("Arial", 12))
password_label.grid(row=1, column=0, padx=50, pady=10, sticky="e")

#creating text entry for password box
password_entry = tk.Entry(window, width=30, font=("Arial", 12))
password_entry.grid(row=1, column=1, padx=0, pady=10)

# FOR LATER: note you might want to show the password while you are debugging then add in the show="*"
# once you are satisfied it is working

#creating login button
login_button = tk.Button(window, text="Login", command=GUIlogin, width= 15, font=("" , 10, "bold"))

#login_button.grid(row=2, column=0, columnspan=2, pady=15)
login_button.place(relx=0.5, rely=0.28, anchor=tk.CENTER)

# pressing Enter calls login(). Without this you will always need to click the Login button
window.bind("<Return>", GUIlogin)

# start cursor in username box
username_entry.focus()

# centers the window on the screen
window.eval('tk::PlaceWindow . center')

# run application
window.mainloop()
