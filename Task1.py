import re

def chatbot():
    while True:
        user_input = input("You: ").lower()
        
        if re.search(r'\bhello\b|\bhi\b', user_input):
            print("Bot: Hello! How can I help you today?")
        elif re.search(r'\bhow are you\b', user_input):
            print("Bot: I'm doing great, thank you! How about you?")
        elif re.search(r'\bbye\b', user_input):
            print("Bot: Goodbye! Have a nice day!")
            break
        elif re.search(r'\bname\b', user_input):
            print("Bot: I am a simple chatbot.")
        elif re.search(r'\bthanks\b|\bthank you\b', user_input):
            print("Bot: You're welcome!")
        elif re.search(r'\bweather\b', user_input):
            print("Bot: I'm not sure about the weather, but I hope it's nice!")
        else:
            print("Bot: I'm sorry, I didn't understand that.")

chatbot()
