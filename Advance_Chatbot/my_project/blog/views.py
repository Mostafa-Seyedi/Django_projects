from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

from .custom_adapters import OpenAILogicAdapter
import os
import openai

import spacy
nlp = spacy.load("en_core_web_sm")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# creating an object of chatbot <takes 3 parameter: name of the chatbot, read_only, and the logic>

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY','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')

bot = ChatBot(
    'My AI Assistant',
    read_only=False,
    logic_adapters= [
        'chatterbot.logic.BestMatch',
        'blog.custom_adapters.OpenAILogicAdapter' # include the custom openAI adapter
        
        # 'default_response':'Sorry, I do not know what that means',
        # 'maximum_similarity_threshold':0.90 
        # if the similariy was less that this number the default response will
        # be sent. <some of reduce the sensativity>
        ],

    storage_adapter='chatterbot.storage.SQLStorageAdapter',  
    database_uri='sqlite:///db.sqlite3',
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

# chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')  # Train the chatterbot with poeple conversations


def get_openai_response(self, user_input, conversation_history): 
    full_prompt = conversation_history + "\nUser: " + user_input + "\nAI:" 
    response = openai.Completion.create( engine="text-davinci-003", prompt=full_prompt, max_tokens=150, n=1, stop=None, temperature=0.7, ) 
    return response.choices[0].text.strip()


chatbot = ChatBot('My AI Assistant', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///db.sqlite3')

def getResponse(request):
    if request.method == 'POST':
        userMessage = request.POST.get('userMessage')
        
        if userMessage:  # Check if userMessage is not empty
            try:
                # Get response from ChatterBot
                chatResponse = str(bot.get_response(userMessage))

                # You might want to integrate OpenAI response here as well
                # Assuming conversation_history is managed correctly
                # This could be a list of past interactions or a string
                conversation_history = ""  # Modify this to track conversation history
                openaiResponse = get_openai_response(userMessage, conversation_history)

                # Combine responses from ChatterBot and OpenAI if needed
                combined_response = f"ChatterBot: {chatResponse}\nOpenAI: {openaiResponse}"

                return JsonResponse({"response": combined_response})
            except Exception as e:
                return JsonResponse({"error": str(e)})
        else:
            return JsonResponse({"error": "No message received."})
    return JsonResponse({"error": "Invalid request method."})



def index(request):
    # HttpResponse take what ever we want to return
    # return HttpResponse("This is my first url")
    return render(request, 'blog/index.html')


print("OpenAI API Key:", OPENAI_API_KEY)  # For debugging; remove in production


# def specific(request): 
#     return HttpResponse("This is a specific url")

# # ---------------------------------------------------------------------


# # We can pass any type of data to the page(user) through view

# def sample(request): 
#     # number = 10
#     list = ['alex ', 'ryan ' , 'luca']
#     return HttpResponse(list)

# # ----------------------------------------------------------------------

# def article(request, article_id): 
#     return HttpResponse(article_id)

# # ----------------------------------------------------------------------

# def test (request, test_id): 
#     return render(request, 'blog/index.html', {'test':test_id})

# # ----------------------------------------------------------------------

