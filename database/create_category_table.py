import connect

connect.cursor.execute(
    "CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(20) NOT NULL,"
    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"
)

connect.conn.commit()

connect.cursor.close()
