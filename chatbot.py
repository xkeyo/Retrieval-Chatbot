# Importing the necessary libraries
import spacy
import re

# Loading the NLP model
nlp = spacy.load("en_core_web_sm")

# Defining the chatbot responses
responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer your questions. Try asking about something more specific!",
    "if_statement": "An if statement in Java is used to make a decision based on a condition.",
    "for_loop": "A for loop is used for iterating over a sequence of elements.",
    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}

# Different patterns to match user inputs
patterns = {
    r"\bhello|hi|hey\b": "greet",
    r"\bbye|goodbye|exit\b": "bye",
    r"\bhelp|support\b": "help",
    r"\bif statement|if condition|if in java\b": "if_statement",
    r"\bfor loop|for statement|for in java\b": "for_loop"
}

# Defining the get_response function
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for matching patterns using regex
    for pattern, response_key in patterns.items():
        if re.search(pattern, user_input):
            if response_key == "bye":
                return "exit"
            return responses[response_key]
    
    return responses["default"]

# Defining the chatbot function
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", response)

# Main function
if __name__ == "__main__":
    chat()

    


