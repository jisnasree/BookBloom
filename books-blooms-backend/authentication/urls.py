from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.CreateUserView.as_view()),
]