from django.urls import path
from . import views
from .views import CHATView

urlpatterns = [
    path('' , view=CHATView.as_view() , name='chat'),
]