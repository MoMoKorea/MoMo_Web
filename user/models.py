# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # django all-auth에 포함되어 있는 기본 항목들 외의 항목들을 추가
    phone_number = models.CharField(max_length=20, default = '01000000000')
    user_type = models.BooleanField(default=True) ## True : 아이어머니 / False : 등교어머니
    gender = models.CharField(max_length=20, default = 'W')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nameUser = models.CharField(max_length = 20, default = '이름이름')

    def __str__(self):
        return self.email
