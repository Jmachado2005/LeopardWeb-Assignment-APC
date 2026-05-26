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

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13315', 'Digital Logic', 'ELEC', '8:00 AM - 9:15 AM', 'Mon. / Fri.', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13602', 'General Chemistry I', 'CHEM', '9:00 AM - 9:50 AM', 'Mon. / Wed. / Fri.', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('13180', 'Computer Science I', 'COMP' , '10:10 AM - 10:50 AM', 'Mon. / Wed. /Fri. ', 'Fall', 2024, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('27470', 'Climate Change & The Humanities', 'HUMN', '10:00 AM - 11:45 AM', 'Tue. / Thur.', 'Spring', 2025, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO COURSE VALUES('28225', 'Engineering Thermodynamics I', 'MECH', '2:00 PM - 3:15 PM', 'Mon. / Wed.', 'Spring', 2025, 4);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES('10011', 'Stephen', 'Ellison', 2026, 'BSME', 'ellisons');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO STUDENT VALUES('10012', 'Allyson', 'Burke', 2028, 'HUSS', 'burkea');"""
cursor.execute(sql_command)

sql_command = """DELETE FROM INSTRUCTOR WHERE ID = 20004;"""
cursor.execute(sql_command)

sql_command = """UPDATE ADMIN SET TITLE = 'Vice-President' WHERE ID = 30002;"""
cursor.execute(sql_command)

sql_command = """SELECT SEMESTER, YEAR FROM COURSE WHERE SEMESTER = 'Fall' AND YEAR = 2024;"""
cursor.execute(sql_command)

database.commit()

database.close()
