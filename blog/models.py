from django.db import models

# Create your models here.
from django.urls import reverse

from authentication.models import User


class Snippet(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    snippet_code = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title},{self.snippet_code[:40]}'

    @property
    def get_absolute_url(self):
        return reverse('snippet_detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'snippets'
        verbose_name = 'snippet'
        verbose_name_plural = 'snippets'
