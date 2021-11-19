
from flask import Flask
from flask import request
from flask import Flask,jsonify,json
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'catalog server'

#searchbytopicTested
@app.route('/books', methods=['GET'])
def getBooksByTopic(): 
    topic = request.args.get('topic')
    file = open('books_catalog.json',) 
    data = json.load(file) 
    booksList = []
    for book in data['books']: 
        if book['topic'] == topic :
            bookDict = {
            'id': book['id'],
            'title': book['title']}
            booksList.append(bookDict)
            file.close()

        if len(booksList) == 0 : 
            abort(404)

    return jsonify(booksList)  
  #searchbybooksID
@app.route('/books/<bookid>', methods=['GET'])
def getById(bookid):
  file = open('books_catalog.json',)
  data = json.load(file)
  
  for book in data['books']:
    if book['id'] == int(bookid) :
       return jsonify(book)
  file.close()
  abort(404)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
