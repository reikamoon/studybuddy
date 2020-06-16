from django.shortcuts import render
import requests
from .models import *

# Create your views here.
def index(request):
    return render('assignments/index.html')
