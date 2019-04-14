from django.db import models


class JobSexModel(models.Model):
    class Meta:
        db_table = "job_sex"


    id = models.BigAutoField(primary_key=True)
    sex = models.CharField(max_length=10, help_text='성별', default="")
    status = models.SmallIntegerField(default=1)
