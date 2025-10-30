from django.db import models

# Create your models here.
class PassageModel(models.Model):
    title = models.CharField(max_length=100)
    passage = models.TextField()