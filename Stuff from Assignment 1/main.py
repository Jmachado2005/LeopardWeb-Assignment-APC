#main file that end user will interact with

from user import User
from student import Student
from instructor import Instructor
from admin import Admin

# start the program by prompting user to enter their first name, last name, and WIT ID
fName = input('Please enter your first name: ')
lName = input('Please enter your last name: ')
uID = input("Please enter your WIT ID number including the 'W' at the front: ")

person = User(fName, lName, uID)   #defining a person of class type "User" and sending in values from user

person.printInfo()     # prints user information out in a nice table format

exit = 0
# from there (for now) ask them which role they would like to be (Student, Instructor, or Admin)
while exit != 1:
    print('For testing purposes, please select a role to test out from the list below: ')
    print('[1] - Student')
    print('[2] - Instructor')
    print('[3] - Admin')
    print('[9] - Test User Class Functions')
    print('[0] - Exit Test')
    choice = int(input(f'Choice: '))     # choice gets stored inside the "choice" variable

    print()

    if choice == 1:     # user chooses student
        studentTest = Student(fName, lName, uID)
        print('** You chose: Student **')
        print('Choose one of the following methods to test from the options below:')
        print('[1] - Course Search')
        print('[2] - Course Add/Drop')
        print('[3] - Print Schedule')
        option = int(input(f'Choice: '))    # choice gets stored inside the "option" variable

        if option == 1:
            studentTest.courseSearch()
            print("Test Successful!\n")
        elif option == 2:
            studentTest.courseAddDrop()
            print("Test Successful!\n")
        elif option == 3:
            studentTest.printSchedule()
            print("Test Successful!\n")
        else:
            print('Invalid option. Please try again. \n')

    elif choice == 2:   # user chooses instructor
        instructorTest = Instructor(fName, lName, uID)
        print('** You chose: Intructor **')
        print('Choose one of the following methods to test from the options below:')
        print('[1] - Course Search')
        print('[2] - Print Schedule')
        print('[3] - Print Class List')
        option = int(input(f'Choice: ')) 

        if option == 1:
            instructorTest.courseSearch()
            print("Test Successful!\n")
        elif option == 2:
            instructorTest.printSchedule()
            print("Test Successful!\n")
        elif option == 3:
            instructorTest.printClassList()
            print("Test Successful!\n")
        else:
            print('Invalid option. Please try again.\n')

    elif choice == 3:   # user chooses admin
        adminTest = Admin(fName, lName, uID)
        print('** You chose: Admin **')
        print('Choose one of the following methods to test from the options below:')
        print('[1] - Add Course')
        print('[2] - Remove Course')
        print('[3] - Add User')
        print('[4] - Remove User')
        print('[5] - Add Student To Course')
        print('[6] - Remove Student From Course')
        print('[7] - Course Search')
        print('[8] - Roster Search')
        print('[9] - Print Course')
        print('[10] - Print Roster')
        option = int(input(f'Choice: '))

        if option == 1:
            adminTest.addCourse()
            print("Test Successful!\n")
        elif option == 2:
            adminTest.removeCourse()
            print("Test Successful!\n")
        elif option == 3:
            adminTest.addUser()
            print("Test Successful!\n")
        elif option == 4:
            adminTest.removeUser()
            print("Test Successful!\n")
        elif option == 5:
            adminTest.addStudentToCourse()
            print("Test Successful!\n")
        elif option == 6:
            adminTest.removeStudentFromCourse()
            print("Test Successful!\n")
        elif option == 7:
            adminTest.courseSearch()
            print("Test Successful!\n")
        elif option == 8:
            adminTest.rosterSearch()
            print("Test Successful!\n")
        elif option == 9:
            adminTest.printCourse()
            print("Test Successful!\n")
        elif option == 10:
            adminTest.printRoster()
            print("Test Successful!\n")
        else:
            print('Invalid option. Please try again.\n')

    elif choice == 9:    #user wants to test the User class functions
        print('*** Testing User Class Functions ***')
        print("Choose one of the options below from the user class to test it:")
        print('[1] - setFirstName (allows you to change your first name)')
        print('[2] - setLastName (allows you to change your last name)')
        print('[3] - setID (allows you to change your WIT ID number)')
        print('[4] - View User Information')
        option = int(input(f'Choice: '))

        if option == 1:
            print("\n*** Running setFirstName Function ***")
            person.setFirstName()
        elif option == 2:
            print("\n*** Running setLastName Function ***")
            person.setLastName()
        elif option == 3:
            print("\n*** Running setID Function ***")
            person.setID()
        elif option == 4:
            person.printInfo()
        else:
            print("Invalid option. Please try again\n")


    elif choice == 0:   # user chooses to exit
        print("Exiting program...\n")
        exit = 1        # sets exit to 1, which will break the while loop and end the program
    else:
        print('Invalid choice. Please try again.')

