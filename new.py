import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS data_science1")

print("Database created")
