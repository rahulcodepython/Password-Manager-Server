from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.RecordView.as_view(), name='record'),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
]