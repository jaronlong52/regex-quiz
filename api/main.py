import os
from flask import Flask, request, jsonify
from prompts import build_prompt, MIN_DIFFICULTY, MAX_DIFFICULTY
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    if request.method != 'GET':
        return jsonify({'error': 'Only GET method is allowed for this endpoint.'}), 405

    return 'welcome to regex-api'


@app.route('/generate/<int:difficulty>', methods=['GET'])
def generate(difficulty: int):
    if request.method != 'GET':
        return jsonify({'error': 'Only GET method is allowed for this endpoint.'}), 405

    if difficulty < MIN_DIFFICULTY or difficulty > MAX_DIFFICULTY:
        return jsonify({'error': f'Invalid difficulty. Use a value between {MIN_DIFFICULTY} and {MAX_DIFFICULTY}.'}), 400
    
    quantity = request.args.get('quantity')
    num_strings = int(quantity) if quantity else 5

    prompt = build_prompt(difficulty, num_strings)
    data = prompt.to_dict()

    return jsonify(data), 200
    

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
