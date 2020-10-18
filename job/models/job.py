from django.db import models
from django.utils import timezone

from job.models.job_location import JobLocationORM
from job.models.job_car_preference import JobCarPreferenceORM
from job.models.job_sex import JobSexORM
from job.models.job_age import JobAgeORM
from job.models.child_age import ChildAgeORM
from job.models.job_day_of_week import JobDayOfWeekORM
from job.models.job_require_document import JobRequireDocumentORM
from user.models import CustomUser


class JobORM(models.Model):

    class Meta:
        db_table = "job"

    @classmethod
    def get_main_list(self):
        return self.objects.select_related("child_age",
                                           "root_location",
                                           "second_location")



    @classmethod
    def get_detail(self):
        return self.objects.select_related("child_age",
                                           "worker_sex",
                                           "car_preference",
                                           "root_location",
                                           "second_location",
                                           "user")




    job_id = models.BigAutoField(primary_key=True)
    status = models.SmallIntegerField(default=1)
    title = models.CharField(max_length=50, help_text='글 제목', default='')
    pay = models.IntegerField(default=0)
    is_negotiation = models.BooleanField(default=False)
    third_location_id = models.SmallIntegerField(default=1)
    description = models.TextField(default='')
    start_available_calling_time = models.TimeField()
    end_available_calling_time = models.TimeField()
    start_working_time = models.TimeField(null=True)
    end_working_time = models.TimeField(null=True)
    start_working_date = models.DateField(default=timezone.now)
    end_working_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, db_column='user_id', related_name='user')
    root_location = models.ForeignKey(JobLocationORM, on_delete=models.SET_NULL, null=True, db_column='root_location_id', related_name='root_location')
    second_location = models.ForeignKey(JobLocationORM, on_delete=models.SET_NULL, null=True, db_column='second_location_id', related_name='second_location')
    worker_sex = models.ForeignKey(JobSexORM, on_delete=models.SET_NULL, null=True, db_column='worker_sex_id', related_name='worker_sex')
    car_preference = models.ForeignKey(JobCarPreferenceORM, on_delete=models.SET_NULL, null=True, db_column='car_preference_id')
    child_age = models.ForeignKey(ChildAgeORM, on_delete=models.SET_NULL, null=True, db_column='child_age_id', related_name='child_age')
    day_of_weeks = models.ManyToManyField(JobDayOfWeekORM, through="JobDayOfWeekMappingORM", null=True, related_name='day_of_weeks')
    documents = models.ManyToManyField(JobRequireDocumentORM, through="JobRequireDocumentMappingORM", null=True, related_name='documents')
    worker_age = models.ManyToManyField(JobAgeORM, through="JobAgeMappingORM", null=True, related_name='worker_age')





