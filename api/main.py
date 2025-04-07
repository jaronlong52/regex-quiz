import os
from flask import Flask, request, jsonify
from prompts import build_prompt, MIN_DIFFICULTY, MAX_DIFFICULTY


app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Regex API!'


@app.route('/generate/<int:difficulty>', methods=['GET'])
def generate(difficulty: int):
    if difficulty < MIN_DIFFICULTY or difficulty > MAX_DIFFICULTY:
        return jsonify({'error': f'Invalid difficulty. Use a value between {MIN_DIFFICULTY} and {MAX_DIFFICULTY}.'}), 400
    
    quantity = request.args.get('quantity')
    num_strings = int(quantity) if quantity else 3

    prompt = build_prompt(difficulty, num_strings)
    data = prompt.to_dict()

    return jsonify(data), 200
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )
