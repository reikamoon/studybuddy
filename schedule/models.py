from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=200, help_text="Enter class name.")
    class_link = models.URLField(max_length=200, help_text="Add a link to class sessions (ex: Zoom)")
    syllabus = models.URLField(max_length=200, null=True, blank=True, help_text="[Optional]Add a link to the Syllabus.")
    tracker = models.URLField(max_length=200, null=True, blank=True, help_text="[Optional]Add a link to class tracker.")
    grades = models.URLField(max_length=200, null=True, blank=True, help_text="[Optional]Add a link to grades for this class.")
    slug = models.CharField(max_length=200, blank = True, editable = False,
    help_text = "Unique URL Path to access this page.")

    def __str__(self): #Return Name on Dashboard
        return self.class_name

    def get_absolute_url(self):
        """Returns a fully-qualified path for a page"""
        path_components = {'slug': self.slug}
        return reverse('assignment-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """Create a URL Safe slug automatically when a new assignment is created"""
        if not self.pk:
            self.slug = slugify(self.class_name, allow_unicode=True)

        #Call Save on the superclass
        return super(Class, self).save(*args, **kwargs)

    class Meta: #Plural vers of Assignments
        verbose_name_plural = 'Classes'
