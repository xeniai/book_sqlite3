from flask import Flask, render_template, request
from random import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    results = cur.fetchall()
    return render_template("home.html", books=results)

@app.route("/add", methods=["POST", "GET"])
def add():
    
    if request.method == "POST":
        rand = randint(1, 100)
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        conn = sqlite3.connect("Books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES ({}, '{}', '{}', {})".format(rand, title, author, rating))
        conn.commit()
        conn.close()
    
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)