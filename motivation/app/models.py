from django.db import models


class quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)