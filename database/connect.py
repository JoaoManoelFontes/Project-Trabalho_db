import mysql.connector
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

# MySQL configs
conn = mysql.connector.connect(
    user=os.getenv("USER"), password=os.getenv("PASSWORD"), host=os.getenv("HOST")
)

# Creating a cursor
cursor = conn.cursor()

# Creating and selecting the database
cursor.execute("CREATE DATABASE IF NOT EXISTS trabalho_db;")
cursor.execute("USE trabalho_db;")
