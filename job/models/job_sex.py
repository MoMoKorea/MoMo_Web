from django.db import models


class JobSexORM(models.Model):
    class Meta:
        db_table = "job_sex"


    job_sex_id = models.BigAutoField(primary_key=True)
    sex = models.CharField(max_length=10, help_text='성별', default="")
    status = models.SmallIntegerField(default=1)
