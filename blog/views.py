from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


def home(request):
    context = {
        'title':'Home',
        'text':'This is a text',
        'categories': Category.objects.all()
    }
    return render(request, 'blog/home.html', context)
