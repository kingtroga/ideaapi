# chat/consumers.py

from base64 import decode
import json
from .views import get_last_10_messages
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Room, Message  # new import

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None  
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_id = int(self.scope['url_route']['kwargs']['user_id'])
        #print(self.scope['url_route'])
        
        
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get_or_create(name=self.room_name)
        
        self.user = User.objects.get(user_id=self.user_id)
        print("self.user.fullName: ", self.user.full_name)
        print("self.user.user_id: ", self.user.user_id)

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'chat_message':
            message = text_data_json['message']

            
            # send chat message event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user_id': self.user.user_id,
                }
            )
            Message.objects.create(user=self.user, room=self.room[0], content=message)  # new
        elif text_data_json['type'] == 'fetch_message':
            for message in get_last_10_messages(self.room[0].pk):
                self.send(text_data=json.dumps(
                    {
                        'type': 'chat_message',
                        'message': message.content,
                        'user_id': message.user.user_id
                    }
                ))
            """ self.send(text_data=json.dumps(
                  {
                'type': 'chat_message',
                'message': get_last_10_messages(self.room[0].pk),
                'user_id': 19010301047,
            })
                  ) """

            

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))