def response(mood):
    mood = mood.lower()  # Convert mood to lowercase to make the program case-insensitive

    if mood == "happy":
        return "That's great to hear! Keep smiling!"
    elif mood == "sad":
        return "I'm sorry to hear that. I hope your day gets better."
    elif mood == "angry":
        return "Take a deep breath. Try to relax and count to three."
    elif mood == "excited":
        return "That's awesome! Keep that energy going drink more caffine!"
    elif mood == "tired":
        return "It sounds like you need a rest. Get in those pj's and sleep"
    elif mood == "bored":
        return "Maybe it's a good time to try a new video game!"
    else:
        return "I see. Take care of yourself!"