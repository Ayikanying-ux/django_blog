from django import views
from django.urls import path

from core.views import AboutView, ContactView, CreatePostView, HomeListView, PostDetailView, SearchResultsView
urlpatterns=[
    path("", HomeListView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('create_blog/', CreatePostView.as_view(), name="create_posts"),
    path('contact/', ContactView.as_view(), name="contact"),
    path("<str:pk>/", PostDetailView.as_view(), name="post_detail"),
]