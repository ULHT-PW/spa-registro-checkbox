from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    present = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} - present = {self.present}, online = {self.online}"
    
