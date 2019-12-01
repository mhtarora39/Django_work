from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

PageTemplate = 'pages/'

def index(request):
  return render(request,PageTemplate+'index.html')

def about(request):
  return render(request,PageTemplate+'about.html')