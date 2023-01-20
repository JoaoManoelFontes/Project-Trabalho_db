from flask import Flask, render_template, request
import mysql_cursor

app = Flask(__name__)

# Routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(mysql_cursor.get_books())
        return "get_books()"

    return render_template("index.html")


@app.route("/books", methods=["GET"])
def get_books():
    books = mysql_cursor.get_books()


@app.route("/books/<int:id>", methods=["GET"])
def get_book_by_id(id):
    book = mysql_cursor.get_book_by_id(id)


# TODO: DELETE and CREATE routes
