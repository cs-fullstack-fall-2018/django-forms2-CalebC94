from django.shortcuts import render

from .forms import RecipesForm

from .models import FormModel



def recipes_create(request):
    form = RecipesForm(request.POST)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'forms_app/recipes_create.html', context)

def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)