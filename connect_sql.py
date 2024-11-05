import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "root",
    database = "vote"
)
if conn.is_connected():
    print("Successfully connected")