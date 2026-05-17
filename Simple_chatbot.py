print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit the chat.\n")

while True:

    user = input("You: ").lower()
    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is PyBot.")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "what can you do":
        print("Bot: I can chat with you and answer simple questions.")

    elif user == "your favorite color":
        print("Bot: I like blue.")

    elif user == "your favorite food":
        print("Bot: I don't eat food, but pizza sounds tasty!")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "i am sad":
        print("Bot: I hope things get better soon.")

    elif user == "i am happy":
        print("Bot: That's great to hear!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user == "good night":
        print("Bot: Good night! Sleep well.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")