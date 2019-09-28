from rest_framework import serializers
from .models import CustomUser


class userSerializers(serializers.ModelSerializer):

    serializers.ReadOnlyField(source = '')

    class Meta:
        model = CustomUser
        fields = __('username', 'first_name','last_name','phone_number','user_type','gender','email')

    
