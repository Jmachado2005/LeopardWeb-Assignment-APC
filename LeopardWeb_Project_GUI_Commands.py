# commands for the GUI

import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.font import BOLD
# from PTL import Image, ImageTk
from LeopardWeb_Project_Functions import login
from LeopardWeb_Project_Classes_and_Objects import Course, User, Student, Instructor, Admin

conn = sqlite3.connect("LeopardWeb_Project.db")
cursor = conn.cursor()

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
        addDrop_button = tk.Button(portal, text="Add/Drop Course", width=40, command=lambda: [portal.destroy(), GUIaddDrop(user)])
        addDrop_button.pack (pady=10)

        # creates print schedule button
        printSchedule_button = tk.Button(portal, text="Print Schedule", width=40, command=lambda: [portal.destroy(), GUIprintSchedule(user)])
        printSchedule_button.pack (pady=10)

        # creates check conflicts button
        checkConflicts_button = tk.Button(portal, text="Check Conflicts in Schedule", width=40, command=lambda: [portal.destroy(), GUIcheckConflicts(user)])
        checkConflicts_button.pack (pady=10)

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

def GUIforgotPW():
    def show_password(username):
        if (username is None or username == ""):
            messagebox.showerror("Error", "Please enter a username.")
            return
        else:
            # gets the password for the given username and displays it in a messagebox
            cursor.execute("""SELECT PASSWORD FROM LOGIN WHERE USERNAME = ?""", (username,))
            password = cursor.fetchone()

            messagebox.showinfo("Current Password", f"The password for {username} is: {password}")

    def reset_password(username):
        if username is None or username == "":
            messagebox.showerror("Error", "Please enter a username.")
            return
        else: 
            # gets the new password from the user and updates it in the database
            new_password = tk.simpledialog.askstring("Reset Password", "Enter your new password:")
            cursor.execute("""UPDATE LOGIN SET PASSWORD = ? WHERE USERNAME = ?""", (new_password, username))
            conn.commit()
            messagebox.showinfo("Password Reset", f"The password for {username} has been reset to {new_password}.")

    forgotPWWindow = tk.Toplevel()
    forgotPWWindow.title("Forgot Password")
    forgotPWWindow.geometry("600x400")

    # creates a label for the username entry
    username_label = tk.Label(forgotPWWindow, text="Enter your username:", font=("Arial", 12))
    username_label.pack(pady=10)

    # create an entry for the username
    username_entry = tk.Entry(forgotPWWindow, width=30, font=("Arial", 12))
    username_entry.pack(pady=10)

    # creates a button to show the user their password
    showPW_button = tk.Button(forgotPWWindow, text="Show Current Password", command=lambda: show_password(username_entry.get()), width=30, font=("", 10, "bold"))
    showPW_button.pack(pady=10)

    # create a button to reset the password
    submit_button = tk.Button(forgotPWWindow, text="Reset Password", command=lambda: reset_password(username_entry.get()), width=30, font=("", 10, "bold"))
    submit_button.pack(pady=10)

    # creates a button to go back to login screen
    return_button = tk.Button(forgotPWWindow, text="Return to Login", command=forgotPWWindow.destroy, width=20, font=("", 10))
    return_button.pack(pady=30)

    forgotPWWindow.mainloop()

def GUIabout():
    aboutWindow = tk.Toplevel()
    aboutWindow.title("About Project")
    aboutWindow.geometry("500x300")

    # create a label for the about information
    about_label = tk.Label(aboutWindow, text="LeopardWeb - Course Registration System", font=("Arial", 14, "bold"))
    about_label.pack(pady=10)

    # create a label for group members
    members_label = tk.Label(aboutWindow, text="Project By: Harrison Brown, Joe Machado, & David Vozzo", font=("Arial", 12))
    members_label.pack(pady=10)

    # create a button to go back to login screen
    return_button = tk.Button(aboutWindow, text="Return to Login", command=aboutWindow.destroy, width=20, font=("", 10))
    return_button.pack(pady=10)

    aboutWindow.mainloop()

def GUIcourseSearch(user):
    def searchCourses():
        # get the selected semester, dept, year, and credit values
        selected_semester = selectVal.get()
        selected_dept = selectDept.get()
        selectedYear = selectYear.get()
        credit = credit_entry.get()

        if selected_dept == '---' and selectedYear == '---' and credit == '':
            courses = user.course_search(selected_semester)  # call the course_search method with the selected semester
        else:
            courses = user.parameter_search(selected_semester, selected_dept, selectedYear, credit)  # call the parameter_search method with the selected parameters
        
        courseList = tk.Listbox(searchWindow, height=25, width=100, activestyle= 'dotbox', font=("Arial", 8))
        courseList.grid(row = 2, column = 2, padx=10, pady=10, sticky='w')

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

