import datetime
import random

def get_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "greetings", "what's up"]
    farewells = ["bye", "exit", "goodbye", "see you"]
    weather_queries = ["weather", "temperature", "forecast"]
    time_queries = ["time", "date"]
    small_talk_queries = ["your name", "joke", "how are you", "you do"]
    faq_queries = {
        "hours": "We are open from 9 AM to 5 PM, Monday to Friday.",
        "location": "We are located at 123 Chatbot Lane, AI City.",
        "contact": "You can contact us at chatbot@example.com."
    }

    if any(greet in user_input for greet in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey!", "Greetings!", "What's up?"])
    
    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a nice day!"
    
    elif any(weather in user_input for weather in weather_queries):
        return "The current weather is sunny with a high of 25°C."

    elif any(time_query in user_input for time_query in time_queries):
        now = datetime.datetime.now()
        if "time" in user_input:
            return f"The current time is {now.strftime('%H:%M:%S')}."
        elif "date" in user_input:
            return f"Today's date is {now.strftime('%Y-%m-%d')}."
    
    elif "help" in user_input:
        return ("You can ask me about the weather, time, date, tell me a joke, ask for our hours, location, or contact info. "
                "You can also say 'bye' to exit.")
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    
    elif "your name" in user_input:
        return "I'm a Chatbot created to assist you."
    
    elif "joke" in user_input:
        return random.choice([
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why was the math book sad? Because it had too many problems."
        ])

    elif any(faq in user_input for faq in faq_queries.keys()):
        for faq, response in faq_queries.items():
            if faq in user_input:
                return response

    # Basic sentiment analysis
    elif "happy" in user_input or "good" in user_input or "great" in user_input:
        return "I'm glad to hear that! How can I assist you further?"
    elif "sad" in user_input or "bad" in user_input or "not good" in user_input:
        return "I'm sorry to hear that. Is there anything I can do to help?"

    # Basic math operations
    elif "calculate" in user_input:
        try:
            # Extract and evaluate the expression
            expression = user_input.split("calculate")[1]
            result = eval(expression)
            return f"The result is {result}."
        except:
            return "I couldn't calculate that. Please provide a valid expression."

    else:
        return "Sorry, I didn't understand that. Can you please rephrase or type 'help' for assistance?"

def main():
    print("Welcome to the Advanced Rule-Based Chatbot! Type 'help' for a list of commands or 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if "bye" in user_input or "exit" in user_input:
            break

if __name__ == "__main__":
    main()
