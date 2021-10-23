from django.shortcuts import render, redirect
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

def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            results = Blog.objects.filter(title_icontains=query)
            context={"results": results}
            return render(request, "blog/search.html", context)
        else:
            print("No information found")
            return request(request, "blog/search.html", {})
