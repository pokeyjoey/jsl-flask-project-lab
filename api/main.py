from flask import Flask, jsonify
from settings import DATABASE, DB_USER
from api.models import Player

import psycopg2

app = Flask(__name__)

# Pass environment variables to the app
app.config.from_mapping(
    DB=DATABASE,
    USER=DB_USER
)

def get_db():
    conn = psycopg2.connect(
        database = app.config['DB'],
        user = app.config['USER'],
        password = 'postgres')
    cursor = conn.cursor()

    return cursor

def create_player(player_lst):
    player_dict = dict(zip(Player.columns, player_lst))
    player_object = Player(player_dict)

    return player_object

@app.route('/players')
def players():
    # get all of the players from the db
    cursor = get_db()
    cursor.execute('SELECT * FROM players')
    players =  cursor.fetchall()

    # create a list of player objects
    player_objects = [create_player(player).__dict__ for player in players]

    return player_objects

@app.route('/players/<id>')
def player(id):
    cursor = get_db()
    cursor.execute('SELECT * FROM players WHERE id = %s', id)
    player = cursor.fetchone()

    player_object = create_player(player)

    return jsonify(player_object.__dict__)


