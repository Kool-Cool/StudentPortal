
# DummyDataBase
#  dict ("email" : "password")
dummy_database = {
    "123@gmail.com" : "123",
    "12345@gmail.com" : "12345"
}

# DataBase Schema

"""  
subjects | teachers | students | grades


users
- id
- username
- password
- first_name
- last_name
- email
- password
- phone
- role_id (Student or Tutor or Admin)
- created
- modified

roles (Student, Tutor)
- id
- name
- created
- modified

courses (The courses that Tutors can teach and that Students can be assigned to)
- id
- start_date
- end_date
- created
- modified
- 

users_courses
- id
- user_id
- course_id
- created
- modified

"""