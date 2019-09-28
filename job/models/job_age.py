from django.db import models


class JobAgeORM(models.Model):

    class Meta:
        db_table = "job_age"

    job_age_id = models.AutoField(primary_key=True)
    age = models.IntegerField(help_text='지원 연령대')
    status = models.SmallIntegerField(default=1)






