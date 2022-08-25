from flask import Flask, jsonify
from settings import DATABASE, DB_USER

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


@app.route('/players')
def players():
    cursor = get_db()
    cursor.execute('SELECT * FROM players')
    players =  cursor.fetchall()

    return jsonify(players)

@app.route('/players/<id>')
def player(id):
    cursor = get_db()
    cursor.execute('SELECT * FROM players WHERE id = %s', id)
    player = cursor.fetchone()

    return jsonify(player)


