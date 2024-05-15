from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Project, Comment, ProgressUpdate, BursaryApplication, GovernmentFeedback, Analytics

class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'projects/project_list.html', {'projects': projects})

class ProjectDetailView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return render(request, 'projects/project_detail.html', {'project': project})

class BursaryApplicationView(View):
    def get(self, request):
        applications = BursaryApplication.objects.all()
        return render(request, 'bursaries/bursary_list.html', {'applications': applications})

class GovernmentFeedbackView(View):
    def get(self, request):
        feedbacks = GovernmentFeedback.objects.all()
        return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})

class AnalyticsView(View):
    def get(self, request):
        analytics = Analytics.objects.all()
        return render(request, 'analytics/analytics_list.html', {'analytics': analytics})
