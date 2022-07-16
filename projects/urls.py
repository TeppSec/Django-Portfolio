from django.urls import path
from projects import views

urlpatterns = [
    path('', views.all_projects),
]
