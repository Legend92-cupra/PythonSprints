import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Eathan2704liezl",
)

# Create Cursor Instance
my_cursor = mydb.cursor()

# Create Database
my_cursor.execute("CREATE DATABASE Data_Tracker")

# Show database
my_cursor.execute("SHOW DATABASES")