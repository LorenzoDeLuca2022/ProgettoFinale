from flask import render_template
from flask import Flask


app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ALBUM"
)

mycursor = mydb.cursor()

@app.route('/album')
def unitList():
    mycursor.execute("SELECT * FROM Album_Venduti")
    myresult = mycursor.fetchall()
    return render_template('project.html', album=myresult)
