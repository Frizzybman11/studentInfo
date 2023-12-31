import sqlite3
from sqlite3 import Error
from os import system, name

class Format:
    end = '\033[0m'
    underline = '\033[4m'

def startMessage():
    clear()
    print("Welcome to the student information system! Please input the number of the menu you would like to enter.")
    print("1. Students")
    print("2. Courses")
    print("3. Scores")
    user_input = input()
    menuSelect(user_input)
    return
    
def menuSelect(user_input):
    clear()
    if user_input == "1":
        print(Format.underline + "Students" + Format.end)
        print("1. Add a new student")
        print("2. Edit a current student")
        print("3. View student entries")
        print("4. Remove a student")
        print("5. Return to main menu")
        user_input = input()
        if user_input == "1":
            clear()
            addStudent()
        elif user_input == "2":
            clear()
            editStudent()
        elif user_input == "3":
            clear()
            viewStudents()
        elif user_input == "4":
            clear()
            removeStudent()
        elif user_input == "5":
            user_input = startMessage()
            return
    elif user_input == "2":
        print(Format.underline + "Courses" + Format.end)
        print("1. Add a new course")
        print("2. Edit a current course")
        print("3. View course entries")
        print("4. Remove a course")
        print("5. Return to main menu")
        user_input = input()
        if user_input == "1":
            clear()
            addCourse()
        elif user_input == "2":
            clear()
            editCourse()
        elif user_input == "3":
            clear()
            viewCourses()
        elif user_input == "4":
            clear()
            removeCourse()
        elif user_input == "5":
            user_input = startMessage()
            return
    elif user_input == "3":
        print(Format.underline + "Scores" + Format.end)
        print("1. Add a new score")
        print("2. Edit a current score")
        print("3. View score entries")
        print("4. Remove a score")
        print("5. Return to main menu")
        user_input = input()
        if user_input == "1":
            addScore()
        elif user_input == "2":
            editScore()
        elif user_input == "3":
            viewScores()
        elif user_input == "4":
            removeScore()
        elif user_input == "5":
            user_input = startMessage()
            return
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
            user_input = user_input.capitalize()
            newEntry.append(user_input)
            condition = False
        else:
            print("Name must contain alphabetic characters only.")
    condition = True
    print("Last Name:")
    while(condition):
        user_input = input()
        if user_input.isalpha():
            user_input = user_input.capitalize()
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
    print("Student entry added! Add another student? (y/n)")
    user_input = input()
    user_input = user_input.lower()
    if user_input == "y" or user_input == "yes":
        clear()
        addStudent()
        return
    else:
        user_input = "1"
        clear()
        menuSelect(user_input)
        return
               
    
def editStudent():
    condition = True
    print("Please enter a student ID to edit entry. For a list of students, type 'view'. To return, type 'return'.")
    while(condition):
        user_input = input()
        if user_input.isalpha():
            user_input = user_input.lower()
            if user_input == "view" or user_input == "v":
                clear()
                editStudentView()
                print("Please enter a student ID to edit entry. To return, type 'return'.")
                user_input = input()
                if user_input.isnumeric():
                    editStudentQuery(user_input)
                    condition = False
                    return
                elif user_input == "return" or user_input == "r":
                    menuSelect("1")
                    condition = False
                    return
                else:
                    print("Please enter a student ID number.")
            elif user_input == "return" or user_input == "r":
                menuSelect("1")
                condition = False
                return
            else:
                print("Please enter a student ID to edit entry. For a list of students, type 'view'")
        elif user_input.isnumeric():
            editStudentQuery(user_input)
            condition = False
            return  
        else:
            print("Please enter a student ID to edit entry. For a list of students, type 'view'")
            
def editStudentView():
    select_students = "SELECT * from students"
    students = executeReadQuery(connection, select_students)
    for student in students:
        print(student)
    return
                                       
