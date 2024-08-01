from django.contrib import admin
from django.urls import path
from calculatorapp import views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Handle root URL
]
