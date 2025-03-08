from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecordView.as_view(), name="record"),
    path("login/", views.LoginView.as_view(), name="login"),
]
