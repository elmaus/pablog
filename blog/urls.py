
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('blog/', views.BlogView.as_view(), name='blog-blog'),
    path('poetry/', views.PoetryView.as_view(), name='blog-poetry'),
    path('fiction/', views.FictionView.as_view(), name='blog-fiction'),
    path('nonfiction/', views.NonfictionView.as_view(), name="blog-nonfiction")
]
