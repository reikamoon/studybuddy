from django.db import models

# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length = 25)
    assignment_link = models.URLField(max_length=200)
    due_date = models.DateField()
    dropbox = models.URLField(max_length = 200)

    def __str__(self): #Return Name on Dashboard
        return self.assignment_name

    class Meta: #Plural vers of Assignments
        verbose_name_plural = 'Assignments'
