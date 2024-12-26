"""
Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, 
both built-in and custom, and to apply data handling techniques using Python's data structures and error handling.

Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how 
they are feeling today and responds with a custom message based on the mood entered.
"""

import mood_responder

def main():
    user_mood = input("How are you feeling today? (Happy, Sad, Excited, etc.): ")

    response = mood_responder.response(user_mood)

    print(response)

if __name__ == "__main__":
    main()