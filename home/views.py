from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    #return HttpResponse("Troubleshooting the page ")
    return render(request, 'home/welcome.html', {'today': datetime.today()})

    #return render(request,'home/welcome.html', {})
