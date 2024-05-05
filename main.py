from flask import Flask, request, jsonify
from webpage import webpage_chat

app = Flask(__name__)


#Endpoint
@app.route('/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data.get('question')
    url = data.get('url')
    openai_api_key = data.get('openai_api_key')
    
    if not openai_api_key:
        return jsonify({'error': 'OpenAI API key is required!'}), 400
    
    # Call the webpage_chat function to get the answer
    answer = webpage_chat(question, url, openai_api_key)
    
    # Return the answer as a JSON response
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
