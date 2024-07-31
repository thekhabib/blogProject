from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home_page')


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'blog/post_create.html'
