import json
from flask import Flask, escape, request, jsonify, render_template

app = Flask(__name__)
current_id = 151

with open('data/pokemon.json') as f:
  data = json.load(f)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/pokemon', methods=['GET'])
def api_pokemon_get():
    return jsonify(data), 200

@app.route('/api/pokemon/<int:id>', methods=['GET'])
def api_pokemon_id_get(id):
    for pokemon in data:
        if pokemon.get("id") == id:
            return jsonify(pokemon), 200
    return jsonify({}), 404

@app.route('/api/pokemon', methods=['POST'])
def api_pokemon_post():
    return "Yay!"
