from django.db import models
from job.models import JobRequireDocumentORM, JobORM


class JobRequireDocumentMappingORM(models.Model):

    class Meta:
        db_table = "job_require_document_mapping"

    job_id = models.ForeignKey(JobORM, db_column="job_id", on_delete=models.CASCADE, null=False)
    require_document_id = models.ForeignKey(JobRequireDocumentORM, db_column="job_require_document_id", on_delete=models.SET_NULL, null=True)