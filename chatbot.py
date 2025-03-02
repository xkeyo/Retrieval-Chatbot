# Importing the necessary libraries
import spacy

# Loading the NLP model
nlp = spacy.load("en_core_web_sm")

# Defining the chatbot responses
responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer your questions. Try asking about something more specific!",
    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}

# Defining the chatbot function
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)


# Main function
if __name__ == "__main__":
    chat()

    


