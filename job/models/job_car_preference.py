from django.db import models


class JobCarPreferenceORM(models.Model):

    class JobCarPreferenceManager(models.Manager):
        def available(self):
            return self.filter(status=1)


    class Meta:
        db_table = 'job_car_preference'

    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=20, default='', help_text='차량소지선호 여부')
    status = models.SmallIntegerField(default=1)

    objects = JobCarPreferenceManager()




