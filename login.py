import sqlite3
import bcrypt

# Connecting to the database
def connect_to_database(database_name):
    
    if not database_name.endswith(".db"):
        raise ValueError("Invalid database name. Please provide a valid .db file.")
    
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        return connection, cursor
    except sqlite3.Error as error:
        return error
    
def close_database_connection(connection):
    try:
        connection.close()
    except sqlite3.Error as error:
        return error

def login(connection, cursor):
    try:
        name = input("Username: ")
        password = input("Password: ")

        cursor.execute("SELECT password FROM COMPANY WHERE name=?", (name,))
        stored_password = cursor.fetchone()
        print(stored_password)

        if stored_password:
            # Verifying the entered password with the stored hashed password
            if bcrypt.checkpw(password.encode(), stored_password[0]):
                print("Login successful!")
            else:
                print("Invalid password!")
        else:
            print("Invalid username!")
    except sqlite3.Error as error:
        return error


database_name = 'Login.db'
connection, cursor = connect_to_database(database_name)

login(connection, cursor)

close_database_connection(connection)


