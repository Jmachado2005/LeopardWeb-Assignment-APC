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

# USER Table (for GUI)
sql_command = """CREATE TABLE IF NOT EXISTS USER (
    fNAME TEXT NOT NULL,
    lNAME TEXT NOT NULL,
    USERNAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL,
    ROLE INTEGER NOT NULL)
    ;"""

cursor.execute(sql_command)