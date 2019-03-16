from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .documents import ThingDocument
from .models import Things
import time
from .forms import ThingsForm
from .models import Things
# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):

    q = request.GET.get('q')

    if q:
        posts = ThingDocument.search().query("match", title=q)
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
            thing.date_added = time.time()
            thing.user = request.user
            thing.image = request.POST.get('image')
            thing.save()
            return render(request, 'things/dashboard.html')
        context = {
                "form": form,
            }
        return render(request, 'things/AddThing.html', context)
        #return render(request, 'things/AddThing.html')


def dashboard(request):
    return render(request, 'things/dashboard.html')

