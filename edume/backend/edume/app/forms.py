from .models import User

from django import forms


class UserForm(forms.ModelForm):
    # name = forms.CharField(max_length=200)
    # surname = forms.CharField(max_length=200)
    # birth_date = forms.DateField(widget=forms.TimeInput(attrs=
    # {
    #     'type': 'date'
    # }))
    class Meta:
        model = User
        fields = ('name', 'surname', 'birth_date',)
