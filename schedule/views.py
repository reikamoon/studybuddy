from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse_lazy
from .models import Class
from .forms import ClassForm
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.
def schedule_index(request):
    schedule = Class.objects.order_by('class_name')[:5]
    context = {'schedule': schedule}
    return render(request, 'schedule/schedule_index.html', context)

class ClassDetailView(DetailView):
    model = Class
    def get(self, request, slug):
        """Returns a specific class by its slug"""
        my_class = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'class.html', {
            'my_class': class
        })

class AddClass(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ClassForm()}
        return render(request, 'class_new.html', context)

    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse_lazy('home'))

class UpdateClass(UpdateView):
    model = Class
    fields = ['class_name', 'class_link', 'days', 'syllabus', 'tracker', 'grades',]
    template_name_suffix = '_update_form'

class DeleteClass(DeleteView):
    model = Class
    success_url = "/"
