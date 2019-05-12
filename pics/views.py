from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture

# Create your views here.

def posted_pics(request):
    
    pics = Picture.objects.all()
    
    return render(request, 'pic/index.html', {"pics":pics})