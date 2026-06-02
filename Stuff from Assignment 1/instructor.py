# instructor derived class from user class

from user import User

class Instructor(User):
   def __init__(self, firstName, lastName, ID):
       super().__init__(firstName, lastName, ID)

   def courseSearch(self):     # allows the instructor to search for courses [May make this be a part of the base class as all derived classes have it]
        print('*** Running Course Search Function... ***')

   def printSchedule(self):     # allows the instructor to print their schedule
        print('*** Running Print Schedule Function (Instuctor) ***')

   def printClassList(self):    # allows the instructor to print their class list
        print('*** Running Print Class List Function *** ')