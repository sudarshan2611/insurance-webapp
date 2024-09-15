from django.urls import path
from . import views


urlpatterns = [
    path('LoginView/', views.LoginView, name='LoginView'),

]
