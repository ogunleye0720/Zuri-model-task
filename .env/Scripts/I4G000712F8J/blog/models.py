from asyncio.windows_events import NULL
from tkinter import CASCADE
from typing import Text
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.TextField(max_length=200)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now =True)


    def __str__(self) :
        return self.Title

