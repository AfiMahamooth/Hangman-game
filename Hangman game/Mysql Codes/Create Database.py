import mysql.connector
con = mysql.connector.connect(host="localhost",
user="root",
password="",
)
cursor = con.cursor()
cursor.execute("CREATE DATABASE Hangman")
con.close()
