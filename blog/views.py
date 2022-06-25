from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "base.html"

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "base.html"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    template_name = "base.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = "base.html"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "base.html"
    success_url = reverse_lazy("blog:all")