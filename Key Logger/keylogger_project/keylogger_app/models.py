# myapp/models.py
from django.db import models

class KeyLog(models.Model):
    keys = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log at {self.timestamp}'
