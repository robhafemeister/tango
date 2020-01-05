from django.http import HttpResponse



# Views

def index(request):
    return HttpResponse("Rango says hey there partner!")
    

