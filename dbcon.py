import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    username="root",
    password="",
    port=3307
)

print(mydb)