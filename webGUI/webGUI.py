
import socket
from flask import Flask, render_template, request

from src import password_generate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate_password():
    json_data = request.get_json()
    if not json_data: return 'No input data provided'

    length = int(json_data['length'])
    special_chars = json_data['special_chars']
    include_numbers = json_data['include_numbers']
    allow_start_with_special = json_data['allow_start_with_special']

    password = password_generate.generator(length, special_chars, include_numbers, allow_start_with_special)

    return password

def find_free_port():
    s = socket.socket()
    s.bind(('', 0))
    return s.getsockname()[1]

def run(port):
    app.run(debug=False, port=port)