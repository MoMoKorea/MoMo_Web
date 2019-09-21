from django.db import models


class ChildAgeORM(models.Model):

    class Meta:
        db_table = 'child_age'

    child_age_id = models.AutoField(primary_key=True)
    age = models.CharField(max_length=20, null=False)
    status = models.SmallIntegerField(default=1)