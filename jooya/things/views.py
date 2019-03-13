from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Things
from .forms import ThingsForm

# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    return render(request, 'things/index.html')

#@login_required
def AddNewThing(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = ThingsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.user = request.user
            thing.image = request.FILES['image']
            thing.description = request.description
            file_type = thing.album_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'thing': thing,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'things/index.html', {'thing': thing})
            thing.save()
        context = {
                "form": form,
            }
        return render(request, 'things/AddThing.html', context)
        #return render(request, 'things/AddThing.html')