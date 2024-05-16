from django.contrib import admin
from .models import Project, ProjectImage, Comment, ProgressUpdate, BursaryApplication, GovernmentFeedback, Analytics

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Comment)
admin.site.register(ProgressUpdate)
admin.site.register(BursaryApplication)
admin.site.register(GovernmentFeedback)
admin.site.register(Analytics)
