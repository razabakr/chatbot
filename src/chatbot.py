from .api_client import APIClient

class Chatbot:
    def __init__(self):
        self.api_client = APIClient()

    def generate_response(self, user_input):
        # Use API to get response from GPT-3
        #
        return self.api_client.get_gpt3_response(user_input)

    def chat(self):
        print("Chatbot: Hi! I am your chatbot. Ask something or type 'quit'.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            #make function call to generate response here and then print it out
            response = self.generate_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
