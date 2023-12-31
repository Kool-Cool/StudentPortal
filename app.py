# Info form se aage nahi jaa rahi :)
from flask import Flask , render_template , request


from db_info import dummy_database as ddb
from db_info import admin_dummy_database as addb

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



@app.route("/admin/login" , methods = ["POST"])
def admin_login():
    # if person (instructor) is_role = Instuctor  , he / she has extra privillages
    # Adding class post or deleting class post , sharing files 
    # 
    return render_template("admin_login.html")


@app.route("/admin/login/<email>" , methods = ["POST"])
def admin_dashboard(email):
        return f"This is dashbord for {email}"
    # admin_email = request.form["admin_email"]
    # admin_password = request.form["admin_password"]
    
    # if admin_email not in addb:
    #     return render_template("admin_login.html" , return_message = "Invalid User")
    # else:
    #     if addb[admin_email] != admin_password:
    #         return render_template("admin_login.html" , return_message = "Invalid Password")
    #     else:
    #         # return render_template('', admin_email = admin_email)   
    #         return f"this is dashborad for admin {admin_email}"

    