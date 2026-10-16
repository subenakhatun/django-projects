from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Shop Home page")

def products(request):
    return HttpResponse("Shop products page")


    