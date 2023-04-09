from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# create ChatBot
chatBot = ChatBot('ChatBot')

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with English language corpus
# you can train with different language
# or with your custom .yam file
trainer.train("chatterbot.corpus.english.health")

# Greeting from chat bot
print("Hi, I am your Health Care Assistant")
print('It is necessary to note that each persons unique medical history, present state of health, and other circumstances will influence the specific medications and safety precautions that are advised for them. For personalized assistance, it is always more effective to consult with a medical expert.')

# keep communicating with ChatBot
while True:
    # take user input/query
    query = input(">>>")
    # response from ChatBot
    # put query on Statement format to avoid runtime alert messages
    # Statement(text=query, search_text=query)
    print(chatBot.get_response(Statement(text=query, search_text=query)))