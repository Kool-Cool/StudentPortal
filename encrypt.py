import bcrypt


def pwd_encrypt(my_password):
    password = str(my_password).encode('utf-8')
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_pwd



"""  
TO CHECK PWD
"""
# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('my_database.db')
# c = conn.cursor()

# # Create table
# c.execute('''CREATE TABLE users
#              (username text, password text)''')

# # User's password
# password = "my_password".encode('utf-8')

# # Hash a password for the first time, with a randomly-generated salt
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# # Insert hashed password into the database
# c.execute("INSERT INTO users VALUES (?,?)", ('my_username', hashed))

# # Save (commit) the changes
# conn.commit()

# # Now let's check a password
# login_password = 'my_password'.encode('utf-8')

# # Fetch the hashed password from the database
# c.execute("SELECT password FROM users WHERE username = ?", ('my_username',))
# data = c.fetchone()  # Fetch one record
# db_password = data[0]

# # Check if the entered password matches the stored password
# if bcrypt.checkpw(login_password, db_password):
#     print("Password is correct")
# else:
#     print("Password is incorrect")

# # Close the connection
# conn.close()
