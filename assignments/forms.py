from django.forms import ModelForm, TextInput
from .models import Assignment

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_link', 'description', 'due_date', 'dropbox']
        widgets = {
            'assignment_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter assignment name'}),
        } #updates the input class to have the correct Bulma class and placeholder
