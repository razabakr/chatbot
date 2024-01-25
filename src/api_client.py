import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APIClient:
    def __init__(self):
        # Set the OpenAI API key
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def get_gpt3_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Using the GPT-3.5 chat model
                messages=[{"role": "user", "content": prompt}]
            )
            # Assuming the response format has the message content
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error in generating response: {e}")
            return "I am having trouble understanding right now."
