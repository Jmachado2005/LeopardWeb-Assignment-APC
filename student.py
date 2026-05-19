# student derived class from user class
from user import User

class Student(User):
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName, lastName, ID)   #super() allows the student class to access the user class's attributes

    def courseSearch(self):     # allows the student to search for courses [May make this be a part of the base class as all derived classes have it]
        print('*** Running Course Search Function... ***')

    def courseAddDrop(self):    # allows the student to add/drop courses
        print('*** Runnin Add/Drop Course Function ***')

    def printSchedule(self):    # allows the student to see and print their schedule
        print('*** Running Print Schedule Function (Student) ***')