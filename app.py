# Do not change anything in this file for this exercise
import json
import os
from flask import Flask, escape, request, jsonify, render_template

app = Flask(__name__)

with open('data/pokemon.json') as f:
  data = json.load(f)

# Home page route that serves index.html
@app.route('/')
def index():
    return render_template('index.html')

# Detail page route that serves detail.html
# For example /1 will give you the detail page for Bulbasaur
@app.route('/<int:id>')
def detail(id):
    return render_template('detail.html')

# API route that returns all pokemon from pokemon.json
@app.route('/api/pokemon', methods=['GET'])
def api_pokemon_get():
    return jsonify(data), 200

# API route that returns a single pokemon from pokemon.json according to the ID in the URL
# For example /api/pokemon/1 will give you Bulbasaur
@app.route('/api/pokemon/<int:id>', methods=['GET'])
def api_pokemon_id_get(id):
    for pokemon in data:
        if pokemon.get("id") == id:
            return jsonify(pokemon), 200
    return jsonify({}), 404

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)