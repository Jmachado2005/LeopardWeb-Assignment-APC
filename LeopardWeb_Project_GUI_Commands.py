# commands for the GUI

import tkinter as tk
from tkinter import SE, messagebox
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