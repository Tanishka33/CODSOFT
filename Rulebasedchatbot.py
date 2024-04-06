import re

# Define patterns and responses
patterns_responses = {
    r'hi|hello|hey': 'Hello! How can I assist you today?',
    r'do you know what codsoft is':'CodSoft are IT services and IT consultancy that specializes in creating innovative solutions for businesses.',
    r'how are you feeling today|how was your mood today':'well I really enjoyed today , talking with you',
    r'how are you|how are you doing': 'I am just a bot, but thanks for asking!',
    r'what is your name|who are you': 'I am a simple chatbot created for demonstration purposes.',
    r'bye|goodbye|see you later': 'Goodbye! Have a great day!',
    r'i love pizza':'ohh great i love pizza too',
    r'.*': "I'm sorry, I didn't understand that."
}


def respond(user_input):
    for pattern, response in patterns_responses.items():
        if re.match(pattern, user_input.lower()):
            return response
    return patterns_responses['.*']  # for Default responses


def main():
    print("Welcome! How can I assist you today? ")
    print("this simple chatbot is created for codsoft")
    print("if you wish to leave , kindly type 'bye' to exit")
    while True:
        user_input = input("Your response: ")
        if user_input.lower() == 'bye':
            print(respond(user_input))
            break
        else:
            print("Bot's response:", respond(user_input))

if __name__ == "__main__":
    main()
