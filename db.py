from mysql.connector.cursor import MySQLCursor

def create_books_table(cursor: MySQLCursor):
    # """Create a 'books' table in the database if it doesn't exist."""
    cursor.execute("USE company_db;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
        Id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        published_year INT NOT NULL,
        gender VARCHAR(100) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        available BOOLEAN DEFAULT TRUE NOT NULL);
    """)

    
def insert_book(cursor: MySQLCursor, books):
    # """Insert a new books into the 'books' table."""
    
    insert = """
       INSERT INTO books (title, author, published_year, gender, price, available)
       VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert, books)


def show_all_books(cursor: MySQLCursor):
    # """Retrieve and display all books from the 'books' table."""
    
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    for book in books:
        print(book)
    print("\n")


def search_books_by_author_or_genre(cursor: MySQLCursor, search_type, search_value):
    #  """Search for books by author or genre."""
    print("\n ")
    if search_type not in ['author', 'gender']:
        print("faqat 'author' yoki 'gender' kiritishingiz kerak ")
        return
    w = f"SELECT * FROM books WHERE {search_type} = %s"
    cursor.execute(w, (search_value,))
    books = cursor.fetchall()
    if books:
        for book in books:
            print(book)
    else:
        print("hech narsa yuq :(")
        print("\n")
    print("\n")


def update_book_price(cursor: MySQLCursor, book_id, new_price):
    # """Update the price of a specific book."""
    d = """UPDATE books
        SET price = %s
        WHERE Id = %s;
        """

    cursor.execute(d, (book_id, new_price))
    cursor._connection.commit()
    if cursor.rowcount > 0:
        print(f"Yangi kitobing narxi = {book_id}")    
    else:
        print("bunaqa id yuq ekan :(")
        print("\n")
    print("\n")


def update_book_availability(cursor: MySQLCursor, book_id, available):
    #  """Update the availability of a specific book."""
    s = ("""UPDATE books
         SET available = %s
         Where Id = %s;
         """)

    cursor.execute(s,(available, book_id))
    cursor._connection.commit()
    if cursor.rowcount > 0:
        print(f"{book_id} --> {available} ga uzgartirildi :)")
    else:
        print("Bunaqa id yuq :(")
        print("\n")
    print("\n")


def delete_book(cursor: MySQLCursor, book_id):
    # """Delete a specific book from the 'books' table.""" 
    a = "DELETE FROM books WHERE Id = %s"
    cursor.execute(a, (book_id,))
    cursor._connection.commit()
    if cursor.rowcount > 0:
        print(f"{book_id} --> O'chirildi :)")
    else:
        print("Bunaqa id raqam yuq !!!")
        print("\n")
    print("\n")


def sort_books_by_year(cursor: MySQLCursor, sort):
    # """Retrieve books sorted by published year."""
    d = 0
    if 1 == sort:
        d = ("SELECT * FROM books ORDER BY published_year;")
        print("Usish tartibida --->")
    elif 2 == sort:
        d = ("SELECT * FROM books ORDER BY published_year DESC;")
        print("Kamayish tartibida --->")
    else:
        print("Siz natug'ri raqam kirtdingiz ")
        print("\n")
    cursor.execute(d)
    books = cursor.fetchall()
    for book in books:
        print(book)
    print("\n")


def count_books(cursor: MySQLCursor):
    # """Count the total number of books in the 'books' table."""
    cursor.execute("SELECT COUNT(*) FROM books;")
    count = cursor.fetchall()[0]
    print(f"jami kitoblar soni: {count}")
    print("\n")


def price_statistics(cursor: MySQLCursor):
    # """Display min, max, and average price of books."""
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM books")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"Min Price: {min_price}, Max Price: {max_price}, Avg Price: {avg_price:.2f}")