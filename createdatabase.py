import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="newdb"
    )

my_cursor=db.cursor()

my_cursor.execute("CREATE DATABASE NewDB")
my_cursor.execute("SHOW DATABASES")

for each in my_cursor:
    print(each)
