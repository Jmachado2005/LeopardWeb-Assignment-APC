import sqlite3

database = sqlite3.connect('assignment3.db')
cursor = database.cursor()

sql_command = """CREATE TABLE IF NOT EXISTS COURSE (
    CRN TEXT PRIMARY KEY,
    TITLE TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    TIME TEXT NOT NULL,
    DAYS_OF_THE_WEEK TEXT NOT NULL,
    SEMESTER TEXT NOT NULL,
    YEAR INTEGER NOT NULL,
    CREDITS INTEGER NOT NULL)
    ;"""

cursor.execute(sql_command)

#adding courses into COURSES table
sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13315', 'Digital Logic', 'BSEE', '8:00AM - 9:15 AM', 'Mon. / Fri.', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13602', 'General Chemistry I', 'BSAS', '9:00 AM - 9:50 AM', 'Mon. / Wed. / Fri.', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13180', 'Computer Science I', 'BCOS' , '10:10 AM - 10:50 AM', 'Mon. / Wed. / Fri.', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('27470', 'Climate Change & The Humanities', 'HUSS', '10:00 AM - 11:45 AM', 'Tue. / Thur.', 'Spring', 2025, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('28225', 'Engineering Thermodynamics I', 'BSME', '2:00 PM - 3:15 PM', 'Mon. / Wed.', 'Spring', 2025, 4);"""
cursor.execute(sql_command)

#adding students into STUDENTS Table
sql_command = """INSERT OR IGNORE INTO STUDENT VALUES('10011', 'Stephen', 'Ellison', 2026, 'BSME', 'ellisons');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES('10012', 'Allyson', 'Burke', 2028, 'HUSS', 'burkea');"""
cursor.execute(sql_command)

#removing 1 instructor from INSTRUCTOR Table
sql_command = """DELETE FROM INSTRUCTOR WHERE ID = 20004;"""
cursor.execute(sql_command)

#updating one of the Admin's titles in ADMIN table
sql_command = """UPDATE ADMIN SET TITLE = 'Vice-President' WHERE ID = 30002;"""
cursor.execute(sql_command)


#queries
print("Lists all courses for Fall 2024")
cursor.execute("""SELECT TITLE, SEMESTER, YEAR FROM COURSE WHERE SEMESTER = 'Fall' AND YEAR = 2024;""")    #ran query in DBViewer - works 
query_result = cursor.fetchall()

print("Lists all courses that are Mon, Wed, Fri")
cursor.execute("""SELECT TITLE, DAYS_OF_THE_WEEK FROM COURSE WHERE DAYS_OF_THE_WEEK = 'Mon. / Wed. / Fri.';""")   #ran query in DBViewer - works
query_result = cursor.fetchall()

print("Lists all courses that are 4 credits")
cursor.execute("""SELECT TITLE, CREDITS FROM COURSE WHERE CREDITS = 4;""")   #ran query in DBViewer - works

print("Lists all courses the DB as well as which professors can teach them in one table")
cursor.exectute("""
SELECT COURSE.TITLE, COURSE.DEPARTMENT, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME
FROM COURSE 
JOIN INSTRUCTOR 
ON COURSE.DEPARTMENT = INSTRUCTOR.DEPT;""")   #ran query in DBViewer - works

database.commit()

database.close()
