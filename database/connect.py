import mysql.connector
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

conn = mysql.connector.connect(
    user=os.getenv("USER"), password=os.getenv("PASSWORD"), host=os.getenv("HOST")
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS trabalho_db;")
cursor.execute("USE trabalho_db;")
