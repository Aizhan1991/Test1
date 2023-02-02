from django.db import models
from Test1.models import Post
# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=40)
    duration = models.PositiveIntegerField()
    category = models.ForeignKey(Post,
    on_delete=models.CASCADE,
    related_name='Test1')
