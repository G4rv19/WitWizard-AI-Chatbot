import requests
import json
url   ='http://localhost:11434/api/generate'

headers = {
    'Content-Type': 'application/json',
}

prompt = input("Enter the prompt: ")
data = {
    "model": "tinyllama",
    "stream": False,
    "prompt": prompt
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data['response']
    print(actual_response)
else:
    print("Error: ", response.status_code, response.text)