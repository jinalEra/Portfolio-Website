from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'resumebuild/index.html')