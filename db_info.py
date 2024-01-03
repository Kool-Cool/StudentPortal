
# DummyDataBase
#  dict ("email" : "password")
dummy_database = {
    "123@gmail.com" : "123",
    "12345@gmail.com" : "12345"
}

admin_dummy_database = {
    "admin@gmail.com" : "admin"
}

# DataBase Schema

data = {
  "students": [
    {
      "student_id": "S123",
      "roll_no": "R123",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "password": "password123",
      "dept_id": "D1",
      "dept_branch": "Computer Science",
      "credits_earned": 120,
      "gpa": 3.8
    },
    {
      "student_id": "S124",
      "roll_no": "R124",
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "password": "password123",
      "dept_id": "D2",
      "dept_branch": "Mechanical Engineering",
      "credits_earned": 110,
      "gpa": 3.6
    }
  ],
  "departments": [
    {
      "dept_id": "D1",
      "dept_name": "Department of Computer Science",
      "dept_branch": "Computer Science"
    },
    {
      "dept_id": "D2",
      "dept_name": "Department of Mechanical Engineering",
      "dept_branch": "Mechanical Engineering"
    }
  ],
  "courses": [
    {
      "course_id": "C1",
      "course_name": "Introduction to Computer Science",
      "dept_id": "D1",
      "credits": 4
    },
    {
      "course_id": "C2",
      "course_name": "Thermodynamics",
      "dept_id": "D2",
      "credits": 3
    }
  ],
  "enrollments": [
    {
      "enrollment_id": "E123",
      "student_id": "S123",
      "roll_no": "R123",
      "course_id": "C1",
      "semester": "Fall",
      "year": 2023,
      "grade": "A"
    },
    {
      "enrollment_id": "E124",
      "student_id": "S124",
      "roll_no": "R124",
      "course_id": "C2",
      "semester": "Spring",
      "year": 2023,
      "grade": "B"
    }
  ],
  "grades": [
    {
      "course_id": "C1",
      "student_id": "S123",
      "enrollment_id": "E123",
      "semester": "Fall",
      "year": 2023,
      "quiz_1": 20,
      "quiz_2": 22,
      "end_term": 45
    },
    {
      "course_id": "C2",
      "student_id": "S124",
      "enrollment_id": "E124",
      "semester": "Spring",
      "year": 2023,
      "quiz_1": 18,
      "quiz_2": 20,
      "end_term": 40
    }
  ],
  "instructors": [
    {
      "instructor_id": "I1",
      "inst_name": "Dr. Smith",
      "inst_email": "dr.smith@example.com",
      "dept_id": "D1",
      "course_id": "C1"
    },
    {
      "instructor_id": "I2",
      "inst_name": "Dr. Johnson",
      "inst_email": "dr.johnson@example.com",
      "dept_id": "D2",
      "course_id": "C2"
    }
  ]
}



"""  
Need to redesign 
- admin: ID , name , email , password
"""

# Create students table query
create_students_query = '''
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(20) PRIMARY KEY,
    roll_no VARCHAR(20) UNIQUE,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) NOT NULL,
    dept_id VARCHAR(10) REFERENCES departments(dept_id),
    dept_branch VARCHAR(20),
    credits_earned INT,
    gpa NUMERIC(3,2),
    CONSTRAINT unique_student_roll_no_id UNIQUE (student_id, roll_no)
);
'''

# Insert into students table query
insert_students_query = '''
INSERT INTO students (student_id, roll_no, first_name, last_name, email, password, dept_id, dept_branch, credits_earned, gpa)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

# Update students table query
update_students_query = '''
UPDATE students
SET
    roll_no = %s,
    first_name = %s,
    last_name = %s,
    email = %s,
    password = %s,
    dept_id = %s,
    dept_branch = %s,
    credits_earned = %s,
    gpa = %s
WHERE
    student_id = %s;
