from django.urls import path
from .views import ProjectListView, ProjectDetailView, BursaryApplicationView, GovernmentFeedbackView, AnalyticsView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('bursaries/', BursaryApplicationView.as_view(), name='bursary_list'),
    path('feedback/', GovernmentFeedbackView.as_view(), name='feedback_list'),
    path('analytics/', AnalyticsView.as_view(), name='analytics_list'),
]
