from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Project, Comment, ProgressUpdate, BursaryApplication, GovernmentFeedback, Analytics, ProjectImage

class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all().prefetch_related('images')
        return render(request, 'base/project_list.html', {'projects': projects})

class ProjectDetailView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return render(request, 'base/project_detail.html', {'project': project})

class BursaryApplicationView(View):
    def get(self, request):
        applications = BursaryApplication.objects.all()
        return render(request, 'base/bursary_list.html', {'applications': applications})

class GovernmentFeedbackView(View):
    def get(self, request):
        feedbacks = GovernmentFeedback.objects.all()
        return render(request, 'base/feedback_list.html', {'feedbacks': feedbacks})

class AnalyticsView(View):
    def get(self, request):
        analytics = Analytics.objects.all()
        return render(request, 'base/analytics_list.html', {'analytics': analytics})

class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'base/registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
        return render(request, 'base/registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'base/registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'base/registration/logged_out.html'
