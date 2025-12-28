import json
import string
import nltk
from nltk.stem import WordNetLemmatizer


nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

# Load intents
with open("data/intents.json", "r") as f:
    intents = json.load(f)

def preprocess_text(text):
    """
    Lowercase, remove punctuation, tokenize, and lemmatize
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()


    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens

def get_intent(tokens):
    """
    Rule-based intent classification using lemmatized tokens
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
