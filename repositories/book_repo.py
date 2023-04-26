from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repo as author_repo

def save(book):
    sql = "INSERT INTO books (title, pubdate, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.pubdate, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book
