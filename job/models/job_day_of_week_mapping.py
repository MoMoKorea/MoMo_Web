from django.db import models
from job.models.job import JobORM
from job.models.job_day_of_week import JobDayOfWeekORM
from django.utils import timezone



class JobDayOfWeekMappingORM(models.Model):

    class Meta:
        db_table = "job_day_of_week_mapping"

    # job_id = models.ForeignKey(JobORM, db_column="job_id", on_delete=models.SET_NULL, null=False)
    job_id = models.BigIntegerField(null=False)
    day_of_week_id = models.ForeignKey(JobDayOfWeekORM, db_column="day_of_week_id", on_delete=models.SET_NULL, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)
