
# DummyDataBase
#  dict ("email" : "password")
dummy_database = {
    "123@gmail.com" : "123",
    "12345@gmail.com" : "12345"
}

# DataBase Schema

"""  
- takes:        ID, course_id, sec_id, semester, year, grade
- student:      ID, name, dept_name, tot_cred
- section:      course_id, sec_id, semester, year, building, room_no, time_slot_id
- course:       course id, title, dept_name, credits
- time_slot:    time_slot_id, day, start_time, end_time
- classroom:    building, room_no, capacity
- teaches:      ID, course_id, sec_id, semester, year
- instructor:   ID, name, dept_name, salary

"""