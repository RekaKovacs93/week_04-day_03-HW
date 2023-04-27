from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repo as book_repo
import repositories.author_repo as author_repo

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def books():
    # books = book_repo.select_all()
    return render_template("index.html")

@books_blueprint.route("/books")
def all_books():
    books = book_repo.select_all()
    return render_template("/books/index.html", books = books)

@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repo.select(id)
    return render_template('/books/book.html', book = book)

@books_blueprint.route("/books/<id>")
def show_author(id):
    author = author_repo.select(id)
    return render_template('/books/author.html', author = author)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')

@books_blueprint.route("/books",  methods=['POST'])
def create_book():
    title = request.form['title']
    author = author_repo.select(request.form['author'])
    pubdate   = request.form['pubdate']
    book = Book(title, pubdate, author) 
    book_repo.save(book)
    return redirect('/books/index..html', book = book)
