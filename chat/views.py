# pylint: disable=no-member

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from chat.models import Room, Message
from chat.serializers import RoomSerializer, MessageSerializer

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'rooms': reverse('room-list', request=request, format=format),
            'messages': reverse('message-list', request=request, format=format)
        })

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomMessages(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        room = self.get_object()
        queryset = room.messages.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
