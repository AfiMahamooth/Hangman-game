import mysql.connector
def insert(name,word,word_length,status):
    db = mysql.connector.connect(host="localhost",user="root",password="",database="Hangman")
    cursor = db.cursor()
    cursor.execute("""INSERT INTO hangman_records (Player_Name, Word_Guessed, Turns_Provided, Turns_Used, Status) VALUES ('{}','{}',{},{},'{}');""".format(name, word, word_length, word_length, status[0]))
    db.commit()
    print("Database Updated")
    db.close()

