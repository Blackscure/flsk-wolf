from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movie_names = ['Avator',
                    'Pirate of Carribbean',
                    'Spectre',
                    'The dark Knight Rises',
                    'John Carter',
                    'Spiderman',
                    'Tangled']

    movies = {
        'Avator': {'critical_review': 732, 'duration': 170, 'indb_score':7.9},
        'Pirate of Carribbean': {'critical_review': 303, 'duration': 230, 'indb_score':8.9},
        'Spectre': {'critical_review': 702, 'duration': 180, 'indb_score':7.9},
        'The dark Knight Rises': {'critical_review': 172, 'duration': 150, 'indb_score':7.3},
        'John Carter': {'critical_review': 422, 'duration': 130, 'indb_score':4.9},
        'Spiderman': {'critical_review': 832, 'duration': 120, 'indb_score':3.9},
        'Tangled': {'critical_review': 392, 'duration': 110, 'indb_score':7.2},
    }
    return render_template('index.html', movie_names=movie_names, movies=movies)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True)