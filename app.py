from flask import Flask, escape, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
def api_messages_get():
    data = [
        {
            "user": "Jon",
            "message": "Hello!",
            "created_at": "2020-01-01 00:00:00"
        }
    ]
    return jsonify(data)