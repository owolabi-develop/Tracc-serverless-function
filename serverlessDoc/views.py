from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"serverlessDoc/index.html",{})

def SlackDoc(request):
    return render(request,"serverlessDoc/SlackDoc.html")
