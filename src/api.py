from flask import Flask,jsonify,request
from json import load


# movies dict
movies = None

def load_json_dict():
    global movies

    with open('json/movies.json','r',encoding='utf-8') as json_file:
        movies = load(json_file)

api = Flask(__name__)

@api.route('/get_movies')
def get_movies():
    return jsonify(movies)

@api.route('/search')
def search_movie():
    sr = str(request.args['sr']).replace('+',' ')


    filtered_results = list(filter(lambda data:data['movie_name'].startswith(sr) or data['movie_name'].endswith(sr),movies))

    return jsonify(filtered_results)



if __name__ == '__main__':
    load_json_dict()
    api.run(host='0.0.0.0',debug=True)