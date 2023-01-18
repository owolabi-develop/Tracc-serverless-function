from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("SlackDocumentation/",views.SlackDoc,name='Slack')
    
]
