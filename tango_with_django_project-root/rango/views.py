from django.http import HttpResponse



# Views

def index(request):
    return HttpResponse("Rango says hey there partner" "<br>" "<a href='/rango/about'>Link to About Page</a>")
def about(request):
    return HttpResponse("Rango says here is the about page." "<br>" "<a href='/'>Link to Home</a>")


