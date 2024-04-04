from flask import Flask, request, jsonify
import wikipedia
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app=app, origins=['http://localhost:5173/'])

@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/search/', methods=['POST'])
@cross_origin()
def searchWikipedia():
    data = request.get_json()
    word = data.get('word')
    app.logger.info(f'Searching for {word}')
    try:
        result = wikipedia.summary(f"{word}", sentences=10)
        return jsonify(result=result)
    except wikipedia.exceptions.PageError:
        return jsonify(result='Page not found')
    except wikipedia.exceptions.DisambiguationError:
        return jsonify(result='Disambiguation page')


if __name__ == '__main__':
    app.run(debug=True)