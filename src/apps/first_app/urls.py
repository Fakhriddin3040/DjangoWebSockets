from django.urls import path

from .views import SayHello

urlpatterns = [
    path("hello/", SayHello.as_view(), name="say_hello"),
]