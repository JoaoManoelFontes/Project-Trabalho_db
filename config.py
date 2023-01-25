import os
import dotenv
import secrets
secret_key = secrets.token_hex(16)

dotenv.load_dotenv(dotenv.find_dotenv())

MYSQL_HOST = os.getenv("HOST")
MYSQL_USER = os.getenv("USER")
MYSQL_PASSWORD = os.getenv("PASSWORD")
MYSQL_DB = "trabalho_db"
SECRET_KEY = secret_key
