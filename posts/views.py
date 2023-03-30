from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *

class Home(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"


class Detail_page(DetailView):
    model = Post
    template_name = "detail_page_view.html"
