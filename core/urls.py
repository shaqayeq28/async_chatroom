from django.contrib.auth import views
from django.urls import path

from core.views import homepage, signup

urlpatterns = [
    path('home/', homepage, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='logout'),
]
