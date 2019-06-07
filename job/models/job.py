from django.db import models
from django.utils import timezone

from job.models.job_car_preference import JobCarPreferenceORM
from job.models.job_sex import JobSexORM

class JobORM(models.Model):

    class Meta:
        db_table = "job"


    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(default=0, help_text='회원 번호')
    status = models.SmallIntegerField(default=1)
    title = models.CharField(max_length=50, help_text='글 제목', default='')
    pay = models.IntegerField(default=0)
    is_negotiation = models.BooleanField(default=False)
    location_id = models.SmallIntegerField(default=1)
    sub_location_id = models.SmallIntegerField(default=1)
    third_location_id = models.SmallIntegerField(default=1)
    worker_sex_id = models.ForeignKey(JobSexORM, on_delete=models.SET_NULL, null=True, db_column='worker_sex_id')
    worker_age_from = models.IntegerField(help_text='지원 연령대 시작', null=True)
    worker_age_to = models.IntegerField(help_text='지원 연령대 끝', null=True)
    car_preference_id = models.ForeignKey(JobCarPreferenceORM, on_delete=models.SET_NULL, null=True, db_column='car_preference_id')
    description = models.TextField(default='')
    start_available_calling_time = models.SmallIntegerField(default=9)
    end_available_calling_time = models.SmallIntegerField(default=18)
    start_working_time = models.SmallIntegerField(null=True)
    end_working_time = models.SmallIntegerField(null=True)
    start_working_date = models.DateField(default=timezone.now)
    end_working_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


