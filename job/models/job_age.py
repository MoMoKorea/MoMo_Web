from django.db import models



class JobAgeModel(models.Model):

    class Meta:
        db_table = "job_age"

    id = models.AutoField(primary_key=True)
    age = models.CharField(max_length=10, help_text='지원 연령대', default='')
    status = models.SmallIntegerField(default=1)






