import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

MYSQL_HOST = os.getenv("HOST")
MYSQL_USER = os.getenv("USER")
MYSQL_PASSWORD = os.getenv("PASSWORD")
MYSQL_DB = "trabalho_db"
