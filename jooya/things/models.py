from django.db import models
from django.contrib.auth.models import User
from .search import ThingIndex


class Things(models.Model):

    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=4000)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='things')
    image = models.ImageField(upload_to='things_pic', blank=True)

    # Method for indexing the model
    def indexing(self):
        obj = ThingIndex(
            meta={'id': self.id},
            user=self.user.username,
            date_added=self.date_added,
            title=self.title,
            image=self.image.url,
            description=self.description
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    # Method for deleting the model
    def deleting(self):
        obj = ThingIndex(
            meta={'id': self.id},
            user=self.user.username,
            date_added=self.date_added,
            title=self.title,
            image=self.image.url,
            description=self.description
        )
        obj.delete()
        return obj.to_dict(include_meta=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.title


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