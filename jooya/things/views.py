from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .search import *
from .models import Things
import time
from .forms import ThingsForm
from django.contrib.auth.models import User
from .filters import UserFilter

# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):

    q = request.GET.get('q')

    if q:
        posts = Search().query("match", title=q)
    else:
        posts = ''

    return render(request, 'things/index.html', {'posts': posts})


#@login_required
def AddNewThing(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = ThingsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.title = request.POST.get('title')
            thing.description = request.POST.get('description')
            thing.image = request.FILES['image']
            thing.date_added = time.time()
            thing.user = request.user
            thing.save()
            response = redirect('../')
            return response
        context = {
                "form": form,
            }
        return render(request, 'things/AddThing.html', context)
        #return render(request, 'things/AddThing.html')


# def dashboard(request):
#
#     username = request.GET.get('username')
#     if User.objects.filter(username=username).exists():
#         print(User.objects.filter(username=username).all())
#
#     return render(request, 'things/dashboard.html')

def dashboard(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'things/dashboard.html', {'filter': user_filter})