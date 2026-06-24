print("===== AI CHATBOT =====")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user:
        print("Bot: I am AI Chatbot.")

    elif "course" in user:
        print("Bot: I can answer simple questions.")

    elif "python" in user:
        print("Bot: Python is a programming language.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand.")