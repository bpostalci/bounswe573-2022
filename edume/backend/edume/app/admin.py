from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Chapter)
