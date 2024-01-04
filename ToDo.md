- [ ] Connect with Cloud Data Base (ElephantSQL for postgresql)
? How to use session in Cloud dataBase
? should fetch data from database , and make one dummy data.json , which will consider the session as previous
? how to delete the data.json (dummy which will store session) after logout to avoid data leak


- [ ] VIEWS of data
- [ ] Add new entry for data set
- [ ] Pretify the Forms (both login and data entry/modification)
- [ ] Show all button to admin
- [ ] For student datshbord 
- [ ] side nav bar design
- [ ] change/edit password
- [ ] no authority to change any other instances
- [ ] Admin Follows Blue theme
- [ ] Student follows yellow theme
---
- [X] User Authentucation in Flask
- [X] Log OUT button (session terminatio)
- [X] How to different pages while being login , (if logged out not possible to accesss)
- [X] While admin is logged in , no login form will be seen for admin (/admin/login?)

```
    """  
        1) make sure to show only 5 entries (use VIEWS from sql)

        CREATE OR REPLACE VIEW random_students AS
        SELECT *
        FROM students
        ORDER BY RANDOM()
        LIMIT 5;

        SELECT * FROM random_students;


        2) after pressin show all ; show all entries
        3) can make new to display all entries (use SELECT qurery)

    """

```