def editStudentQuery(user_input):
    first_name = ""
    last_name = ""
    grade = ""
    sex = ""
    query_list = []
    student_entry = []
    update_student = ""
    condition = True
    if user_input.isnumeric():
        select_student = "SELECT * FROM students WHERE id = " + user_input
        student = executeReadQuery(connection, select_student)
        for entry in student:
            student_entry = entry
        print("First Name: " + student_entry[1])
        print("Last Name: " + student_entry[2])
        print("Grade: " + str(student_entry[3]))
        print("Sex: " + student_entry[4])
        print("For each field, enter new data. Leave blank to keep the same")
        print("First Name: ")
        while(condition):
            user_input = input()
            if len(user_input) == 0:
                first_name = student_entry[1]
                condition = False
            elif not user_input.isalpha():
                print("Name must contain alphabetic characters only.")
            else:
                user_input = user_input.capitalize()
                first_name = user_input
                condition = False
        print("Last Name: ")
        condition = True
        while(condition):
            user_input = input()
            if len(user_input) == 0:
                last_name = student_entry[2]
                condition = False
            elif not user_input.isalpha():
                print("Name must contain alphabetic characters only.")
            else:
                user_input = user_input.capitalize()
                last_name = user_input
                condition = False
        print("Grade: ")
        condition = True
        while(condition):
            user_input = input()
            if len(user_input) == 0:
                grade = student_entry[3]
                condition = False
            elif user_input.isnumeric():
                user_input = int(user_input)
                if not user_input >= 1 and not user_input <= 6:
                    print("Grade must be between 1st and 6th.")
                elif user_input:
                    grade = user_input
                    condition = False
                else:
                    grade = student_entry[3]
                    condition = False
            else: 
                print("Grade must be numerical.")
        print("Sex: ")
        condition = True
        while(condition):
            user_input = input()
            if len(user_input) == 0:
                sex = student_entry[4]
                condition = False
            elif user_input.isalpha():
                user_input = user_input.lower()
                if user_input == "m" or user_input == "male":
                    sex = "M"
                    condition = False
                elif user_input == "f" or user_input == "female":
                    sex = "F"
                    condition = False
                elif user_input:
                    print("Sex must be male or female.")
                else:
                    sex = student_entry[4]
                    condition = False     
            else:
                print("Sex must be male or female.")
        update_student = """
        UPDATE
            students
        SET
            fname = """ + '"' + first_name + '"' """,
            lname = """ + '"' + last_name + '"' """,
            grade = """ + '"' + str(grade) + '"' """,
            sex = """ + '"' + sex + '"' """
        WHERE
            id = """ + str(student_entry[0]) + """
        """
        try:
            executeQuery(connection, update_student)
            print("Entry updated successfully!")
            print("Press enter to return")
            input()
            menuSelect("1")
            return
        except Error as e:
            print(f"The error '{e}' occurred.")

def removeStudent():
    condition = True
    print("Please enter a student ID for removal. For a list of students, type 'view'. To return, type 'return'.")
    while(condition):
        user_input = input()
        if user_input.isalpha():
            user_input = user_input.lower()
            if user_input == "view" or user_input == "v":
                viewStudents()
                print("Please enter a student ID.")
                user_input = input()
                if user_input.isnumeric():
                    removeStudentQuery(user_input)
                    condition = False
                    return
                else:
                    print("Please enter a student ID number.")
            elif user_input == 'return' or user_input =='r':
                menuSelect("1")
                condition = False
                return
            else:
                print("Please enter a student ID. For a list of students, type 'view'")
        elif user_input.isnumeric():
            removeStudentQuery(user_input)
            condition = False
            return  
        else:
            print("Please enter a student ID. For a list of students, type 'view'")
    
def removeStudentQuery(user_input):
    student_id = user_input
    select_students = "SELECT * from students WHERE id = "
    students = executeReadQuery(connection, select_students + student_id)
    for student in students:
        print(student)
    print("Are you sure you wish to remove this student entry? (y/n)")
    user_input = input()
    if user_input == "y" or user_input == "yes":
        delete_student = "DELETE FROM students WHERE id = "
        executeQuery(connection, delete_student + student_id)
        print("Student entry removed!")
        print("Press enter to return")
        input()
        menuSelect("1")
        return
    else:
        print("Removal cancelled.")
        print("Press enter to return")
        input()
        menuSelect("1")
        return                   
    
