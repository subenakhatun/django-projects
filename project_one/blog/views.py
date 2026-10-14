from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Blog Home page")

def about(request):
    return HttpResponse("Blog About page")