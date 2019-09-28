from django.db import models


class JobRequireDocumentORM(models.Model):

    class Meta:
        db_table = "job_require_document"

    job_require_document_id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)



