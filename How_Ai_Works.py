from textblob import Textblob
import colorama 
from colorama import Fore,Style
import sys
import time
user_name = ""
positive_count = 0
negative_count = 0
neutral_count = 0
def start_sentiment_chat():
    print(Fore.CYAN,"Hello and welcome to Sentiment Spy it's your personalized emotional detector")
    global user_name
    user_name = input("Please enter your name ?")
    print(Fore.CYAN,"Nice to meet you",user_name)
    while True:
        user_input = input("Enter a sentence to ananlyse your emotions if you wnat to exit please type exit")
        if user_input.lower() == "exit":
            break
        blob = Textblob(user_input)
        sentence = blob.sentiment.polarity
        if sentence > 0:
            print("Positive Emotion",sentence)
        elif sentence < 0:
            print("Negative Emotion",sentence)
        else:
            print("Neutral Emotion",sentence)
if __name__ == "__main__":
    start_sentiment_chat()
