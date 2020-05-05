from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name