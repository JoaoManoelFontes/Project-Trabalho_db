import connect

connect.cursor.execute(
    "CREATE TABLE book (id INT AUTO_INCREMENT PRIMARY KEY,"
    "title VARCHAR(255) NOT NULL,"
    "synopsis TEXT,"
    "author_name VARCHAR(255) NOT NULL,"
    "publishing_company_name VARCHAR(255) NOT NULL,"
    "release_year DATE NOT NULL,"
    "category_id int,"
    "CONSTRAINT FK_category FOREIGN KEY (category_id) REFERENCES category(id));"
)

connect.conn.commit()

connect.cursor.close()
