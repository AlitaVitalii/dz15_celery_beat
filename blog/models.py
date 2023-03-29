from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return self.quote[:15]
