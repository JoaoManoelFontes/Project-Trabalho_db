import connect

# Creating book table
connect.cursor.execute(
    "CREATE TABLE book (id INT AUTO_INCREMENT PRIMARY KEY,"
    "title VARCHAR(255) NOT NULL,"
    "synopsis TEXT,"
    "author_name VARCHAR(255) NOT NULL,"
    "publishing_company_name VARCHAR(255) NOT NULL,"
    "release_year DATE NOT NULL,"
    "category VARCHAR(255));"
)

connect.conn.commit()

connect.cursor.close()
