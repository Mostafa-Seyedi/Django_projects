from django.urls import path
from . import views 

urlpatterns = [ 
    # Creating url --> it takes 3 parameters : 1) url itself(empty means main of blog app)
    #                                          2) view or file or function we want to execute <.index is the name of the function>
    #                                          3) name of the url 
    path('', views.index, name = 'index'),
    # url's that send the data from the frontend to the backend
    path('getResponse', views.getResponse, name='getResponse')

]


