# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS ALBUM")

mycursor.execute("DROP TABLE  IF  EXISTS ALBUM.Album_Venduti")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS ALBUM.Album_Venduti (
    ID INTEGER,
    Artista VARCHAR(50) NOT NULL,
    Album VARCHAR(50) NOT NULL,
    Anno CHAR(4) NOT NULL,
    Genere VARCHAR(20) NOT NULL,
    Vendite INTEGER,
    Miglior_Canzone VARCHAR(50),
    PRIMARY KEY (Album)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM ALBUM.Album_Venduti")
mydb.commit()

#Read data from a csv file
album = pd.read_csv('./album.csv', index_col=False, delimiter = ';')
album = album.fillna('Null')
print(album.head(20))

#Fill the table
for i,row in album.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO ALBUM.Album_Venduti VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM ALBUM.Album_Venduti")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)