from django.db import models
from django.utils import timezone


class Job(models.Model):

    id = models.BigAutoField(primary_key='true')
    user_id = models.BigIntegerField(help_text='회원 번호')
    status = models.SmallIntegerField()
    title = models.CharField(max_length=50, help_text='글 제목')
    pay = models.IntegerField()
    is_negotiation = models.BooleanField(default='false')
    mobile = models.CharField(max_length=20)
    location_id = models.SmallIntegerField()
    sub_location_id = models.SmallIntegerField()
    third_location_id = models.SmallIntegerField()
    worker_sex_id = models.SmallIntegerField()
    worker_age_id = models.SmallIntegerField()
    has_car = models.BooleanField()
    child_description = models.TextField()
    child_personality = models.TextField()
    start_availble_calling_time = models.SmallIntegerField()
    end_availble_calling_time = models.SmallIntegerField()
    start_working_time = models.SmallIntegerField()
    end_working_time = models.SmallIntegerField()
    start_working_date = models.DateField(default=timezone.now)
    end_working_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "job"




