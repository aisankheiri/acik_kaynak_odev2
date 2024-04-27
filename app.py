from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Benim adim Aisan Kheiri 170420995 ve bu acik kaynak odevidir!'

@app.route('/books', methods=['GET'])
def get_books():
    # Tüm kitapları döndüren bir işlem
    books = [
        {'id': 1, 'title': 'Kitap 1'},
        {'id': 2, 'title': 'Kitap 2'},
        {'id': 3, 'title': 'Kitap 3'}
    ]
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET', 'DELETE'])
def get_or_delete_book(id):
    if request.method == 'GET':
        # Belirli bir kitabın detaylarını döndüren bir işlem yapılır
        book = {'id': id, 'title': f'Kitap {id}'}
        return jsonify(book)
    elif request.method == 'DELETE':
        # Belirli bir kitabı silen bir işlem yapılır
        # Silme işlemi başarılı olduğunda 204 No Content yanıtı döner
        return '', 204

if __name__ == '__main__':
    app.run()
