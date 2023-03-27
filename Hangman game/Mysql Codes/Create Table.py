import mysql.connector
db = mysql.connector.connect(host="localhost",
user="root",
password="",
database="Hangman"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE Hangman_Records(Player_Name VARCHAR(20), Word_Guessed VARCHAR(30), Turns_Provided INT, Turns_Used INT, Status VARCHAR(5))")
print("Table Created")
con.close()
