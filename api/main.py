import os
from flask import Flask, request, jsonify
from prompts import build_prompt, MIN_DIFFICULTY, MAX_DIFFICULTY
from flask_cors import CORS
import re


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    if request.method != 'GET':
        return jsonify({'error': 'Only GET method is allowed for this endpoint.'}), 405

    return 'welcome to regex-api'


@app.route('/generate/<int:difficulty>', methods=['GET'])
def generate(difficulty: int):
    if difficulty < MIN_DIFFICULTY or difficulty > MAX_DIFFICULTY:
        return jsonify({'error': f'Invalid difficulty. Use a value between {MIN_DIFFICULTY} and {MAX_DIFFICULTY}.'}), 400
    
    quantity = request.args.get('quantity')
    num_strings = int(quantity) if quantity else 5

    prompt = build_prompt(difficulty, num_strings)
    data = prompt.to_dict()

    return jsonify(data), 200


@app.route('/test', methods=['POST'])
def test():
    """
    Endpoint that accepts a JSON payload with a regex pattern and a list of strings,
    and checks if each string fully matches the given regex pattern.

    Expected JSON payload:
    {
        "pattern": "<regex pattern>",
        "strings": ["<string1>", "<string2>", ...]
    }
    """
    data = request.get_json()
    if not data or 'pattern' not in data or 'strings' not in data:
        return jsonify({'error': 'Invalid payload. Must contain "pattern" and "strings".'}), 400

    pattern = data['pattern']
    strings = data['strings']

    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        return jsonify({'error': 'All "strings" must be a list of strings.'}), 400

    for string in strings:
        if not re.fullmatch(pattern, string):
            return jsonify({'result': False, 'error': f'"{pattern}" does not match string "{string}".'}), 200

    return jsonify({'result': True}), 200
   

def main():
    port = int(os.environ.get("PORT", 8080))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        threaded=True,
    )


if __name__ == '__main__':
    main()
