#contains all the commands to create the database and tables for the LeopardWeb_Project

import sqlite3

database = sqlite3.connect("LeopardWeb_Project.db")
cursor = database.cursor()

# **creating tables**
# STUDENT Table
sql_command = """CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    SURNAME TEXT NOT NULL,
    GRADE_YEAR INTEGER NOT NULL,
    MAJOR TEXT NOT NULL,
    EMAIL TEXT NOT NULL)
    ;"""

cursor.execute(sql_command)

# INSTRUCTOR Table
sql_command = """CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    SURNAME TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    HIRE_YEAR INTEGER NOT NULL,
    DEPT TEXT NOT NULL,
    EMAIL TEXT NOT NULL)
    ;"""

cursor.execute(sql_command)

# ADMIN Table
sql_command = """CREATE TABLE IF NOT EXISTS ADMIN (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    SURNAME TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    OFFICE TEXT NOT NULL,
    EMAIL TEXT NOT NULL)
    ;"""

cursor.execute(sql_command)

# COURSES Table
sql_command = """CREATE TABLE IF NOT EXISTS COURSES (
    CRN TEXT PRIMARY KEY,
    TITLE TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    TIME TEXT NOT NULL,
    DAYS_OF_THE_WEEK TEXT NOT NULL,
    INSTRUCTOR_ID INTEGER,
    SEMESTER TEXT NOT NULL,
    YEAR INTEGER NOT NULL,
    CREDITS INTEGER NOT NULL)
    ;"""

cursor.execute(sql_command)

# LOGIN Table (for GUI)
sql_command = """CREATE TABLE IF NOT EXISTS LOGIN (
    ID INTEGER PRIMARY KEY,
    USERNAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    ROLE INTEGER NOT NULL);"""    #Roles: 1 = Student, 2 = Instructor, 3 = Admin

cursor.execute(sql_command)

# Adding one admin to the ADMIN table and then add them to the LOGIN table

sql_command = """INSERT OR IGNORE INTO ADMIN VALUES(30001, 'Kyla', 'Griffiths', 'Registrar', 'Willston 101', 'registrar@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(30001, 'griffithsk', 'number1registrar', 3);"""
cursor.execute(sql_command)

# Adding 20 students into STUDENTS table and then add them to the LOGIN table
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10001, 'Burt', 'Chance', 2027, 'Applied Science', 'chanceb@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10001, 'chanceb', 'BurtIsDaBest', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10002, 'Fannie', 'Nielson', 2028, 'Information Technology', 'nielsonf@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10002, 'nielsonf', 'AintThatPerculiar28', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10003, 'Maeve', 'Masters', 2029, 'Electromechanical Engineering', 'mastersm@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10003, 'mastersm', 'MasterOfPuppets29', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10004, 'Jones', 'Cowden', 2029, 'Computer Science', 'cowdenj@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10004, 'cowdenj', 'IndianaJones29?', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10005, 'Lloyd', 'Prestron', 2030, 'Mechanical Engineering', 'prestronl@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10005, 'prestonl', 'JC_Superstar30', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10006, 'Allan', 'Cornell', 2030, 'Industrial Design', 'cornella@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10006, 'cornella', 'C0rnellR3jectedM3?', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10007, 'Brigham', 'Rowland', 2030, 'Cybersecurity', 'rowlandb@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10007, 'rowlandb', 'R0wleyJ3fferson', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10008, 'Arthur', 'Courtenay', 2029, 'Computer Information Systems', 'courtenay@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10008, 'courtenaya', 'K1ngArthur29', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10009, 'Gracelyn', 'Smythe', 2028, 'Architecture', 'smytheg@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10009, 'smytheg', 'P1x1eDr3amG1rl', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10010, 'Catherine', 'Sweet', 2030, 'Biomedical Engineering', 'sweetc@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10010, 'sweetc', 'SugarCra5h30', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10011, 'Epiphany', 'Warren', 2026, 'Project Management', 'warrene@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10011, 'warrene', 'Warr3nBuff3t26', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10012, 'Marvin', 'Henley', 2030 , 'Civil Engineering', 'henleym@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10012, 'henleym', 'B0ysOfSumm3r', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10013, 'Tad', 'Irvin', 2026 , 'Information Technology', 'irvint@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10013, 'irvint', 'TadB1tBr0k3', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10014, 'Roman', 'Wade', 2027, 'Climate Resilience', 'wader@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10014, 'wader', 'N0tAWa1t3r', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10015, 'Jessye', 'Backus', 2029, 'Engineering', 'backusj@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10015, 'backusj', 'Walt3rWh1t3!', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10016, 'Pattie', 'Roberson', 2029, 'Computer Science & Society', 'robersonp@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10016, 'robersonp', 'R0b3r0n29', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10017, 'Jaeden', 'Toft', 2026, 'Biological Engineering', 'toftj@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10017, 'toftj', 'T0fuIsYucky26', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10018, 'Becky', 'Easton', 2028, 'Physics', 'eastonb@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10018, 'eastonb', 'W3ston28', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10019, 'Baldric', 'Travers' , 2026, 'Applied Mathematics', 'traversb@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10019, 'traversb', 'IProm1s3ImN0tBald', 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES(10020, 'Sandie', 'Weaver', 2029 , 'Computer Engineering', 'weavers@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(10020, 'weavers', 'IL0veC0mpEng1neer1ng!', 1);"""
cursor.execute(sql_command)

# Adding 15 instructors into INSTRUCTORS table and then add them to the LOGIN table
sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20001, 'Bram', 'Gorbold', 'Dean of SoM', 2020, 'MGMT', 'gorboldb@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20001, 'gorboldb', 'Manag3mt4L1f3', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20002, 'Willie', 'Brewster', 'Visting Professor', 2022, 'HUMN', 'brewsterw@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20002, 'brewsterw', 'IrelandIsMyH0m3', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20003, 'Adrianna', 'Whittaker', 'Associate Dean of SoM', 2021,'MGMT', 'whittakera@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20003, 'whittakera', 'Wh1ttak3r21', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20004, 'Carly', 'Gates', 'Professor' , 2026, 'ARCH', 'gatesc@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20004, 'gatesc@wit.edu', 'P3arlyGat3s', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20005, 'Josslyn', 'Beake', 'Assistant Professor', 2018, 'PHYS', 'beakej@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20005, 'beakej', 'B1rdL0v3r18', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20006, 'Cecilia', 'Berry', 'Associate Dean of SoAD', 2016, 'ARCH', 'berryc@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20006, 'berryc', 'IL0veB3rr1es!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20007, 'Greta', 'Audley', 'Professor', 2012, 'MGMT', 'audleyg@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20007, 'audleyg', 'H0wDar3Y0u!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20008, 'Gwyneth', 'Readdie', 'Associate Professor' , 2016, 'MECH', 'readdieg@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20008, 'readdieg', 'IL1k3B00ks!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20009, 'Lucca', 'Rey', 'Adjunct Learner', 2012, 'COMP', 'reyl@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20009, 'reyl', '$t@rW@rs4L1f3!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20010, 'Joann', 'Strudwick', 'Visiting Professor', 2011, 'COMM', 'strudiwckj@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20010, 'strudwickj', '$trudW1ck!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20011, 'Lyric', 'Savege', 'Adjunct Learner', 2024, 'MGMT', 'saveagel@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20011, 'saveagel', 'Mu$1c4L1f3', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20012, 'Jaylin', 'Boone', 'Dean of SoE', 2012, 'ELEC', 'boonej@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20012, 'boonej', 'SoED3an2012', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20013, 'Dallas', 'Carter', 'Associate Professor', 2017, 'BMED', 'carterd@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20013, 'carterd', 'T3xa$4L1fe!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20014, 'Wiley', 'Grey', 'Associate Professor', 2021, 'ENGR', 'wileyg@wit.edu');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20014, 'wileyg', 'R0b0tsRC00l!', 2);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO INSTRUCTOR VALUES(20015, 'Fable', 'Benbow', 'Visiting Professor', 2025, 'CIVL', 'benbowf');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO LOGIN VALUES(20015, 'benbowf', 'IBu1ldBr1dg3s!', 2);"""
cursor.execute(sql_command)

