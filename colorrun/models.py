from django.db import models

class color(models.Model):
    color_name = models.CharField(max_length=100,primary_key=True)
    code = models.CharField(max_length=100)