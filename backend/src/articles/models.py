from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=129)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
