from django.urls import path
from . import views 

urlpatterns = [ 
    # Creating url --> it takes 3 parameters : 1) url itself(empty means main of blog app)
    #                                          2) view or file or function we want to execute <.index is the name of the function>
    #                                          3) name of the url 
    path('', views.index, name = 'index'),
    path('get-response/', views.getResponse, name='get_response'),  

    # path('specific', views.specific, name = 'sepcific'),
    # path('sample', views.sample, name = 'sample'),

    # path('article/<int:article_id>', views.article, name = 'article'),

    # path('test/<int:test_id>', views.test, name = 'test'),

    # # url's that send the data from the frontend to the backend
    # path('getResponse', views.getResponse, name='getResponse')

]


# Next step is to tell our project that we have the above url
# Go to urls.py in project level, and tell django that we have an app called "blog" and it has urls



# After that we have to create a function that will be executed upon going to the above defined url
# Go to views.py in app level and create the function "index"


# Now we want to know how to pass a parameter in the url <article path example>
# Frist create the url as above
# Then go to the views.py file and create a view which recieve a parameter in addition to the request
# This allow users to pass parameter and get specific data



# Now we want to know how to return html code 
# To create an html fie=le, we need to go to our specific app we are working on and create a folder 
# as follow : blog --> template<folder> --> blog<folder> --> html<file>
# To return it to the user, in the views.py file, instead of returning HttpResponse, we will return "render" function 
# which takes 3 parameters : 1- request 
#                            2- file we want to return<blog/index.html> (blog is the name of the folder that html file saved)
#                            3- any parameter we want like article_id <{'key' : value}> 
# render function must be imported
# Finally we need to define the app in settings.py --> INSTALLED_APPS  in project level <'blog.apps.BlogConfig',>




# Now we want to know how to add CSS into our project and make the page we created look better
# To do it, first create a folder inside the app called "static" and inside it create another forlder with same name 
# as the app_name. Then create a file "style.css" inside it
# To add this style to the html file we had, we need to use following syntax in the head tag of the html file : 

#                        {% load static %}
#                        <link rel="stylesheet" type="text/css" href="{% static 'blog/style.css '%}" /> 

# Do not forget to RESTART THE SERVER 



# Now we want to work on the user interface --> go to index.html

# Now, to make it look better, we need to work on its CSS


# Now we want to add "JQuery" into our project. <It’s a tiny helper that makes it simple to tell the website what to
# do—like show pictures, hide things, or move stuff around—without writing a lot of code. It's like a shortcut for 
# making websites more fun and interactive!>

# Now, in order to get the text from the user, we want to use jQuery. Go to index.html file and create a script at the
# end of the code. <Create a function that gonna take the text from the user inside that script>




# So far, what we did were all frontend works. Now we want to take this input from the use and send to Django(Python) to do 
# somthing with it. <send it from frontend to the backend>
 

# After that we need to install a few libraries in CMD : 
# 
# 1) chatterbot  
# 2) chatterbot-corpus 
# 3) pyyaml #python -m spacy download en  
# 4) spacy
# 5) jupyter
# 6) flask 


# Now we need to create an object of the chatbot 

# Now we need to train our chatbot to response to the user < very very important >


# After training our chatbot, we need to change the return message. < Right now the user message will be returned. While
# we want to get the message from the chatbot >


# Now suppose the user asked a question which was not in the "List_of_train". We can leave the user with no answer. To 
# fix this we can use "default response" --> change the logic_adapter

# the chatbot is very smart, so the question similar to what we defined for train also give the same answer to us
# <it able to predict the answer>

# If we want to have a lot of conversations, it will be cumbersome. Fortunately this library provides us with conversations
# that other people have already created <import ChatterBotCorpusTrainer>



# As many time as we train our chatbot, as smarter it will be   
# When we use chatterBotCurpos, it is better to remove the default response to do not intrupt it

# We can also use other languages for our chatbot. <change english to any other language, but consider that other 
# languages will not contain as much conversation as english>



# where is the memory 






# what is the data format ? The format of data is defined based on the requirements and design of 
# the AI system you are using. It typically depends on several factors, such as the type of AI model,
# the programming framework, the purpose of the application. 
# When using the ChatterBot library in your project, the compatible data format is primarily text-based 
# because ChatterBot is designed to handle conversational AI models that work with text input and output.