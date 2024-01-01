
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



