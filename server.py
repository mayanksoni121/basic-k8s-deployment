import os
import mysql.connector

# Database configurations
db_host = os.environ.get('DB_HOST', 'localhost')
db_username = os.environ.get('DB_USERNAME', 'root')
db_password = os.environ.get('DB_PASSWORD', 'root')
db_name = os.environ.get('DB_NAME', 'mydatabase')

print("Connecting to the database...")
cnx = mysql.connector.connect(
    host=db_host,
    user=db_username,
    password=db_password
)
cursor = cnx.cursor()

print(f"Creating database `{db_name}`...")
cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
cnx.commit()

print(f"Switching to database `{db_name}`...")
cursor.execute(f"USE `{db_name}`;")

print("Creating table `users`...")
create_table = """
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT
);
"""
cursor.execute(create_table)

print("Inserting a user into the table...")
add_user = (
    "INSERT INTO users (name, email) "
    "VALUES (%s, %s);"
)
user_data = ('Pathan', 'srk@example.com')
cursor.execute(add_user, user_data)
cnx.commit()

cursor.close()
cnx.close()
print("Done.")
 