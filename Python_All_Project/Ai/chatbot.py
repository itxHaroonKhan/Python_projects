def simple_chatbot():
    print("Hello! I am a simple chatbot. Type something to start the conversation.")
    print("Type 'bye' to end the conversation.")

    # Dictionary of responses
    responses = {
        "hello": "Hello! How are you?",
        "who make you" : "I make by a Haroon Rasheed Developer",
        "who is haroon" : "Haroon is a good Developer",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm doing great, how about you?",
        "what are you doing": "I'm chatting with you!",
        "what is your name": "My name is SimpleBot.",
        "who are you": "I'm SimpleBot, your friendly chatbot assistant.",
        "bye": "Goodbye! See you later!"
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Bot:", responses[user_input])
            break

        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don't understand that. Please try asking something else.")

if __name__ == "__main__":
    simple_chatbot()
