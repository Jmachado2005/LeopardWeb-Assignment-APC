#base user class
class User:
 
    def __init__(self, firstName, lastName, ID):    #declaration of class
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID

    def setFirstName(self):     # lets user override their first name they entered at the beginning of the program
        print(f'Your current first name is: {self.firstName}')
        print('What would you like to change it to?')
        self.firstName = input('New first name: ')
        print(f'Successfully updated firstName attribute to: {self.firstName}\n')

    def getFirstName(self):   # prints value stored in firstName attribute
        return(self.firstName)
        
    def setLastName(self):  # lets user overide their last name they entered at the beginning of the program
        print(f'Your current last name is: {self.lastName}')
        print('What would you like to change it to?')
        self.lastName = input('New last name: ')
        print(f'Successfully updated lastName attribute to: {self.lastName}\n')

    def getLastName(self):  # prints value stored in lastName attribute
        return(self.lastName)
    
    def setID(self):    # lets user overide their WIT ID number they entered at the start of the program
        print(f'Your current ID number is: {self.ID}')
        print("What would you like to change it to (don't forget to add the 'W')?")
        self.ID = input('New ID number: ')
        print(f'Successfully updated ID attribute to: {self.ID}\n')

    def getID(self):    # prints user's ID
        return(self.ID)

    def printInfo(self):    # prints all info on user
        print()
        print('*** Information *** ')
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"WIT ID: {self.ID}")
        print()
