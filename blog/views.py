from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Book


ALL_BOOKS = Book.objects.all()

def home(request):
    context = {
        'title':'Home',
        'text':'This is a text',
        'stories': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['books'] = ALL_BOOKS

        return context

    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['books'] = ALL_BOOKS

        return context

    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category='blog')

class PoetryView(ListView):
    model = Post
    template_name = 'blog/poetry.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Poetry'
        context['books'] = ALL_BOOKS

        return context

    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category='poetry')

class FictionView(ListView):
    model = Post
    template_name = 'blog/fiction.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Fiction'
        context['books'] = ALL_BOOKS

        return context
    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category='fiction')

class NonfictionView(ListView):
    model = Post
    template_name = 'blog/nonfiction.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NonFiction'
        context['books'] = ALL_BOOKS

        return context
    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category='nonfiction')



    