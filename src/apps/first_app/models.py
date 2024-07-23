from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    chats = models.ManyToManyField("Chat", related_name="users_in")


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="messages"
    )
    chat = models.ForeignKey(
        "Chat", on_delete=models.CASCADE, blank=True, null=True, related_name="messages"
    )


class Chat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField(User, related_name="chats_in")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_group_chat = models.BooleanField(default=False)
