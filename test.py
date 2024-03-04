import requests

# Define the API URL for the chatbot endpoint
api_url = 'https://chatbot-sp6egsqylq-el.a.run.app'  # Replace 'your-api-url' with the actual API URL

# Define the input text for the chatbot
input_text = {
    'text': 'corona virus and high fever'
}

# Send a POST request to the chatbot API
response = requests.post(api_url, json= input_text)

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the chatbot
    print(response.json())
else:
    print('Error: Failed to make a request. Status Code:', response.status_code)