from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from . forms import BlogForms
from django.db.models import Q

from core.models import Blog
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
        blog = Blog.objects.get(pk=pk)
        context={"blog": blog}
        return render(request, "blog/post_detail.html", context)
    

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/contact.html")

class CreatePostView(View):
    template_name="blog/create_post.html"
    form_class=BlogForms

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context={
            "form": form
        }
        return render(request, "blog/create_post.html", context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

class SearchResultsView(generic.ListView):
    model = Blog
    template_name = 'blog/search.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('query')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        return object_list
