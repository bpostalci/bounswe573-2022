from datetime import datetime

from django.shortcuts import render, redirect
from django.core import validators
# Create your views here.
from .forms import UserForm
from django.forms.models import model_to_dict

from .models import Topic, User


def select_topics(request):
    if request.method == "POST":
        return select_topics_submit(request)
    else:
        return select_topics_view(request)


def select_topics_view(request):
    data = request.session.get('data')
    new_user = None
    user = None
    topics = Topic.objects.filter()

    if data is not None:
        if 'new_user' in data:
            new_user = data['new_user']

        if 'user' in data:
            user = data['user']

    return render(request, 'edume/select_topics.html', {'new_user': new_user, 'user': user, 'topics': topics})


def select_topics_submit(request):
    if 'selected_topics' in request.POST:
        selected_topics = request.POST.getlist('selected_topics')
        if selected_topics:
            user_id = request.session.get('data')['user']['id']
            user = User.objects.get(id=user_id)
            topics = Topic.objects.filter(id__in=selected_topics)
            user.topics.set(topics)
            user.save()

    return redirect('main')


def main(request):
    data = request.session.get('data')
    user = None

    if data is not None:
        if 'user' in data:
            user = data['user']

    return render(request, 'edume/main.html', {'user': user})


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.POST.get('name')
            user.surname = request.POST.get('surname')
            user.email = request.POST.get('email')
            user.birth_date = request.POST.get('birth_date')
            user.create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.password = request.POST.get('password')
            second_pass = request.POST.get('second_pass')
            user.bio = request.POST.get('bio')
            user.save()
            request.session['data'] = {'new_user': 'True', 'user': model_to_dict(user)}
            return redirect('select_topics')
    else:
        form = UserForm()
    return render(request, 'edume/login.html', {'form': form})
