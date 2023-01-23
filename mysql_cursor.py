import mysql.connector
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
# Mysql configs
mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database="trabalho_db",
)

# Creating a cursor
cursor = mydb.cursor()

def get_cursor():
    return cursor

# Generics functions
def get_books() -> list:
    """Retorna toda a lista de livros presente no banco de dados"""
    cursor.execute("SELECT * FROM book;")
    return cursor.fetchall()


def get_book_by_id(id: str) -> object | None:
    """Retorna o livro com o id referente ao apresentado pelo usuário"""
    cursor.execute("SELECT * FROM book WHERE id=%s;" % id)
    return cursor.fetchone()
