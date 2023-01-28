from app import app
from flask_mysqldb import MySQL
import MySQLdb

mysql = MySQL(app)


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
