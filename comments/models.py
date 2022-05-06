from django.db import models
from users.models import User
from posts.models import Post
from autoslug import AutoSlugField


class Comment(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField(default='Default content')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
