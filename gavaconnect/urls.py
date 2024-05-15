from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),  # Assuming your app is named 'base_app'
]
