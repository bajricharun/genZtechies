from django.db import models
from django.contrib.auth.models import User
import os


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

SECTION = (
    (0, "News"),
    (1, "Tips"),
    (2, "DIY Projects")
)


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    caption = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    section = models.IntegerField(choices=SECTION, default=0)
    image = models.ImageField(default='default.png')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
