from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("I am learning Django")