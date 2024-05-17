from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Project, Comment, ProgressUpdate, BursaryApplication, GovernmentFeedback, Analytics, ProjectImage
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model


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
        return render(request, 'base/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
        return render(request, 'base/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'base/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'base/logged_out.html'


@login_required
def project_list(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        content = request.POST.get('content')
        if project_id and content:
            project = Project.objects.get(id=project_id)
            comment = Comment(content=content, date=timezone.now(), author=request.user)
            comment.save()
            project.comments.add(comment)
            return redirect('project_list')

    return render(request, 'base/project_list.html', {'projects': projects})

@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Project, Comment
from django.utils import timezone


@login_required
def project_list(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        content = request.POST.get('content')
        print(f'POST data received: project_id={project_id}, content={content}')  # Debugging line
        if project_id and content:
            try:
                project = get_object_or_404(Project, id=project_id)
                comment = Comment(content=content, date=timezone.now(), author=request.user)
                comment.save()
                project.comments.add(comment)
                project.save()  # Ensure the project is saved after adding the comment
                return redirect('project_list')
            except Exception as e:
                print(f'Error while saving comment: {e}')  # Debugging line
    return render(request, 'base/project_list.html', {'projects': projects})
    projects = Project.objects.all()
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        content = request.POST.get('content')
        if project_id and content:
            project = Project.objects.get(id=project_id)
            comment = Comment(content=content, date=timezone.now(), author=request.user)
            comment.save()
            project.comments.add(comment)
            return redirect('project_list')

    return render(request, 'base/project_list.html', {'projects': projects})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    return render(request, 'base/user_list.html', {'users': users})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'base/user_detail.html', {'user': user})

