from django.forms import ModelForm, TextInput
from .models import Class

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'class_link', 'days', 'time', 'syllabus', 'tracker', 'grades',]
        widgets = {
            'class_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter class name'}),
        } #updates the input class to have the correct Bulma class and placeholder
