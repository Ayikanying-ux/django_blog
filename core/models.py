from django.db import models
from django.shortcuts import reverse

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