from rest_framework import serializers
from .models import CustomUser


class UserSerializers(serializers.ModelSerializer):

    serializers.ReadOnlyField(source = '')

    class Meta:
        model = CustomUser
        fields = '__all__'

    
