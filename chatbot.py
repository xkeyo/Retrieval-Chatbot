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

    # IF-STATEMENT RELATED
    "if_statement": "An if statement in Java checks a condition and executes the block of code if the condition is true. Syntax: `if (condition) { // block of code to be executed if the condition is true}`.",
    "else_statement": "An else statement in Java runs if the 'if' condition is false. It provides an alternative path. Syntax: `if (condition) { // block of code to be executed if the condition is true } else { // block of code to be executed if the condition is false }`.",
    "else_if_statement": "An else-if statement in Java allows multiple conditions to be checked in sequence. Syntax: `if (condition1) { // block of code to be executed if condition1 is true } else if (condition2) { // block of code to be executed if the condition1 is false and condition2 is true } else { // block of code to be executed if the condition1 is false and condition2 is false }`.",
    "nested_if": "A nested if statement is an if statement inside another if statement for more complex logic. Syntax: `if (condition1) { // block of code to be executed if condition1 is true if (condition2) { // block of code to be executed if condition1 is true and condition2 is true } }`.",
    "ternary_operator": "The ternary operator (?:) in Java is a shorthand for a simple if-else statement. Syntax: `variable = (condition) ? expressionTrue : expressionFalse;`.",
    "logical_operators": "Logical operators (`&&`, `||`, `!`) are used in if statements to combine conditions. Syntax: `if (condition1 && condition2) { // code }`.",
    "difference_if_else": "if-else runs one of two code blocks, depending on the condition. if runs only one block or none if false.",
    "difference_if_elseif": "Use else-if to handle multiple conditions. Without else-if, you'd have separate if statements that can all run.",
    "difference_if_switch": "Use if statements for complex or range-based conditions. Switch is often clearer for discrete, fixed values.",
    
    # FOR-LOOP RELATED
    "for_loop": "A for loop in Java is used to iterate a set number of times. Syntax: for(int i=0; i<n; i++){...}",
    "enhanced_for_loop": "The enhanced for loop (for-each) in Java iterates over arrays or collections. Syntax: for(Type var : array){...}",
    "nested_for_loop": "A nested for loop is one for loop inside another. Useful for multi-dimensional data or repeated tasks. Syntax: `for(int i=0; i<n; i++){ for(int j=0; j<m; j++){...} }`.",    
    "difference_for_while": "A for loop is best when you know how many times to iterate. A while loop is best when the number of iterations is not fixed.",
    "difference_for_do_while": "A for loop checks the condition before each iteration. A do-while loop runs at least once before checking.",

    # OTHER CONTROL-FLOW STATEMENTS
    "while_loop": "A while loop in Java runs as long as its condition is true. Syntax: while(condition){...}",
    "do_while_loop": "A do-while loop runs the code block at least once before checking the condition. Syntax: do{...} while(condition);",
    "switch_statement": "A switch statement in Java chooses execution paths based on matching a variable to cases. Syntax: `switch(expression) { case x: // code block break; case y: // code block break; default: // code block }`.",
    "break_statement": "A break statement ends the nearest loop or switch immediately.",
    "continue_statement": "A continue statement skips the current iteration of the loop and continues with the next iteration.",
    "labeled_break": "A labeled break can exit an outer loop from an inner loop. Syntax: labelName: for(...){... break labelName;}",
    "labeled_continue": "A labeled continue can skip the current iteration of an outer loop. Syntax: labelName: for(...){... continue labelName;}",
    "difference_while_do_while": "A while loop checks the condition first; a do-while loop executes at least once before checking.",
    
    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}

# Different patterns to match user inputs
patterns = {
    # Greetings / Exit / Help
    r"\b(hello|hi|hey)\b": "greet",
    r"\b(bye|goodbye|exit)\b": "bye",
    r"\b(help|support)\b": "help",
    
    # IF-STATEMENT RELATED
    r"\b(if statement|if condition|if in java)\b": "if_statement",
    r"\b(else statement|else in java)\b": "else_statement",
    r"\b(else if|elseif|else-if)\b": "else_if_statement",
    r"\b(nested if|nested condition)\b": "nested_if",
    r"\b(ternary operator|conditional operator)\b": "ternary_operator",
    r"\b(logical operator|logical operators |logical and|logical or|logical not)\b": "logical_operators",
    r"\b(difference between if and else|if vs else)\b": "difference_if_else",
    r"\b(difference between if and else if|if else if)\b": "difference_if_elseif",
    r"\b(difference between if and switch|if vs switch)\b": "difference_if_switch",
    
    # FOR-LOOP RELATED
    r"\b(for loop|for statement|for in java)\b": "for_loop",
    r"\b(enhanced for loop|for each loop|for-each loop)\b": "enhanced_for_loop",
    r"\b(nested for loop|double for loop)\b": "nested_for_loop",
    r"\b(difference between for and while|for vs while)\b": "difference_for_while",
    r"\b(difference between for and do while|for vs do while)\b": "difference_for_do_while",
    
    # OTHER CONTROL-FLOW
    r"\b(while loop|while in java)\b": "while_loop",
    r"\b(do while loop|do-while loop|do while in java)\b": "do_while_loop",
    r"\b(switch statement|switch in java)\b": "switch_statement",
    r"\b(break statement|break in java)\b": "break_statement",
    r"\b(continue statement|continue in java)\b": "continue_statement",
    r"\b(labeled break|labelled break)\b": "labeled_break",
    r"\b(labeled continue|labelled continue)\b": "labeled_continue",
    r"\b(difference between while and do while|while vs do while)\b": "difference_while_do_while",
}

# Defining the get_response function
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for matching patterns using regex
    for pattern, response_key in patterns.items():
        if re.search(pattern, user_input):
            if response_key == "bye":
                return responses["bye"]

            return responses[response_key]
    
    return responses["default"]

# Defining the chatbot function
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == responses["bye"]:
            print("Chatbot:", response)
            break

        print("Chatbot:", response)
                
# Main function
if __name__ == "__main__":
    chat()
