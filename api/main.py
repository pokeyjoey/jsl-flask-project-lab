from flask import Flask

app = Flask(__name__)

@app.route('/players')
def players():
    return 'Show all of the players'

@app.route('/players/<id>')
def player(id):
    return f'Show player {id}'

app.run(debug = True)
