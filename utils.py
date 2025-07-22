def get_bot_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi": "Hello! I'm here to support your mental health. How are you feeling today?",
        "sad": "I'm sorry you're feeling this way. Would you like to talk about it?",
        "anxious": "It’s okay to feel anxious. Let’s do a short breathing exercise together.",
        "bye": "Take care. Remember, you're not alone."
    }
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm here to listen. Please share more about how you're feeling."