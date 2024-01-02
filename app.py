# Info form se aage nahi jaa rahi :)
from flask import Flask , render_template , request , json , jsonify, session, redirect, url_for

import json
import random
import string

def genKey(n=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(n))
    return random_string

db = json.load(open('db.json', 'r'))
ddb = db['dummy_database']
adb = db['admin_dummy_database']
data = db['data']


app = Flask(__name__)
app.secret_key = "key"


@app.route("/try")
def myTry():
    return render_template("try.html" )



@app.route("/" , methods = ["POST" , "GET"])
def home():
    logged_user = None
    try:
        for i in ddb:
            if i['session']==session['session']:
                logged_user = i
    except KeyError:
        pass
    if not logged_user:
        return render_template("std_login.html")
    elif logged_user:
        return render_template("std_dashboard.html", student_email = logged_user['email'], show_email = logged_user['email'])

@app.route("/student_dashbord" , methods = ["POST", 'GET'])
def std_login():
    student_email = request.form["student_email"]
    student_password = request.form["student_password"]
    user_exists = False
    logged_user = None
    logged_user_index = None
    for i in ddb:
        if i['email']==student_email:
            user_exists = True
        if i['password']==student_password:
            logged_user = i
            logged_user_index = ddb.index(logged_user)
    if not user_exists:
        return render_template("std_login.html" , return_message = "Invalid User")
    elif user_exists:
        if not logged_user:
            return render_template("std_login.html" , return_message = "Invalid Password")
        elif logged_user:
            new_session = genKey()
            ddb[logged_user_index]['session'] = new_session
            db['dummy_database'] = ddb
            session['session'] = new_session
            with open('db.json', 'w') as f:
                json.dump(db, f)
            return render_template("std_dashboard.html" , student_email = student_email , show_email = student_email)



@app.route("/admin/login" )
def admin_login():
    return render_template("admin_login.html")



@app.route("/admin_dashbord" ,methods = ["POST"])
def admin_dashboard():
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
    admin_email = request.form["admin_email"]
    admin_password = request.form["admin_password"]
    
    if admin_email not in adb:
        return render_template("admin_login.html" , return_message = "Invalid User")
    else:
        if adb[admin_email] != admin_password:
            return render_template("admin_login.html" , return_message = "Invalid Password")
        else:
            return render_template("admin_dashboard.html" , admin_email = admin_email , data = data , show_email = admin_email)

@app.route("/logout")
def logout():
    session.pop('session')
    return redirect(url_for("home"))