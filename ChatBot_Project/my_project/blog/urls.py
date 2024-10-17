from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.index, name = 'index'),
    # url's that send the data from the frontend to the backend
    path('getResponse', views.getResponse, name='getResponse')

]


