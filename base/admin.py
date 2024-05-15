from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Comment, ProgressUpdate, BursaryApplication, GovernmentFeedback, Analytics

admin.site.register(User, UserAdmin)

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(ProgressUpdate)
admin.site.register(BursaryApplication)
admin.site.register(GovernmentFeedback)
admin.site.register(Analytics)
