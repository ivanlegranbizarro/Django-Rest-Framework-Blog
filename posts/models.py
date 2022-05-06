from django.db import models
from autoslug import AutoSlugField
from categorias.models import Category
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    miniature = models.ImageField(
        upload_to='posts/img/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
