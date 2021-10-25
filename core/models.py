from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    CHOICES=(
        ("Travel", "Travel"),
        ("Sport", "Sport"),
        ("Nature", "Nature"),
    )
    image=models.ImageField(upload_to="blog/images")
    title = models.CharField(max_length=100)
    blog_texts=models.TextField(max_length=3000)
    category=models.CharField(choices=CHOICES, max_length=10)
    date_posted=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment=models.TextField(max_length=2000)
    date_posted=models.DateField(auto_now_add=True)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

