from datetime import datetime

from django.shortcuts import render, redirect
from .forms import UserForm
from django.forms.models import model_to_dict

from .models import Topic, User, Course, Chapter, Question, Answer


def select_topics(request):
    if request.method == "POST":
        return add_selected_topics(request)
    else:
        return view_select_topics(request)


def view_select_topics(request):
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


def add_selected_topics(request):
    if 'selected_topics' in request.POST:
        selected_topics = request.POST.getlist('selected_topics')
        if selected_topics:
            user_id = request.session.get('data')['user']['id']
            user = User.objects.get(id=user_id)
            topics = Topic.objects.filter(id__in=selected_topics)
            user.topics.set(topics)
            user.save()
            request.session['topics'] = selected_topics

    return redirect('courses')


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


def courses(request):
    if request.method == "POST":
        return select_a_course(request)
    else:
        return view_courses(request)


def view_courses(request):
    topics = Topic.objects.filter(id__in=request.session['topics'])
    course_list = Course.objects.filter(topics__in=topics).distinct()
    return render(request, 'edume/courses.html', {'courses': course_list, 'user': request.session['data']['user']})


def select_a_course(request):
    request.session['course_id'] = request.POST['selected_course']
    return redirect('course')


def course(request):
    if request.method == "POST":
        return select_a_chapter(request)
    else:
        if request.GET.get('forum') == 'forum':
            return redirect('forum')
        else:
            return view_the_course(request)


def select_a_chapter(request):
    request.session['chapter_id'] = request.POST['selected_chapter']
    return redirect('chapter')


def view_the_course(request):
    selected_course = Course.objects.get(id=request.session['course_id'])
    topics = selected_course.topics.all()
    chapters = Chapter.objects.filter(course_id=request.session['course_id'])
    return render(request, 'edume/course.html', {'course': selected_course,
                                                 'user': request.session['data']['user'],
                                                 'topics': topics,
                                                 'chapters': chapters})


def chapter(request):
    selected_chapter = Chapter.objects.get(id=request.session['chapter_id'])
    return render(request, 'edume/chapter.html', {'chapter': selected_chapter})


def forum(request):
    if request.method == "POST":
        if 'submit_answer' in request.POST:
            answer = Answer()
            answer.answered_user = request.session['data']['user']['name']
            answer.answer = request.POST['answer']
            answer.question = Question.objects.get(id=request.POST['submit_answer'])
            answer.save()
            return redirect('forum')

        elif 'submit_question' in request.POST:
            question = Question()
            question.asked_user = request.session['data']['user']['name']
            question.question = request.POST['question']
            question.course = Course.objects.get(id=request.session['course_id'])
            question.save()
            return redirect('forum')
    else:
        return view_forum(request)


def view_forum(request):
    questions = Question.objects.filter(course_id=request.session['course_id'])
    for question in questions:
        question.answers = question.answer_set.all()

    return render(request, 'edume/forum.html', {'questions': questions})
