from django.db import models


from job.models import JobORM, JobAgeORM


class JobAgeMappingORM(models.Model):

    class Meta:
        db_table = "job_age_mapping"

    job_id = models.ForeignKey(JobORM, db_column="job_id", on_delete=models.CASCADE, null=False)
    age_id = models.ForeignKey(JobAgeORM, db_column="job_age_id", on_delete=models.CASCADE, null=False)