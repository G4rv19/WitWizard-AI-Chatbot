from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
CORS(app)

# Global variable to store selected model
current_model = "openchat:7b"
executor = ThreadPoolExecutor(max_workers=4)  # Adjust the number of workers as needed

def ollama(message, model):
    url = 'http://127.0.0.1:11434/api/generate'  # Use service name 'ollama'
    headers = {'Content-Type': 'application/json'}
    data = {
        "model": model,
        "stream": False,
        "prompt": message
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        return actual_response
    else:
        print("Error: ", response.status_code, response.text)
        return f"Error: {response.status_code} - {response.text}"

@app.route('/save-model', methods=['POST'])
def save_model():
    global current_model
    data = request.get_json()
    current_model = data.get('model')
    return jsonify({'message': f'Model {current_model} saved successfully'}), 200

@app.route('/backend', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message')
    model = data.get('model', current_model)
    print(f"Received message: {message} with model: {model}")
    future = executor.submit(ollama, message, model)
    try:
        reply = future.result()  # This will block until the function completes
    except Exception as e:
        print(f"Error in ollama function: {e}")
        return jsonify({'message': 'Error generating response'}), 500

    return jsonify({'message': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
