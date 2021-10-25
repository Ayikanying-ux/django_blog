from django.http import request
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from . forms import BlogForms, CommentForm
from django.db.models import Q

from core.models import Blog, Comment
# Create your views here.
class HomeListView(View):
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.all()
        context={"blog": blog}
        return render(request, "blog/index.html", context)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/about.html")

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        form = CommentForm
        blog = Blog.objects.get(pk=pk)
        comment=blog.comment_set.all()
        context={"blog": blog, "form": form, "comment": comment}
        return render(request, "blog/post_detail.html", context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/contact.html")

class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = BlogForms
        context={
            "form": form
        }
        return render(request, "blog/create_post.html", context)
    
    def post(self, request, *args, **kwargs):
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

class SearchResultsView(View):
    def get(self, request, *args, **kwags): 
        query = self.request.GET.get('query')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        context={"object_list": object_list}
        return render(request, 'blog/search.html', context)
