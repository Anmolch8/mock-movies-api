from flask import Flask
from json import load

# movies dict
movies = None

def load_json_dict():
    global movies

    with open('json/movies.json','r') as json_file:
        movies = load(json_file)

api = Flask(__name__)

@api.route('/get_movies')
def get_movies():
    return {
        'movies' : movies 
    }


if __name__ == '__main__':
    load_json_dict()
    api.run(host='0.0.0.0',debug=True)