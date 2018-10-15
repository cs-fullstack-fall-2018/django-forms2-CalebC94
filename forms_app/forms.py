from django import forms


from .models import FormModel


class RecipesForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = [
            'name',
            'recipe',
            'timeCook',
            'dateCreated'
        ]