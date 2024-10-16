from django.shortcuts import render
from  django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")

# Create your views here.

# creating an object of chatbot <takes 3 parameter: name of the chatbot, read_only, and the logic>
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[{
        'import_path':'chatterbot.logic.BestMatch',
        # 'default_response':'Sorry, I do not know what that means',
        # 'maximum_similarity_threshold':0.90 
        # if the similariy was less that this number the default response will
        # be sent. <some of reduce the sensativity>
        }],

    storage_adapter='chatterbot.storage.SQLStorageAdapter',  
    tagger='chatterbot.tagging.SpacyTagger',
    language='en_core_web_sm',
)

# following list must have an even number of elements <1 Q and 1 A for each pair>
list_to_train = [
    "hi",  # question that might be asked by the user
    "Hi there! How can I assist you?", # Answer that the chatbot will 

    "Hello", 
    "Hello! What can I do for you today?",

    "How are you?", 
    "I'm just a chatbot, but I'm here and ready to help!",

    "What is your name?", 
    "I'm just a chatbot, here to assist you!",

    "What's your favorite food?", 
    "I like virtual pizza!",

    "Where are you from?", 
    "I'm from the digital world, created to assist you!",

    "Who created you?", 
    "I was created by developers to help people like you!",

    "How old are you?", 
    "I don't age, as I'm just a program!",

    "Tell me a joke", 
    "Why don't programmers like nature? It has too many bugs!",

]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')  # Train the chatterbot with poeple conversations

def index(request):
    # HttpResponse take what ever we want to return
    # return HttpResponse("This is my first url")
    return render(request, 'blog/index.html')


def getResponse(request): 
    userMessage = request.GET.get('userMessage')
    # return HttpResponse(userMessage)
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
