from django.urls import path
from . import views
from .views import CHATView

urlpatterns = [
    path('<str:room_name>' , view=CHATView.as_view() , name='chat'),
]