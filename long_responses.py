import random
from datetime import datetime
now = datetime.now()

R_NAME = "My Name Billy the Bot"
R_INTRO = "I am a robot"
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_DATE = "It's: "+now.strftime("%A %d/%m/%Y")
R_TIME = "It's: "+now.strftime("%H:%M:%S")
R_INFO = "In place of direct communication with a live human agent, a chatbot or chatterbot is a software application that conducts an online chat conversation using text or text-to-speech."
R_DOING = "Nothing, Just talking to you right now!"
R_INTERNET = "It's better to google that"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "It's better to google that",
                "What does that mean?"][
        random.randrange(4)]
    return response