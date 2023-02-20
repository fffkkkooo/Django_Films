from django.urls import path
from . import views

urlpatterns = [
    path('', views.Movieview.as_view()),
]