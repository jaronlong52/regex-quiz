import os
from flask import Flask, request, jsonify
from prompts import Prompt, build_match, build_regex, DIFFICULTY


app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Regex API!'


@app.route('/generate/<int:type>')
def generate(type: int):
    if type not in [0, 1]:
        return jsonify({'error': 'Invalid type. Use 0 for regex and 1 for match.'}), 400

    prompt: Prompt = None
    if type == 0:
        prompt = build_regex()
    else:
        prompt = build_match()

    data = prompt.to_dict()
    
    difficulty = request.args.get('difficulty', default=0, type=int)
    if difficulty < DIFFICULTY[0] or difficulty > DIFFICULTY[1]:
        return jsonify({'error': f'Invalid difficulty. Use a value between {DIFFICULTY[0]} and {DIFFICULTY[1]}.'}), 400

    data['difficulty'] = difficulty

    return jsonify(data), 200
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )
