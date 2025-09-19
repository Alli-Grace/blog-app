
from django.db import models
from datetime import datetime
from account.models import CustomUser
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author', default=1)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    # commentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_by')
    name = models.CharField(max_length=20)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(default='This is the default')
    created_at = models.DateTimeField(default=datetime.now)
    # active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.name}'