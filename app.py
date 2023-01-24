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

    if request.method == "POST":
        if not request.form['title']:
            print("erro")
        elif not request.form['author_name']:
            print("erro")
        elif not request.form['publishing_company_name']:
            print("erro")
        elif not request.form['release_year']:
            print("erro")
        
        else:
            cursor.execute('INSERT INTO book (title, synopsis, author_name, publishing_company_name, release_year, category) VALUES (%s, %s, %s, %s, %s, %s);' %(request.form['title'], request.form['synopsis'], request.form['author_name'], request.form['publishing_company_name'], request.form['release_year'], request.form['category']))
            cursor.close()

        return render_template("index.html", books=books)
    
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

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cursor = get_connection()
    cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    cursor.close()

    if request.method == "POST":
        print(request.form)
        return render_template("index.html", books=books)

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
