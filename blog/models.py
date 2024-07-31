from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})
