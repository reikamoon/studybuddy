from django.shortcuts import render
import requests
from .models import Assignment

# Create your views here.
def index(request):
    assignments_list = Assignment.objects.order_by('-due_date')[:5]
    context = {'assignments_list': assignments_list}
    return render(request, 'assignments/index.html', context)
