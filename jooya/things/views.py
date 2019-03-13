from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'things/index.html')


def dashboard(request):
    return render(request, 'things/dashboard.html')
