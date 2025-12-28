import json
import string

# Load intents
with open("data/intents.json", "r") as f:
    intents = json.load(f)

def preprocess_text(text):
    """
    Convert text to lowercase and remove punctuation
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def get_intent(tokens):
    """
    Match user tokens with intent keywords
    """
    for intent, data in intents.items():
        for keyword in data["keywords"]:
            if keyword in tokens:
                return intent
    return "unknown"

def chatbot():
    print("Chatbot started (type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        tokens = preprocess_text(user_input)
        intent = get_intent(tokens)

        if intent == "unknown":
            print("Bot: Sorry, I didn't understand that.")
        else:
            print("Bot:", intents[intent]["response"])

        if intent == "goodbye":
            break

if __name__ == "__main__":
    chatbot()

