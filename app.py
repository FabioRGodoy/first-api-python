from db import books

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/livros', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/livros/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


@app.route('/livros/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    updated_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(updated_book)
            return jsonify(books[index])


@app.route('/livros', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(new_book)


@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id' == id):
            del books[index]

    return jsonify(books)


app.run(port=3000, host='localhost', debug=True)
