
name = input("Hi! What's your name? ")
print("Nice to meet you,", name)

while True:
    message = input("You: ").lower()  # Get user input and make it lowercase

    if message == "hello":
        print("Bot: Hello! How can I help you?")
    elif message == "how are you?":
        print("Bot: I'm just code, but I'm doing great!")
    elif message == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
