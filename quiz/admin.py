from django.contrib import admin
from .models import Exams,Question,Answer

# Register your models here.
admin.site.register(Exams)
admin.site.register(Question)
admin.site.register(Answer)