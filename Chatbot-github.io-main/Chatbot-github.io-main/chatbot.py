responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but thanks for asking!,how are you?",
    "what is your name": "I am a chatbot programmed by [Your Name].",

    # Add more responses here
}
def chatbot_response(user_input):
    user_input_lower = user_input.lower()

    for key in responses:
        if key in user_input_lower:
            return responses[key]

    return "I'm sorry, but I don't understand that. Can you please be more specific?"
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()