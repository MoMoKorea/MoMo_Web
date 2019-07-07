from django.db import models
from django.utils import timezone

from job.models.job_car_preference import JobCarPreferenceORM
from job.models.job_sex import JobSexORM
from job.models.job_age import JobAgeORM
from job.models.child_age import ChildAgeORM

class JobORM(models.Model):

    class Meta:
        db_table = "job"


    job_id = models.BigAutoField(primary_key=True)
    # TODO :: user_id foreignKey
    user_id = models.BigIntegerField(default=0, help_text='회원 번호')
    status = models.SmallIntegerField(default=1)
    title = models.CharField(max_length=50, help_text='글 제목', default='')
    pay = models.IntegerField(default=0)
    is_negotiation = models.BooleanField(default=False)
    location_id = models.SmallIntegerField(default=1)
    sub_location_id = models.SmallIntegerField(default=1)
    third_location_id = models.SmallIntegerField(default=1)
    description = models.TextField(default='')
    start_available_calling_time = models.SmallIntegerField(default=9)
    end_available_calling_time = models.SmallIntegerField(default=18)
    start_working_time = models.SmallIntegerField(null=True)
    end_working_time = models.SmallIntegerField(null=True)
    start_working_date = models.DateField(default=timezone.now)
    end_working_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    worker_sex_id = models.ForeignKey(JobSexORM, on_delete=models.SET_NULL, null=True, db_column='worker_sex_id', related_name='worker_sex')
    worker_age_from_id = models.ForeignKey(JobAgeORM, on_delete=models.SET_NULL, db_column='worker_age_from_id', related_name='worker_age_from', help_text='지원 연령대 시작', null=True)
    worker_age_to_id = models.ForeignKey(JobAgeORM, on_delete=models.SET_NULL, db_column='worker_age_to_id', related_name='worker_age_to', help_text='지원 연령대 끝', null=True)
    car_preference_id = models.ForeignKey(JobCarPreferenceORM, on_delete=models.SET_NULL, null=True, db_column='car_preference_id', related_name='car_preference')
    child_age_id = models.ForeignKey(ChildAgeORM, on_delete=models.SET_NULL, null=True, db_column='child_age_id', related_name='child_age')



    # 희망제출서류




