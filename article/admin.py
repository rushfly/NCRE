from django.contrib import admin
from article.models import Lesson, Student, Score, Teacher


admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Teacher)