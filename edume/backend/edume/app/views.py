from datetime import timezone

from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserForm


def main(request):
    return render(request, 'edume/main.html', {})


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(request)
            user = form.save(commit=False)
            user.name = request.POST.get('name')
            user.surname = request.POST.get('surname')
            user.birth_date = request.POST.get('birth_date')
            user.save()
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'edume/login.html', {'form': form})