# *** Joe's Work Starts here ***

def GUIaddDrop(user):
    def addDrop():
        choice = showOption.get()
        crnNum = CRN_entry.get()

        confirmation = user.addDrop_course(choice, crnNum, user.wit_ID)

        print(f"Add/Drop ran successfully! Value: {confirmation}")

        # prints the appropriate message to the bottom part of the window based on what was returned from add drop methood
        if (confirmation == 0):     # ADD: no course w/ entered CRN exists in system
            addDropMsg = tk.Message(addDropWindow, text="Course does not exist in database. Please try again", font=("Arial", 12))
            addDropMsg.grid(row=2, column=0, padx=10, pady=0)
        elif (confirmation == 1):   # ADD: course was added to schedule
            addDropMsg = tk.Message(addDropWindow, text="Course has been added to your schedule!", font=("Arial", 12))
            addDropMsg.grid(row=2, column=0, padx=10, pady=0)
        elif (confirmation == 2):   # ADD: max amt off courses in student schedule
            addDropMsg = tk.Message(addDropWindow, text="Maximum amount of courses reached! You cannot add any more to your schedule", font=("Arial", 12))
            addDropMsg.grid(row=2, column=0, padx=10, pady=0)
        elif (confirmation == 3):   # DROP: 
            addDropMsg = tk.Message(addDropWindow, text="This course is not in your schedule. Try Again", font=("Arial", 12))
            addDropMsg.grid(row=2, column=0, padx=10, pady=0)
        elif (confirmation == 4):
            addDropMsg = tk.Message(addDropWindow, text="Course has been removed from your schedule!", font=("Arial", 12))
            addDropMsg.grid(row=2, column=0, padx=10, pady=0)

    #initialize the add/drop window
    addDropWindow = tk.Tk()

    addDropWindow.title("Add/Drop")
    addDropWindow.geometry("720x480")

    option = ['Select Option Here', 'Add', 'Drop']

    # creates a label for the option
    option_label = tk.Label(addDropWindow, text="Selection:", font=("Arial", 12))
    option_label.grid(row=0, column=0, padx=10, pady=10)

    # puts in add/drop options inside menu + shows the dropdown menu
    showOption = tk.StringVar(addDropWindow)
    showOption.set(option[0])  # default value
    addDropSelection = tk.OptionMenu(addDropWindow, showOption, *option)
    addDropSelection.grid(row=1, column=0, padx=10, pady=0)


    # creates a label for CRN entry
    CRN_label = tk.Label(addDropWindow, text="CRN Entry", font=("Arial", 12))
    CRN_label.grid(row=0, column=1, padx=10, pady=10)
  
    # puts in text entry for CRN entry
    CRN_entry = tk.Entry(addDropWindow, width=10, font=("Arial", 12))
    CRN_entry.grid(row=1, column=1, padx=10, pady=10)


    # creates a label for confirm button
    confirm_label = tk.Label(addDropWindow, text="Confirm?", font=("Arial", 12))
    confirm_label.grid(row=0, column=2, padx=10, pady=10)
    

    # creates button to confirm that user wants to add/drop course
    confirm_button = tk.Button(addDropWindow, text="Yes, Confirm", command=addDrop, width= 15, font=("" , 10))
    confirm_button.grid(row=1, column=2, padx=10, pady=10)


    # home button to go back to main portal
    back_button = tk.Button(addDropWindow, text= "Home", command= lambda: [addDropWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.grid(row=1, column=3, padx=10, pady=10)

    addDropWindow.mainloop() 

def GUIprintSchedule(user):
    def printStudentSchedule():
        schedule = user.print_schedule(user.first_name)      # call the print schedule method

        studentSchedule = tk.Listbox(printSchWindow, height=25, width=100, activestyle= 'dotbox', font=("Arial", 8))
        studentSchedule.grid(row = 1, column = 0, padx=10, pady=10, sticky='s')

        entry = 1
        for row in schedule:
            studentSchedule.insert(entry, row)
            entry += 1

    #initialize the check window
    printSchWindow = tk.Tk()

    printSchWindow.title("Print Schedule")
    printSchWindow.geometry("960x540")

    # creates a label to show the student's schedule
    schedule_label = tk.Label(printSchWindow, text="Your Schedule:", font=("Arial", 14))
    schedule_label.grid(row=0, column=0, padx=10, pady=10)

    # calls printStudentSchedule function to show student their schedule
    printStudentSchedule()

    # home button to go back to main portal
    back_button = tk.Button(printSchWindow, text= "Home", command= lambda: [printSchWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.grid(row=0, column=2, padx=10, pady=10)

    printSchWindow.mainloop()

def GUIcheckConflicts(user):
    def checkConflicts():
        schedule = user.print_schedule(user.first_name)      # calls the print schedule method (like before)

        studentSchedule = tk.Listbox(checkConfWindow, height=25, width=100, activestyle= 'dotbox', font=("Arial", 8))
        studentSchedule.grid(row = 1, column = 0, padx=10, pady=10, sticky='s')

        entry = 1
        for row in schedule:
            studentSchedule.insert(entry, row)
            entry += 1

        # code to show if conflicts detected are here
        duplicateDetect = user.check_conflicts(user.wit_ID)

        # DEBUGGING: print(f"sucessfully checked for dupes. Value: {duplicateDetect}")

        if (duplicateDetect == 1):  # duplicate detected
            duplicateMsg = tk.Message(checkConfWindow, text="ATTENTION: Student has duplicate courses in their schedule!", font=("Arial", 12))
            duplicateMsg.grid(row=3, column=0, padx=10, pady=0)
        elif (duplicateDetect == 0):
            duplicateMsg = tk.Message(checkConfWindow, text="No Duplicates Found In Schedule!", font=("Arial", 12))
            duplicateMsg.grid(row=3, column=0, padx=10, pady=10)

    #initialize the check window
    checkConfWindow = tk.Tk()

    checkConfWindow.title("Check Conflicts")
    checkConfWindow.geometry("960x540")

    # creates a label to show the student's schedule
    schedule_label = tk.Label(checkConfWindow, text="Your Schedule:", font=("Arial", 14))
    schedule_label.grid(row=0, column=0, padx=10, pady=10)

    # calls printStudentSchedule function to show student their schedule
    checkConflicts()

    # home button to go back to main portal
    back_button = tk.Button(checkConfWindow, text= "Home", command= lambda: [checkConfWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.grid(row=0, column=2, padx=10, pady=10)


# *** Harrison's Work Starts here ***

def GUIprintTeachSchedule(user):
    scheduleWindow = tk.Tk()

    scheduleWindow.title("Teaching Schedule")
    scheduleWindow.geometry("960x540")

    scheduleLabel = tk.Label(scheduleWindow, text="Teaching Schedule", font=("Arial", 12, "bold"))
    scheduleLabel.place(relx=0.26, rely=0.13, anchor=tk.CENTER)

    schedule = tk.Listbox(scheduleWindow, height = 25, width = 100, activestyle= 'dotbox', font=("Arial", 8))
    schedule.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

    back_button = tk.Button(scheduleWindow, text= "Home", command= lambda: [scheduleWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.place(relx=0.9, rely=0.08, anchor=tk.CENTER)

    courseSchedule = user.print_teaching_schedule()

    entry = 1
    for row in courseSchedule:
        schedule.insert(entry, row)
        entry += 1

    scheduleWindow.mainloop()
    
def GUIsearchStudent(user):

    def studentSearch():
        CRN = selectVal.get()
        ID = studentID.get()
        studentInfo = user.search_student(ID, CRN)
        searchMessage.delete(0, tk.END)  # Clear the listbox before inserting new data
        if studentInfo is not None:
            searchMessage.insert(1, "Student Found to be Enrolled in This Course.")
        else:
            searchMessage.insert(1, "Student Not Found to be Enrolled in This Course.")
    searchStudentWindow = tk.Tk()

    searchStudentWindow.title("Student Search")
    searchStudentWindow.geometry("960x540")

    rosterLabel = tk.Label(searchStudentWindow, text="Confirmation Message", font=("Arial", 12, "bold"))
    rosterLabel.place(relx=0.26, rely=0.13, anchor=tk.CENTER)

    searchMessage = tk.Listbox(searchStudentWindow, height = 15, width = 75, activestyle= 'dotbox', font=("Arial", 8))
    searchMessage.place(relx = 0.4, rely = 0.37, anchor = tk.CENTER)

    back_button = tk.Button(searchStudentWindow, text= "Home", command= lambda: [searchStudentWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.place(relx=0.9, rely=0.08, anchor=tk.CENTER)

    courseCRNs = []
    selectVal = tk.StringVar(searchStudentWindow)

    courses = user.print_teaching_schedule()
    for course in courses:
        courseCRNs.append(course[0])

    courseSelection = tk.OptionMenu(searchStudentWindow, selectVal, *courseCRNs)
    courseSelection.grid(row=0, column=0, padx=10, pady=10)

    idLabel = tk.Label(searchStudentWindow, text="Student ID:", font=("Arial", 12))
    idLabel.grid(row=0, column=1, padx=5, pady=10)

    studentID = tk.Entry(searchStudentWindow, width=15, font=("Arial", 12))
    studentID.grid(row=0, column=2, padx=10, pady=10)

    search_button = tk.Button(searchStudentWindow, text="Search", command=studentSearch, width= 15, font=("" , 10, "bold"))
    search_button.grid(row=0, column=3, padx=10, pady=10)

    searchStudentWindow.mainloop()

def GUIprintRoster(user):
    def getRoster():
        CRN = selectVal.get()
        courseRoster = user.print_roster(CRN)
        roster.delete(0, tk.END)  # Clear the listbox before inserting new data
        entry = 1
        for row in courseRoster:
            roster.insert(entry, row)
            entry += 1

    printRosterWindow = tk.Tk()

    printRosterWindow.title("Course Rosters")
    printRosterWindow.geometry("960x540")

    rosterLabel = tk.Label(printRosterWindow, text="Course Roster", font=("Arial", 12, "bold"))
    rosterLabel.place(relx=0.26, rely=0.13, anchor=tk.CENTER)

    roster = tk.Listbox(printRosterWindow, height = 25, width = 100, activestyle= 'dotbox', font=("Arial", 8))
    roster.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

    back_button = tk.Button(printRosterWindow, text= "Home", command= lambda: [printRosterWindow.destroy(), open_portal(user)], width= 15, font=("" , 10, "bold"))
    back_button.place(relx=0.9, rely=0.08, anchor=tk.CENTER)

    courseCRNs = []
    selectVal = tk.StringVar(printRosterWindow)

    courses = user.print_teaching_schedule()
    for course in courses:
        courseCRNs.append(course[0])

    courseSelection = tk.OptionMenu(printRosterWindow, selectVal, *courseCRNs)
    courseSelection.grid(row=0, column=0, padx=10, pady=10)

    search_button = tk.Button(printRosterWindow, text="Print", command=getRoster, width= 15, font=("" , 10, "bold"))
    search_button.grid(row=0, column=1, padx=10, pady=10)

    printRosterWindow.mainloop()
   

# *** David's Work Starts here ***

def GUIeditCourseDB(user):      # edit courses database
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
     
        cursor.execute("""SELECT * FROM COURSES WHERE CRN = ?;""", (CRN,),)
        check = cursor.fetchone()
        if (time == "" or CRN == "" or title == "" or dep == "" or DoW == "" or semester == "" or year == "" or credit == ""):
            win = tk.Toplevel()
            win.title("Error")
            win.geometry("600x300")

            error = tk.Label(win, text = "Error creating course. One or more data entries empty")
            error.pack()
        elif(check != None):
            win = tk.Toplevel()
            win.title("Error")
            win.geometry("600x300")

            error = tk.Label(win, text = "CRN already exists")
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

def GUIeditStudentDB(user):     # edit student database
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

def GUIeditInstructorDB(user):  # edit instructor 
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


    nWin = tk.Toplevel()
    nWin.title("Link/Unlink Instructor")
    nWin.geometry("1200x800")




    def linkInstructor():
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

def GUIlinkUnlinkInstructor(user):  # link/unlink instructor from course
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

def GUIeditStudentSchedule(user):   # edit student schedule

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
        btn = tk.Button(Win, text = "Submit Data", command = lambda: [removeStudent(studentID.get(), CRN.get())])

    btn1 = tk.Button(nWin, text = "Add Student to Course", command = add_student_course)
    btn1.pack(pady = 10)
    btn2 = tk.Button(nWin, text = "Remove Student From Course", command = remove_student_course)
    btn2.pack(pady = 10)

    exitBtn = tk.Button(nWin, text = "Return to Portal", command = lambda: [nWin.destroy(), open_portal(user)])
    exitBtn.pack(pady = 10)
   

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
password_entry = tk.Entry(window, width=30, font=("Arial", 12), show="*")
password_entry.grid(row=1, column=1, padx=0, pady=10)

#creating login button
login_button = tk.Button(window, text="Login", command=GUIlogin, width= 15, font=("" , 10, "bold"))
login_button.place(relx=0.5, rely=0.28, anchor=tk.CENTER)

# creating the "Forgot Password?" button
forgotPW_button = tk.Button(window, text="Forgot Password/Reset Password", command=GUIforgotPW, width= 30, font=("Arial", 10, "bold"))
forgotPW_button.place(relx=0.5, rely=0.38, anchor=tk.CENTER)

# creating a "Help" button
help_button = tk.Button(window, text = "Help", command=lambda: messagebox.showinfo("Help", "Please refer to the user manual for instructions on how to use this program."), width= 15, font=("Arial", 10, "bold"))
help_button.place(relx=0.5, rely=0.48, anchor=tk.CENTER)

# creating the "About" button
about_button = tk.Button(window, text="About", command=GUIabout, width= 10, font=("Arial", 10, "bold"))
about_button.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

# pressing Enter calls login(). Without this you will always need to click the Login button
window.bind("<Return>", GUIlogin)

# start cursor in username box
username_entry.focus()

# centers the window on the screen
window.eval('tk::PlaceWindow . center')

# run application
window.mainloop()
