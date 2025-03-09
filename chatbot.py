# -------------------------------------------------------------------------------
# Chatbot Project with NLP Integration
# Written by: Pratham Patel - 40227835, Jonathan Chen - 40214327
# For COMP-474 - Winter 2025
# ---------------------------------------------------------------------------------


# Importing the necessary libraries
import spacy
import re

# Loading the NLP model for tokenization
nlp = spacy.load("en_core_web_sm")

# Defining the chatbot responses based on user inputs
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
    "while_loop": "A while loop in Java loops through a block of code as long as a specified condition is true. Syntax: while(condition){ // code block to be executed}",
    "do_while_loop": "A do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true. Syntax: do{ //code block to be executed} while(condition);",
    "switch_statement": "A switch statement in Java chooses execution paths based on matching a variable to cases. Syntax: `switch(expression) { case x: // code block break; case y: // code block break; default: // code block }`.",
    "break_statement": "A break statement ends the nearest loop or switch immediately.",
    "continue_statement": "A continue statement skips the current iteration of the loop and continues with the next iteration.",
    "labeled_break": "A labeled break can exit an outer loop from an inner loop. Syntax: labelName: for(...){... break labelName;}",
    "labeled_continue": "A labeled continue can skip the current iteration of an outer loop. Syntax: labelName: for(...){... continue labelName;}",
    "difference_while_do_while": "A while loop checks the condition first; a do-while loop executes at least once before checking.",
    
    "default": "I'm sorry, I didn't understand that. Could you rephrase?"
}

# Different patterns to match user inputs and their corresponding responses
patterns = {
    # Greetings / Exit / Help
    r"\b(hello|hi|hey)\b": "greet",
    r"\b(bye|goodbye|exit)\b": "bye",
    r"\b(help|support)\b": "help",
    
    # IF-STATEMENT RELATED
    r"\b(if statement|if|if condition|if in java)\b": "if_statement",
    r"\b(else statement|else|else in java)\b": "else_statement",
    r"\b(else if statement|else if|elseif|else-if)\b": "else_if_statement",
    r"\b(nested if statement|nested if|nested condition)\b": "nested_if",
    r"\b(ternary operator|conditional operator)\b": "ternary_operator",
    r"\b(logical operator|logical operators|logical and|logical or|logical not)\b": "logical_operators",
    r"\b(difference between if and else|difference between else and if|if vs else|else vs if)\b": "difference_if_else",
    r"\b(difference between if and else if|difference between else if and if|if vs else if|else if vs if)\b": "difference_if_elseif",
    r"\b(difference between if and switch|difference between if and switch|if vs switch|switch vs if)\b": "difference_if_switch",
    
    # FOR-LOOP RELATED
    r"\b(for loop|for statement|for in java)\b": "for_loop",
    r"\b(enhanced for loop|for each loop|for-each loop)\b": "enhanced_for_loop",
    r"\b(nested for loop|double for loop)\b": "nested_for_loop",
    r"\b(difference between for and while|difference between while and for|for vs while|while vs for)\b": "difference_for_while",
    r"\b(difference between for and do while|difference between do while and for|for vs do while|do while vs for)\b": "difference_for_do_while",
    
    # OTHER CONTROL-FLOW
    r"\b(while|while loop|while in java)\b": "while_loop",
    r"\b(do while|do while loop|do-while loop|do while in java)\b": "do_while_loop",
    r"\b(switch statement|switch|switch in java)\b": "switch_statement",
    r"\b(break statement|break|break in java)\b": "break_statement",
    r"\b(continue statement|continue|continue in java)\b": "continue_statement",
    r"\b(labeled break|labelled break)\b": "labeled_break",
    r"\b(labeled continue|labelled continue)\b": "labeled_continue",
    r"\b(difference between while and do while|difference between do while and while|while vs do while|do while vs while)\b": "difference_while_do_while",
}

# Defining the get_response function 
def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    # Create a list to store all matches
    matches = []
    # Check for all matching patterns and store them
    for pattern, response_key in patterns.items():
        # Use re.findall to find all matches
        found_matches = re.findall(pattern, user_input)
        # If there are matches add them to the list
        if found_matches:
            for match in found_matches:
                if isinstance(match, tuple):  
                    match = match[0]  
                matches.append((response_key, match, len(match)))
    
    #return the response for the longest matched text
    if matches:
        # Sort the matches based on the length of the matched text
        matches.sort(key=lambda x: x[2], reverse=True)
        best_match = matches[0][0] 
        
        # Check if the best match is "bye"
        if best_match == "bye":
            return responses["bye"]
        return responses[best_match]
    
    return responses["default"]

# Defining the chatbot function
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    # Start a loop to keep the conversation going
    while True:
        # Get user input
        user_input = input("You: ")
        response = get_response(user_input)

        # Check if the response is "bye"
        if response == responses["bye"]:
            print("Chatbot:", response)
            break

        print("Chatbot:", response)
                
# Main function
if __name__ == "__main__":
    chat()
