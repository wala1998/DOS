
from flask import Flask
from flask import request
from flask import Flask,jsonify,json
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'catalog server'


@app.route('/books', methods=['GET'])
def getBooksByTopic():
    topic = request.args.get('topic')
    f = open('books_catalog.json',) 
    data = json.load(f) 
    booksList = []
    for book in data['books']: 
        if book['topic'] == topic :
            bookDict = {
            'id': book['id'],
            'title': book['title']}
            booksList.append(bookDict)
            
    f.close()

    if len(booksList) == 0 :
        abort(404)

    return jsonify(booksList)
    