'''



# Create departments table query
create_departments_query = '''
CREATE TABLE IF NOT EXISTS departments (
    dept_id VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(20),
    dept_branch VARCHAR(20)
);
'''

# Insert into departments table query
insert_departments_query = '''
INSERT INTO departments (dept_id, dept_name, dept_branch)
VALUES (%s, %s, %s);
'''

# Update departments table query
update_departments_query = '''
UPDATE departments
SET
    dept_name = %s,
    dept_branch = %s
WHERE
    dept_id = %s;
'''




# Create courses table query
create_courses_query = '''
CREATE TABLE IF NOT EXISTS courses (
    course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    dept_id VARCHAR(10) REFERENCES departments(dept_id),
    credits INT
);
'''

# Insert into courses table query
insert_courses_query = '''
INSERT INTO courses (course_id, course_name, dept_id, credits)
VALUES (%s, %s, %s, %s);
'''

# Update courses table query
update_courses_query = '''
UPDATE courses
SET
    course_name = %s,
    dept_id = %s,
    credits = %s
WHERE
    course_id = %s;
'''




# Create enrollments table query
create_enrollments_query = '''
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id VARCHAR(20) PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    roll_no VARCHAR(20),
    course_id VARCHAR(10) REFERENCES courses(course_id),
    semester VARCHAR(255),
    year INT,
    grade VARCHAR(2)
);
'''

# Insert into enrollments table query
insert_enrollments_query = '''
INSERT INTO enrollments (enrollment_id, student_id, roll_no, course_id, semester, year, grade)
VALUES (%s, %s, %s, %s, %s, %s, %s);
'''

# Update enrollments table query
update_enrollments_query = '''
UPDATE enrollments
SET
    student_id = %s,
    roll_no = %s,
    course_id = %s,
    semester = %s,
    year = %s,
    grade = %s
WHERE
    enrollment_id = %s;
'''




# Create grades table query
create_grades_query = '''
CREATE TABLE IF NOT EXISTS grades (
    course_id VARCHAR(10) REFERENCES courses(course_id),
    student_id INT REFERENCES students(student_id),
    enrollment_id VARCHAR(20) REFERENCES enrollments(enrollment_id),
    semester VARCHAR(255),
    year INT,
    quiz_1 INT CHECK (quiz_1 > 0 AND quiz_1 <= 25),
    quiz_2 INT CHECK (quiz_2 > 0 AND quiz_2 <= 25),
    end_term INT CHECK (end_term >= 0 AND end_term <= 50),
    PRIMARY KEY (course_id, student_id, enrollment_id, semester, year)
);
'''

# Insert into grades table query
insert_grades_query = '''
INSERT INTO grades (course_id, student_id, enrollment_id, semester, year, quiz_1, quiz_2, end_term)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
'''

# Update grades table query
update_grades_query = '''
UPDATE grades
SET
    course_id = %s,
    student_id = %s,
    enrollment_id = %s,
    semester = %s,
    year = %s,
    quiz_1 = %s,
    quiz_2 = %s,
    end_term = %s
WHERE
    course_id = %s AND student_id = %s AND enrollment_id = %s AND semester = %s AND year = %s;
'''



# Create instructors table query
create_instructors_query = '''
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id VARCHAR(20) PRIMARY KEY,
    inst_name VARCHAR(255),
    inst_email VARCHAR(255) UNIQUE,
    dept_id VARCHAR(10) REFERENCES departments(dept_id),
    course_id VARCHAR(10) REFERENCES courses(course_id)
);
'''

# Insert into instructors table query
insert_instructors_query = '''
INSERT INTO instructors (instructor_id, inst_name, inst_email, dept_id, course_id)
VALUES (%s, %s, %s, %s, %s);
'''

# Update instructors table query
update_instructors_query = '''
UPDATE instructors
SET
    inst_name = %s,
    inst_email = %s,
    dept_id = %s,
    course_id = %s
WHERE
    instructor_id = %s;
'''




