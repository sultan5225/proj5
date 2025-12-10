from django.db import models
from django.contrib.auth.models import User


# عنوان المستخدم
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "عناوين المستخدم"

    def __str__(self):
        return f"عنوان {self.user.username}"
