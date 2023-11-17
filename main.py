import sqlite3
from sqlite3 import Error

def startMessage():
    print("Welcome to the student information management system! Please input the number of the command you would like to make.")
    print("1. Add/Edit a student entry")
    print("2. Add/Edit a course entry")
    print("3. Add/Edit a score entry")
    user_input = input()
    return user_input
    
def menuSelect(user_input):
    if user_input == "1":
        print("\u0332".join("Students"))
        print("Please select a command:")
        print("1. Add a new student")
        print("2. Edit a current student")
        print("3. View all student entries")
        user_input = input()
        if user_input == "1":
            addStudent()
        elif user_input == "2":
            editStudent()
    elif user_input == "2":
        print("\u0332".join("Courses"))
        print("Please select a command:")
        print("1. Add a new course")
        print("2. Edit a current course")
        print("3. View all course entries")
        user_input = input()
        if user_input == "1":
            addCourse()
        elif user_input == "2":
            editCourse()
    elif user_input == "3":
        print("\u0332".join("Scores"))
        print("Please select a command:")
        print("1. Add a new score")
        print("2. Edit a current score")
        print("3. View all score entries")
        user_input = input()
        if user_input == "1":
            addScore()
        elif user_input == "2":
            editScore()
    else:
        print("Invalid command")
        user_input = input()
        menuSelect(user_input)
        return 
    
def addStudent():
    newEntry = []
    condition = True
    print("Please enter the following information for new student entry:")
    print("First Name:")
    while(condition):
        user_input = input()
        if user_input.isalpha():
            user_input.capitalize()
            newEntry.append(user_input)
            condition = False
        else:
            print("Name must contain alphabetic characters only.")
    condition = True
    print("Last Name:")
    while(condition):
        user_input = input()
        if user_input.isalpha():
            user_input.capitalize()
            newEntry.append(user_input)
            condition = False
        else:
            print("Name must contain alphabetic characters only.")
    condition = True
    print("Grade(1 - 6):")
    while(condition):
        user_input = input()
        if user_input.isnumeric() == True:
            user_input = int(user_input)
            if user_input >= 1 and user_input <= 6:
                newEntry.append(user_input)
                condition = False
            else:
                print("Grade must be between 1st and 6th.")
        else:
            print("Grade must be numerical.")
    condition = True
    print("Sex(M/F):")
    while(condition):
        user_input = input()
        user_input = user_input.lower()
        if user_input == "m" or user_input == "male":
            user_input = "M"
            newEntry.append(user_input)
            condition = False
        elif user_input == "f" or user_input == "female":
            user_input = "F"
            newEntry.append(user_input)
            condition = False
        else:
            print("Sex must be male or female.")
    values = ", ".join(f"'{value}'" for value in newEntry)
    executeQuery(connection, create_student+"("+values+")")
    print("Student entry added!")
            
    
    
    
    
def editStudent():
    print("WIP")
    
def addCourse():
    print("WIP")
    
def editCourse():
    print("WIP")
    
def addScore():
    print("WIP")

def editScore():
    print("WIP")  
    
def createConnection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred.")     
    return connection

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred.")

connection = createConnection("./student_info.sqlite")
create_students_table = """
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    grade INTEGER,
    sex TEXT
);
"""

create_student = """
INSERT INTO
    students (fname, lname, grade, sex)
VALUES

"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
"""

create_course = """
INSERT INTO
    courses (name)
VALUES
"""

create_scores_table = """
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    score INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
"""

create_score = """
INSERFT INTO
    scores (student_id, course_id, score)
VALUES
"""

executeQuery(connection, create_students_table)
executeQuery(connection, create_courses_table)
executeQuery(connection, create_scores_table)

user_input = startMessage()
user_input = menuSelect(user_input)
