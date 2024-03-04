from flask import Flask, request, jsonify, render_template
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser

# Initialize your chatbot model
chatllm = ChatOpenAI(temperature=0.6, model='gpt-3.5-turbo')

# Define your Flask application
app = Flask(__name__)

# Define your chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the input text from the request
    data = request.get_json()
    user_input = data['text']

    # Define your chat prompt and chain
    template = "You are a Medical Consultant AI assistant. Whenever the user gives any input, you should give the user suggestions on how he can perform temporary first aid or any temporary action he can take based on the emergency he has mentioned in the text until the actual emergency services arrive to assist him, and then give the answer. The answer should be written as a paragraph or point wise."
    human_template = "{text}"
    chatprompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template)
    ])
    chain = chatprompt | chatllm

    # Invoke the chatbot model with user input
    message = chain.invoke({"text": user_input})

    # Return the response from the chatbot
    response = {
        'response': message.content
    }
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
