- [ ] How to different pages while being login , (if logged out not possible to accesss)
- [ ] VIEWS of data
- [ ] Add new entry for data set
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