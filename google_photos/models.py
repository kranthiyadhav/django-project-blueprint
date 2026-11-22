from django.db import models

class Googlephotos(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    