- [ ] User Authentucation in Flask
- [X] Log OUT button (session terminatio)
- [ ] VIEWS of data
- [ ] Add new entry for data set
- [ ] Show all button to admin
- [ ] For student datshbord 
- [ ] side nav bar design
- [ ] change/edit password
- [ ] no authority to change any other instances


# User Authentication in Flask
```py
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

login_manager = LoginManager()
login_manager.init_app(app)

admin_dummy_database = {
    "admin@gmail.com" : "admin"
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in admin_dummy_database and admin_dummy_database[username] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@login_manager.user_loader
def load_user(user_id):
    if user_id in admin_dummy_database:
        return User(user_id)
    return None

if __name__ == '__main__':
    app.run(debug=True)


```