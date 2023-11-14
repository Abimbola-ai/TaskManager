from django.contrib import admin
from django.contrib.admin.models import LogEntry
# from .models import Question
from taskmanager.models import CustomUser

#Update the user field in the LogEntry model
LogEntry._meta.get_field('user').remote_field.model = CustomUser
# admin.site.register(Question)
admin.site.register(CustomUser)

