# chat/views.py
from django.shortcuts import render, get_object_or_404
from .models import Room


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def get_last_10_messages(roomId):
    room = get_object_or_404(Room, id=roomId)
    return room.message_set.order_by('-timestamp').all()[:10]