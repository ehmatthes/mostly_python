from django.http import HttpResponse

def index(request):
    msg = "Welcome to the Piano Store!"
    return HttpResponse(msg)

def about(request):
    msg = "About the Piano Store"
    return HttpResponse(msg)

def contact(request):
    msg = "Contact the Piano Store"
    return HttpResponse(msg)

def faq(request):
    msg = "Piano Store FAQ"
    return HttpResponse(msg)