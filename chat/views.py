from django.shortcuts import render
from django.views import View


# Create your views here.

class CHATView(View):
    def get(self,request, room_name):
        return render(request, "chat/chat.html", {
            "room_name": room_name
        })