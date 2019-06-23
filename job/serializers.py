from rest_framework import serializers
from .models.job import JobORM


class JobSerializer(serializers.ModelSerializer):

    carPreference = serializers.ReadOnlyField(source='car_preference_id')
    workerSex = serializers.ReadOnlyField(source='worker_sex_id')




    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['carPreference'] = ret['carPreference'].value
        ret['workerSex'] = ret['workerSex'].sex

        # 필요없는 컬럼 제외
        ret.pop('car_preference_id')
        ret.pop('worker_sex_id')

        return ret

    class Meta():
        model = JobORM
        fields = '__all__'
        # field = ('id', 'user_id', 'status', 'title', 'pay'
        #          , 'is_negotiation', 'location_id', 'sub_location_id', 'third_location_id'
        #          , 'worker_sex', 'worker_age_from', 'worker_age_to', 'car_preference'
        #          , 'description', 'start_available_calling_time', 'end_available_calling_time'
        #          , 'start_working_time', 'end_working_time', 'start_working_date'
        #          , 'end_working_date', 'created_at', 'updated_at')


    # Kyle 2019-06-22 이런식으로 필드 벨리데이션을 커스텀 할 수 있다.
    # def validate_title(self, value):
    #     pass



