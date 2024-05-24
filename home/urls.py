from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='homepg'),  # Add this line
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('about', views.AboutView.as_view(), name='about'),

]
