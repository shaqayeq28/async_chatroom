from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from chat.models import Room


@login_required()
def rooms_list(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'chat/rooms.html', context={'rooms': rooms})


@login_required()
def room_detail(request, slug):
    try:
        room = Room.objects.filter(is_active=True).get(slug=slug)
    except Room.DoesNotExist:
        raise Exception("there is no valid room with this name ")

    return render(request, 'chat/current_room.html', context={'room': room})
