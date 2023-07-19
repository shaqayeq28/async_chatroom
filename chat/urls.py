from django.urls import path

from chat.views import rooms_list, room_detail

urlpatterns = [
    path('rooms/', rooms_list, name='rooms'),
    path('<slug:slug>/', room_detail, name='room'),
]
