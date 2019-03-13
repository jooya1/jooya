from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import modelformset_factory


class Things(models.Model):

    description = models.CharField(max_length=4000)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='things')
    image = models.ImageField(upload_to='things_pic', blank=True)
'''
@login_required
def AddNewThing(request):
    ThingsFormSet = modelformset_factory(Things, fields=('name', 'price', 'category'), extra=0)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Product.objects.filter(user=request.user))
    for form in formset:
        form.fields['category'].queryset = Category.objects.filter(user=request.user)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('products_list')

    return render(request, 'products/products_formset.html', {'formset': formset})'''