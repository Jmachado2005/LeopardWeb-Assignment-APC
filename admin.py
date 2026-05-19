# admin derived class from user class

from user import User

class Admin(User):
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName, lastName, ID)

    def addCourse(self):    # allows the admin to add a course to the system
        print('*** Running Add Course Function ***')

    def removeCourse(self): # allows the admin to remove a course from the system
        print('*** Running Remove Course Function ***')

    def addUser(self):      # allows the admin to add a user to the system
        print('*** Running Add User Function ***')
        
    def removeUser(self):   # allows the admin to remove a user from the system
        print('*** Running Remove User Function ***')

    def addStudentToCourse(self):   # allows the admin to add a student to a course
        print('*** Running Add Student To Course Function ***')

    def removeStudentFromCourse(self):  # allows the admin to remove a student from the course
        print('*** Running Remove Student From Course Function ***')

    def courseSearch(self):     # allows the admin to search for courses [May make this be a part of the base class as all derived classes have it]
        print('*** Running Search Courses Function ***')

    def rosterSearch(self):     # allows the admin to search a roster
        print('*** Running Search Roster Function ***')

    def printCourse(self):      # allows the admin to print the courses
        print('*** Running Print Course Function ***')

    def printRoster(self):      # allows the admin to print a roster
        print('*** Running Print Roster Function ***')




