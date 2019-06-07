from rest_framework import serializers
from .models.job import JobORM


class JobSerializer(serializers.ModelSerializer):

    class Meta():
        model = JobORM
        fields = '__all__'
        # field = ('id', 'user_id', 'status', 'title', 'pay'
        #          , 'is_negotiation', 'location_id', 'sub_location_id', 'third_location_id'
        #          , 'worker_sex', 'worker_age_from', 'worker_age_to', 'car_preference'
        #          , 'description', 'start_available_calling_time', 'end_available_calling_time'
        #          , 'start_working_time', 'end_working_time', 'start_working_date'
        #          , 'end_working_date', 'created_at', 'updated_at')
