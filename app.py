from flask import Flask , render_template , request


from db_info import dummy_database as ddb

app = Flask(__name__)

@app.route("/" , methods = ["POST" , "GET"])
def home():
    # return "This is Home Page !!"
    return render_template("login.html")

@app.route("/student_login" , methods = ["POST"])
def login():
    student_email = request.form["student_email"]
    student_password = request.form["student_password"]
    
    if student_email not in ddb:
        return render_template("login.html" , return_message = "Invalid User")
    else:
        if ddb[student_email] != student_password:
            return render_template("login.html" , return_message = "Invalid Password")
        else:
            return render_template("std_home.html" , student_email = student_email)
