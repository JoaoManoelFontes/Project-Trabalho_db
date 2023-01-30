from app import app
from flask import request, render_template, redirect, abort
from app import cursor
from app.form import CreateBookForm


@app.route("/", methods=["GET", "POST"])
def home():
    books = cursor.get_books()

    if request.method == "POST":
        if not request.form["title"]:
            abort(400)
        elif not request.form["author_name"]:
            abort(400)
        elif not request.form["publishing_company_name"]:
            abort(400)
        elif not request.form["release_year"]:
            abort(400)
        else:
            cursor.create_book(request.form)

        return redirect("/")

    return render_template("index.html", books=books)


@app.route("/cadastro", methods=["GET"])
def cadastro():
    form = CreateBookForm()
    return render_template("cadastro.html", form=form)


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    cursor.delete_book(id)
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":
        cursor.update_book(id, request.form)
        return redirect("/")

    book = cursor.get_book_by_id(id)
    form = CreateBookForm()
    return render_template("edit.html", book=book, form=form)


@app.route("/book/<int:id>", methods=["GET"])
def get_book(id):
    book = cursor.get_book_by_id(id)
    if book == None:
        abort(400)
    return render_template("book.html", book=book)
