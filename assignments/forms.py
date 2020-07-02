from django.forms import ModelForm, TextInput
from .models import Assignment, Class

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_link', 'description', 'due_date', 'dropbox']
        widgets = {
            'assignment_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter assignment name'}),
        } #updates the input class to have the correct Bulma class and placeholder

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'class_link', 'days', 'time', 'syllabus', 'tracker', 'grades',]
        widgets = {
            'class_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter class name'}),
        } #updates the input class to have the correct Bulma class and placeholder
