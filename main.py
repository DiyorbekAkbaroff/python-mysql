from mysql.connector import connect
import settings
from db import (
    create_books_table,
    insert_book,
    show_all_books,
    search_books_by_author_or_genre,
    update_book_price,
    update_book_availability,
    delete_book,
    sort_books_by_year,
    count_books,
    price_statistics
)

def connect_to_db():
    password = DB_CONFIG["password"]

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=password,
        database=DB_CONFIG["database"],
        collation=DB_CONFIG["collation"]
    )

    cursor = connection.cursor()

create_books_table(cursor)

b = [
    ("Atomic Habits", "James Clear", 2018, "Self-help", 15.99, True),
    ("Deep Work", "Cal Newport", 2016, "Productivity", 12.50, True),
    ("Python Crash Course", "Eric Matthes", 2019, "Programming", 22.95, True)
]
insert_book(cursor, b)

DB_CONFIG.commit() 

show_all_books(cursor)

d = input("'author' yoki 'gender' kiriting --> " ).strip().lower()
r = input("qidirayotgan narsangizning nomini kiriting --> " ).strip()
search_books_by_author_or_genre(cursor, d, r)

book_id = int(input("Narxini yangilamoqchi bulgan kitob id raqamini kiriting --> " ))
new_price = float(input("Yangi narxni kiriting floatda bulsa yaxshi --> " ))
update_book_price(cursor, new_price, book_id)

a = int(input("mavjudligini uzgartirmoqchi bulgan kitobni id raqamini kiriting --> " ))
b = int(input("availableni 'True = 1', 'False = 0' raqami buyicha uzgartiring --> " ))
update_book_availability(cursor, a, b)

a = int(input("Uchirmoqchi bulgan narsangizni id raqamini kiritng --> " ))
delete_book(cursor, a)

sort = int(input("1- raqam usish taribida, 2- raqam kamayish tartibida --> ")) 
sort_books_by_year(cursor, sort)

count_books(cursor)

price_statistics(cursor)


cursor.close()
connect_to_db.close()