# Adding 20 courses into COURSES table

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17242', 'Contemporary Art & Theory', 'HUMN', '8:00-9:45 AM', 'T, TH', 20002, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16717', 'Computer Business Applications', 'MGMT', '10:00-11:45 AM', 'T, TH', 20003, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16065', 'Studio I - LAB', 'ARCH', '8:00 - 11:35 AM', 'W, F', 20004, 'Fall', 2026, 6);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16064', 'Studio I - LEC', 'ARCH', '12:00 - 12:50 PM', 'W, F', 20004, 'Fall', 2026, 6);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16942', 'Engineering Physics I', 'PHYS', '8:00 - 9:15 AM', 'T, TH', 20005, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16067', 'Architectual Representation - LEC', 'ARCH', '10:00 - 11:50 AM', 'M', 20006, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16169', 'Architectual Representation - LAB', 'ARCH', '8:00 - 11:30 AM', 'T', 20006, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17276', 'Engineering Thermodynamics', 'MECH', '5:15 - 6:30 PM', 'T, TH', 20008, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17020', 'Computer Science I - LEC', 'COMP', '10:00 - 11:15 AM', 'M, F', 20009, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17021', 'Computer Science I - LAB', 'COMP', '10:00 - 11:45 AM', 'W', 20009, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17229', 'Sound Production', 'COMM', '8:00 - 9:45 AM', 'T, TH', 20010, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16428', 'Digital Logic - LEC', 'ELEC', '8:00 - 9:15 AM', 'M, F', 20012, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('164215', 'Digital Logic - LAB', 'ELEC', '8:00 - 9:45 AM', 'T', 20012, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17256', 'Medical Devices and Systems - LEC', 'BMED', '8:00 - 9:15 AM', 'W, F', 20013, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17257', 'Medical Devices and Systems - LAB', 'BMED', '8:00 - 9:45 AM', 'M', 20013, 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16493', 'Introduction to Engineering - LAB', 'ENGR', '1:00 - 2:45 PM', 'T, TH', 20014 , 'Fall', 2026, 3);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('17150', 'Introduction to Engineering - LEC', 'ENGR', '1:00 - 1:50 PM', 'F', 20014, 'Fall', 2026, 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16308', 'Fluid Mechanics - LEC', 'CIVL', '1:00 - 2:15 PM', 'T, TH', 20015 , 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16310', 'Fluid Mechanics - LAB', 'CIVL', '1:00 - 2:45 PM', 'W', 20015 , 'Fall', 2026, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSES VALUES('16467', 'Computer Architecture', 'ELEC', '8:00 - 9:15 AM', 'T, TH' , 20012, 'Fall', 2026, 3);"""
cursor.execute(sql_command)

database.commit()

database.close()

 