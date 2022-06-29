import datetime
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Message
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class MessageChannel(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        sender = data.get('sender')
        receiver = data.get('receiver')
        message = data.get('message')
        time = datetime.utcnow()

        message_data = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'time' : time,
        }

        message = Message.objects.create(**message_data)

        data = {
            "message": f"New message added to channel with id: {message.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = Message.objects.count()
        items = Message.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'sender': item.sender,
                'receiver': item.receiver,
                'message': item.message,
                'time_sent': item.time_sent,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)