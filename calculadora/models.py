from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=1000, default = None)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class PostModel (models.Model):
    title = models.CharField(max_length=1000, default = None)
    description = models.TextField(default = None)
    text = models.TextField(default = None)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateField(default = date.today)
    last_updated = models.DateField(auto_now=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.author} em {self.post.title}'