from django.contrib import admin

from .models import Question , Information, Choice

admin.site.register(Question)
admin.site.register(Information)
admin.site.register(Choice)

# Register your models here.