def viewStudents():
    print("To view all students, press enter. To view a specific grade, enter grade number. To return, type 'return'.")
    condition = True
    user_input = input()
    while(condition):
        if user_input == "return" or user_input == "r":
            menuSelect("1")
            condition = False
            return
        elif user_input.isnumeric():
            if int(user_input) >= 1 and int(user_input) <= 6:
                viewStudentsQuery(user_input)
                condition = False
                return
            else:
                print("Grade must be between 1st and 6th.")
        else:
            viewStudentsQuery(user_input)
            condition = False
            return
                
    
def viewStudentsQuery(user_input):
    if user_input.isnumeric():
        grade = user_input
        select_students = "SELECT * from students WHERE grade = "
        select_students = select_students + grade
        students = executeReadQuery(connection, select_students)
    else:
        select_students = "SELECT * from students"
        students = executeReadQuery(connection, select_students)
    if students:    
        for student in students:
            print(student)
    else:
        print("No students found.")
    print("To view sort commands, type 'sort'. To return, type 'return', or leave input blank and press enter.")
    condition = True
    while(condition):
        user_input = input()
        if user_input == "sort" or user_input == "s":
            print("Input sort command:")
            print("- id (default)")
            print("- first : First Name (Ascending)")
            print("- dfirst : First Name (Descending)")
            print("- last : Last Name (Ascending)")
            print("- dlast : Last Name (Descending)")
        elif user_input == "id":
            select_students_end = " ORDER BY id ASC"
            students = executeReadQuery(connection, select_students + select_students_end)
            for student in students:
                print(student)
        elif user_input == "first" or user_input == "f":
            select_students_end = " ORDER BY fname ASC"
            students = executeReadQuery(connection, select_students + select_students_end)
            for student in students:
                print(student)
        elif user_input == "dfirst" or user_input == "df":
            select_students_end = " ORDER BY fname DESC"
            students = executeReadQuery(connection, select_students + select_students_end)
            for student in students:
                print(student)
        elif user_input == "last" or user_input == "l":
            select_students_end = " ORDER BY lname ASC"
            students = executeReadQuery(connection, select_students + select_students_end)
            for student in students:
                print(student)
        elif user_input == "dlast" or user_input == "dl":
            select_students_end = " ORDER BY lname DESC"
            students = executeReadQuery(connection, select_students + select_students_end)
            for student in students:
                print(student)
        elif user_input == "return" or user_input == "r" or user_input == "":
            menuSelect("1")
            condition = False
            return
        else:
            print("Invalid command")
    
def addCourse():
    newEntry = []
    print("Please enter new course name:")
    user_input = input()
    if user_input:
        user_input = user_input.capitalize()
        newEntry.append(user_input)
        values = ", ".join(f"'{value}'" for value in newEntry)
        executeQuery(connection, create_course+"("+values+")")
        print("Add another course? (y/n)")
        user_input = input()
        if user_input == "y" or user_input == "yes":
            clear()
            addCourse()
            return
        else:
            menuSelect("2")
            return
    else:
        menuSelect("2")
        return
        
    
def editCourse():
    print("WIP")
    input()
    menuSelect("2")
    
def viewCourses():
    select_courses = "SELECT * from courses"
    print("To view all courses, press enter. To return, type 'return'.")
    user_input = input()
    if user_input == "return" or user_input == "r":
        menuSelect("2")
        return
    else:
        courses = executeReadQuery(connection, select_courses)
        for course in courses:
            print(course)
        print("Press enter to return")
        input()
        menuSelect("2")
        return
    
def removeCourse():
    print("WIP")
    input()
    menuSelect("2")
    
def addScore():
    print("WIP")
    input()
    menuSelect("3")

def editScore():
    print("WIP")
    input()
    menuSelect("3")
    
def viewScores():
    print("WIP")
    input()
    menuSelect("3")

def removeScore():
    print("WIP")
    input()
    menuSelect("3")  
    
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
        
def executeReadQuery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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

startMessage()
