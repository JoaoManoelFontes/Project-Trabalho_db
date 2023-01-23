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
@app.route("/", methods=["GET", "POST"])
def home():
    cursor = get_connection()
    cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    cursor.close()

    if request.method == "POST":
        #criar
        return render_template("index.html", books=books)

    return render_template('index.html', books=books)

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")


@app.route("/books", methods=["GET"])
def get_books():
    return "oi"


@app.route("/books/<int:id>", methods=["GET"])
def get_book_by_id(id):
    return "oi"


# TODO: DELETE and CREATE routes
