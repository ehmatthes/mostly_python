from django.http import HttpResponse

def about(request):
    for pattern in request.resolver_match.tried:
        print(pattern)
        
    msg = "About our synths"
    return HttpResponse(msg)

def faq(request):
    msg = "Synthesizer FAQ"
    return HttpResponse(msg)