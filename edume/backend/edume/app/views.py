from django.shortcuts import render, redirect
from django.core import validators
# Create your views here.
from .forms import UserForm
from django.forms.models import model_to_dict


def main(request):
    data = request.session.get('data')
    new_user = None
    user = None

    if data is not None:
        if 'new_user' in data:
            new_user = data['new_user']

        if 'user' in data:
            user = data['user']

    return render(request, 'edume/main.html', {'new_user': new_user, 'user': user})


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.POST.get('name')
            user.surname = request.POST.get('surname')
            user.email = request.POST.get('email')
            user.birth_date = request.POST.get('birth_date')
            user.password = request.POST.get('password')
            second_pass = request.POST.get('second_pass')
            user.save()
            request.session['data'] = {'new_user': 'True', 'user': model_to_dict(user)}
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'edume/login.html', {'form': form})
