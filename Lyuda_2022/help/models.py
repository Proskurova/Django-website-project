from django.db import models


class Question(models.Model):
    author = models.CharField(max_length=35)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

