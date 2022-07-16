from django.urls import path
from projects import views

urlpatterns = [
    path('', views.all_projects),
    path('<int:pk>', views.project_detail), # check integer as link
]
