from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse_lazy
from .models import Assignment, Class
from .forms import AssignmentForm
from schedule.models import Class
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    assignments_list = Assignment.objects.order_by('-due_date')[:5]
    context = {'assignments_list': assignments_list}
    return render(request, 'assignments/index.html', context)

def schedule_index(request):
    schedule = Class.objects.order_by('class_name')[:5]
    context = {'schedule': schedule}
    return render(request, 'schedule/schedule_index.html', context)

class AssignmentDetailView(DetailView):
    model = Assignment
    def get(self, request, slug):
        """Returns a specific assignment by its slug"""
        assignment = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'assignment.html', {
            'assignment': assignment
        })

class CreateAssignment(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AssignmentForm()}
        return render(request, 'assignment_new.html', context)

    def post(self, request, *args, **kwargs):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse_lazy('home'))

class UpdateAssignment(UpdateView):
    model = Assignment
    fields = ['assignment_name', 'assignment_link', 'description', 'due_date', 'dropbox']
    template_name_suffix = '_update_form'

class DeleteAssignment(DeleteView):
    model = Assignment
    success_url = "/"

class ClassDetailView(DetailView):
    model = Class
    def get(self, request, slug):
        """Returns a specific class by its slug"""
        my_class = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'class.html', {
            'my_class': my_class
        })

class AddaClass(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ClassForm()}
        return render(request, 'class_new.html', context)

    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse_lazy('schedule'))

class UpdateClass(UpdateView):
    model = Class
    fields = ['class_name', 'class_link', 'days', 'time', 'syllabus', 'tracker', 'grades',]
    template_name_suffix = '_update_form'

class DeleteClass(DeleteView):
    model = Class
    success_url = "/schedule/"
