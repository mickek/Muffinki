from django.db import models

# Create your models here.

class Przepis(models.Model):
	title = models.CharField(max_length = 512, default='')
	url = models.CharField(max_length = 512, default='', unique = True)
	ingredients = models.TextField(default='')
	content = models.TextField(default='')
