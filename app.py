from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_URL = "https://api.openai.com/v1/engines/davinci/completions"
OPENAI_API_KEY = "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"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_prompt = request.json.get('prompt')
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    
    data = {
        "prompt": user_prompt,
        "max_tokens": 1500
    }
    
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    openai_response = response.json()['choices'][0]['text'].strip()

    return jsonify({'response': openai_response})

if __name__ == "__main__":
    app.run(debug=True)
