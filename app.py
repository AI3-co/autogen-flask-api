import json
from flask import Flask, jsonify, request
from run_autogen import use_autogen

app = Flask(__name__)

@app.route('/api/v1/prompt', methods=['POST'])
def prompt_model():
    data = request.get_json()
    prompt = data['user_prompt']
    messages = use_autogen(prompt)
    return jsonify(messages)

@app.route('/api/v1/hi', methods=['GET'])
def say_hi():
    return "Hi"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5000)
