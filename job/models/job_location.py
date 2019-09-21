from django.db import models


class JobLocationORM(models.Model):

    class Meta:
        db_table = "job_location"


    job_location_id = models.IntegerField(primary_key=True)
    parent_location_id = models.IntegerField(null=True)
    depth = models.SmallIntegerField(default=1)
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)