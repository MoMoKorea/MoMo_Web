import logging
from pprint import pprint

from job.models.job import JobORM
from job.serializers import JobSerializer

logger = logging.getLogger(__name__)
class JobRecords:

    @staticmethod
    def create(request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        else:
            return None

    @staticmethod
    def get_job_detail(jobId):

        querySet = JobORM.objects.get(id=jobId)
        jobSerializer = JobSerializer(querySet)

        jobData = jobSerializer.data.copy()
        return jobData
