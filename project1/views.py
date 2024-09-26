from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse("I am learning Django")

def testPage(request):
    return HttpResponse("<b>This will be a test page.</b>")

def archetype(request):
    return HttpResponse("Here you can choose the archetypes of your player")

#here we can use the db to specifically get our response wrt the id specified (int as specified n the field corresponding url) 

def archetypeDetails(request, archetypeId):
    return HttpResponse(archetypeId)