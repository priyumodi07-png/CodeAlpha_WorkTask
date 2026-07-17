def chatbot():
    print("Simple Chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello there! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks for asking! How about you?")
        elif user_input in ["i am fine", "i'm good", "fine"]:
            print("Bot: That's wonderful to hear!")
        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm a simple chatbot created in Python.")
        elif user_input in ["what can you do", "help"]:
            print("Bot: I can chat with you, answer greetings, and keep you company!")
        elif user_input in ["tell me a joke", "joke"]:
            print("Bot: Why don’t programmers like nature? Too many bugs!")
        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: Hmm, I don't understand that. Try something else.")

chatbot()
