from django.db import models

class JobDayOfWeekORM(models.Model):

    class Meta:
        db_table = "job_day_of_week"

    id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=5)
    status = models.SmallIntegerField(default=1)

