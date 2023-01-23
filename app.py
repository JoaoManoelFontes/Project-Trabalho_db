from flask import Flask, render_template, request
import mysql_cursor
from flask_mysqldb import MySQL 
import MySQLdb 

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'trabalho_db'

mysql = MySQL(app)

def get_connection():
    cursor = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cursor


# Routes
@app.route("/", methods=["GET", "POST", "PUT"])
def home():
    cursor = get_connection()
    cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    cursor.close()

    if request.method == "POST":
        #criar
        return render_template("index.html", books=books)
    elif request.method == "PUT":
        #atualiza
        print(request.method)
        return render_template("index.html", books=books)
    print("getete")
    return render_template('index.html', books=books)


@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    cursor = get_connection()
    cursor.execute('SELECT * FROM book WHERE id=%s' %id)
    book = cursor.fetchone()
    cursor.close()
    return render_template("book.html", book=book)

@app.route("/edit/<int:id>", methods=["GET"])
def edit(id):
    cursor = get_connection()
    cursor.execute("SELECT * FROM book WHERE id=%s" %id)
    book = cursor.fetchone()
    cursor.close()
    return render_template("edit.html", book=book)


@app.route("/book/<int:id>", methods=["GET"])
def get_book_by_id(id):
    cursor = get_connection()
    cursor.execute("SELECT * FROM book WHERE id=%s" %id)
    book = cursor.fetchone()
    cursor.close()
    return render_template("book.html", book=book)
