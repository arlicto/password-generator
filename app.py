from flask import Flask, render_template, request, jsonify
from generator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    letters = int(data.get('letters', 0))
    numbers = int(data.get('numbers', 0))
    symbols = int(data.get('symbols', 0))

    password = generate_password(letters, numbers, symbols)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
