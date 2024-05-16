from django.urls import path
from .views import ProjectListView, ProjectDetailView, BursaryApplicationView, GovernmentFeedbackView, AnalyticsView, UserRegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('bursaries/', BursaryApplicationView.as_view(), name='bursary_list'),
    path('feedback/', GovernmentFeedbackView.as_view(), name='feedback_list'),
    path('analytics/', AnalyticsView.as_view(), name='analytics_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
