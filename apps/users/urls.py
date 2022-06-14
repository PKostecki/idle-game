from django.urls import path, include
from apps.users import views

urlpatterns = [path("", views.dashboard, name="dashboard"),
               path('accounts/', include('django.contrib.auth.urls'))]
