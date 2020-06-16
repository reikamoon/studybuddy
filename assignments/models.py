from django.db import models

# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length = 25)
    assignment_link = models.URLField(max_length=200)
    due_date = models.DateField()
    dropbox = models.URLField(max_length = 200)
