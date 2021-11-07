from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import PostModel
from .forms import PostForm


class AboutView(TemplateView):
    template_name = 'post/about.html'


class PostView(ListView):
    model = PostModel
    template_name = 'post/all_posts.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetailView(DetailView):
    model = PostModel
    context_object_name = 'artyom'


class PostCreateView(CreateView):
    model = PostModel
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('posts-home')


class PostUpdateView(UpdateView):
    model = PostModel
    template_name = 'post/postmodel_form.html'
    form_class = PostForm
    success_url = 'myfirstapp-home'


class PostDeleteView(DeleteView):
    model = PostModel
    success_url = 'posts-home'


# def movies_delete_view(request, id=None):
#     obj = get_object_or_404(ObjectModel, id=id)
#     creator = obj.user.username
#     if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
#         obj.delete()
#         return HttpResponseRedirect("/Blog/list/")


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    obj = get_object_or_404(GeeksModel, id = id)
    form = GeeksForm(request.POST or None, instance = obj)
    # save the data from the form and
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
