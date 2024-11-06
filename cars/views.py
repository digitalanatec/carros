# Create your views here.
from django.http import HttpResponse

def cars_view(request):
    return HttpResponse("Meus Carros")