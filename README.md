### Webpage-chat

### Using Postman
Start by running the Flask
Once the server is running, open Postman.
Set the request type to POST.
Enter the URL where the Flask server is hosted, along with the endpoint for the webpage_chat function.
In the request body, provide the question and URL as JSON data.
Click on "Send" to submit the request.
You will receive the response containing the answer to your question.
### Using Python Script
Import the webpage_chat function into your Python script.
Provide the question, URL, and OpenAI API key as arguments to the function.
Call the function with the provided arguments.
The function will return the answer to your question based on the content of the webpage.
You can then print or process the answer as needed.

Example (Python Script)

from webpage_chat import webpage_chat

question = "What is generative artificial intelligence?"
url = "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"
openai_api_key = "YOUR_OPENAI_API_KEY_HERE"

answer = webpage_chat(question, url, openai_api_key)
print("Answer:", answer)
Replace "YOUR_OPENAI_API_KEY_HERE" with your actual OpenAI API key.

