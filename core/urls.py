from django.urls import path

from core.views import homepage, signup

urlpatterns = [
    path('home/', homepage, name='home'),
    path('signup/', signup, name='signup'),
]
