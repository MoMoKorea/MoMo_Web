from rest_framework import serializers
from .models.job import JobORM
from .models.job_day_of_week_mapping import JobDayOfWeekMappingORM


class JobSerializer(serializers.ModelSerializer):

    car_preference = serializers.ReadOnlyField(source='car_preference_id')
    worker_sex = serializers.ReadOnlyField(source='worker_sex_id')
    worker_age_from = serializers.ReadOnlyField(source='worker_age_from_id')
    worker_age_to = serializers.ReadOnlyField(source='worker_age_to_id')
    child_age = serializers.ReadOnlyField(source='child_age_id')



    # 불필요한 데이터 정리 or 가공
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['car_preference'] = ret['car_preference'].value
        ret['child_age'] = ret['child_age'].age
        ret['worker_sex'] = ret['worker_sex'].sex
        ret['worker_age_from'] = ret['worker_age_from'].age
        ret['worker_age_to'] = ret['worker_age_to'].age
        ret['day_of_weeks'] = JobDayOfWeekMappingORM.objects.filter(job_id=ret['job_id'])

        # 필요없는 컬럼 제외
        ret.pop('car_preference_id')
        ret.pop('worker_sex_id')
        ret.pop('worker_age_from_id')
        ret.pop('worker_age_to_id')
        ret.pop('child_age_id')
        return ret

    class Meta():
        model = JobORM
        fields = '__all__'


    # Kyle 2019-06-22 이런식으로 필드 벨리데이션을 커스텀 할 수 있다.
    # def validate_title(self, value):
    #     pass



