from datetime import date

from django.db import models

# Create your models here.


class Myip(models.Model):
    ip_txt = models.CharField(max_length=15)
    # pubdate = models.DateField(auto_now_add=True)
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_txt
