import mysql.connector
def retreive():
    db = mysql.connector.connect(host="localhost",user="root",password="",database="Hangman")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM hangman_records""")
    rows = cursor.fetchall()
    print("-"*80)
    print("Name\tWord Guessed\t Turns Provided\tTurns Used\tStatus")
    print("="*80)
    for row in rows:
        print("\t\t".join( str(item) for item in row))
