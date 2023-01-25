# Imports
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, DateField)
from wtforms.validators import InputRequired, Length
import MySQLdb

# Flask app
app = Flask(__name__)
app.config.from_pyfile("config.py")
mysql = MySQL(app)

#Form
class BookForm(FlaskForm):
    title = StringField("Título", validators=[InputRequired(),Length(min=0, max=255)])
    synopsis = TextAreaField("Sinopse") 
    author_name = StringField("Autor(a)", validators=[InputRequired(),Length(min=0, max=255)])
    publishing_company_name = StringField("Editora", validators=[InputRequired(),Length(min=0, max=255)])
    release_year = DateField("Ano de lançamento", validators=[InputRequired()])
    category = StringField("Categoria", validators=[Length(min=0, max=255)])

# Generics
def get_connection():
    cursor = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cursor


def get_books():
    cursor = get_connection()
    cursor.execute("SELECT * FROM book")
    return cursor.fetchall()


def get_book_by_id(id):
    cursor = get_connection()
    cursor.execute("SELECT * FROM book WHERE id=%s" % id)
    return cursor.fetchone()


def delete_book(id):
    cursor = get_connection()
    cursor.execute("DELETE FROM book WHERE id=%s" % id)
    mysql.connection.commit()
    cursor.close()


def create_book(req):
    cursor = get_connection()
    cursor.execute(
        "INSERT INTO book (title, synopsis, author_name, publishing_company_name, release_year, category) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');"
        % (
            req["title"],
            req["synopsis"],
            req["author_name"],
            req["publishing_company_name"],
            req["release_year"],
            req["category"],
        )
    )
    mysql.connection.commit()
    cursor.close()


def update_book(id, req):
    cursor = get_connection()
    cursor.execute(
        "UPDATE book SET title='%s', synopsis='%s', author_name='%s', publishing_company_name='%s', release_year='%s', category='%s' WHERE id=%s;"
        % (
            req["title"],
            req["synopsis"],
            req["author_name"],
            req["publishing_company_name"],
            req["release_year"],
            req["category"],
            id,
        )
    )
    mysql.connection.commit()
    cursor.close()


# Routes
@app.route("/", methods=["GET", "POST", "PUT"])
def home():
    books = get_books()

    if request.method == "POST":
        if not request.form["title"]:
            print("erro")
        elif not request.form["author_name"]:
            print("erro")
        elif not request.form["publishing_company_name"]:
            print("erro")
        elif not request.form["release_year"]:
            print("erro")
        else:
            create_book(request.form)

        return redirect("/")

    return render_template("index.html", books=books)


@app.route("/cadastro", methods=["GET"])
def cadastro():
    form = BookForm()
    return render_template("cadastro.html", form = form)


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    delete_book(id)
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":
        update_book(id, request.form)
        return redirect("/")

    book = get_book_by_id(id)
    return render_template("edit.html", book=book)


@app.route("/book/<int:id>", methods=["GET"])
def get_book(id):
    book = get_book_by_id(id)
    return render_template("book.html", book=book)
