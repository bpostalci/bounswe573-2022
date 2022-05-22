from django.db import models
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=200)
    syllabus = models.CharField(max_length=1000)
    create_date = models.DateTimeField(default=timezone.now)
    topics = models.ManyToManyField(Topic)

    def publish(self):
        self.save()


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    birth_date = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    topics = models.ManyToManyField(Topic)
    courses = models.ManyToManyField(Course)
    bio = models.CharField(max_length=500, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' ' + self.surname


class Question(models.Model):
    asked_user = models.CharField(max_length=400)
    question = models.CharField(max_length=300)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()


class Answer(models.Model):
    answered_user = models.CharField(max_length=400)
    answer = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()
