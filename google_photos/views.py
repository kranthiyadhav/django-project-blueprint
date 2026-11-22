from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the google photos app index.")
# Create your views here.
def photo(request):
    return render(request, 'photos/photo.html')