import random
import time

class CustomerServiceChatbot:
    def __init__(self):
        # Predefined greetings
        self.greetings = ["Hi! How can I assist you today?", "Hello! How can I help you?", "Hey there! Need any help?"]

        # Frequently asked questions (FAQs) and their answers
        self.faqs = {
            "What are your store hours?": "Our store is open 24/7 online!",
            "Where are you located?": "We're an online store, so you can shop from anywhere!",
            "What is your return policy?": "We accept returns within 30 days of purchase, as long as the item is in original condition.",
            "How do I track my order?": "You can track your order by visiting the 'My Orders' section on our website."
        }

        # Goodbye messages
        self.goodbye = ["Goodbye! Thank you for visiting!", "Take care and have a great day!", "Thanks for chatting with us!"]

    # Function to start the conversation
    def start_conversation(self):
        print(random.choice(self.greetings))  # Greet the user
        time.sleep(1)

        while True:
            # Taking user input
            user_input = input("You: ").strip().lower()

            # If the user wants to exit the chat
            if user_input in ["exit", "quit", "bye", "goodbye"]:
                print(random.choice(self.goodbye))  # Respond with a goodbye message
                break

            # If the user asks about an order
            elif "order" in user_input:
                print("Sure! Could you please provide your order number?")

            # If the user asks a question from the FAQ list
            elif any(faq.lower() in user_input for faq in self.faqs.keys()):
                for question, answer in self.faqs.items():
                    if question.lower() in user_input:
                        print(answer)
                        break

            # If the bot doesn't understand the user's query
            else:
                print("I'm not sure how to help with that. Could you please rephrase your question?")

# Running the chatbot
if __name__ == "__main__":
    chatbot = CustomerServiceChatbot()
    chatbot.start_conversation()
