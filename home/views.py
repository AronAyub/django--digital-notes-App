from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Troubleshooting the page ")
    return render(request, 'home/welcome.html', {})

    #return render(request,'home/welcome.html', {})
