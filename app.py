# Imports
from flask import Flask, render_template, request, redirect, abort
from flask_mysqldb import MySQL
import MySQLdb
from form import CreateBookForm

# Flask app
app = Flask(__name__)
app.config.from_pyfile("config.py")
mysql = MySQL(app)

# Generics
def get_connection():
    """Retorna o cursor para fazer querys no banco de dados"""
    cursor = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cursor


def get_books() -> list:
    """Retorna todos os livros cadastrados no banco"""
    cursor = get_connection()
    cursor.execute("SELECT * FROM book")
    return cursor.fetchall()


def get_book_by_id(id: int) -> object or None:
    """retorna o livro com id referente ao passado pelo usuário"""
    cursor = get_connection()
    cursor.execute("SELECT * FROM book WHERE id=%s" % id)
    return cursor.fetchone()


def delete_book(id: int) -> None:
    """Deleta o livro com id referente ao passado pelo usuário"""
    cursor = get_connection()
    cursor.execute("DELETE FROM book WHERE id=%s" % id)
    mysql.connection.commit()
    cursor.close()


def create_book(req: dict) -> None:
    """Cadastra um novo livro no banco de dados"""
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
    form = CreateBookForm()
    return render_template("cadastro.html", form=form)


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
    if book == None:
        abort(400)
    return render_template("book.html", book=book)
