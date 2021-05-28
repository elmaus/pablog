from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title':'Home',
        'text':'This is a text'
    }
    return render(request, 'blog/home.html', context)
