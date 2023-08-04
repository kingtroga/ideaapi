import json

from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Room, Message

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None # ??
        self.room_group_name = None # Group chats
        self.room = None # All chats names
        self.user = None # Authenticated user

    def returnUser(self, token_string):
        try:
            user = Token.objects.get(key=token_string).user
        except:
            user = AnonymousUser()
        return user

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'
        self.room, self.created = Room.objects.get_or_create(name=self.room_name)
        

        self.access_token = self.scope["url_route"]["kwargs"]["access_token"]
        print("self.access_token: ", self.access_token)
        
        self.user = self.returnUser(self.access_token)
        print("self.user: ", self.user)
        print("self.user.fullName: ", self.user.fullName)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name,
        )


    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name,
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        if not self.user.is_authenticated:
            return 
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message",
                'user': self.user.fullName,
                "message": message,
            }
        )
        Message.objects.create(
            user=self.user,
            room=self.room,
            content=message
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))