from django import forms
from .models import User


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    surname = forms.CharField(max_length=200)
    birth_date = forms.DateField(widget=forms.TimeInput(attrs=
    {
        'type': 'date'
    }))
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    second_password = forms.CharField(max_length=200, widget=forms.PasswordInput, label="Re-type password")
    bio = forms.CharField(max_length=1000, widget=forms.Textarea())

    def clean_second_password(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('second_password')
        if pass1 != pass2:
            raise forms.ValidationError("Passwords are not matched")
        return pass1

    class Meta:
        model = User
        fields = ('name', 'surname', 'birth_date', 'email', 'bio', 'password')
