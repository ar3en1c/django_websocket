from django.shortcuts import render
from django.views import View


# Create your views here.

class CHATView(View):
    def get(self,request):
        return render(request , 'chat/index.html')