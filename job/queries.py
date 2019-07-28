import logging
from pprint import pprint

from job.models.job import JobORM
from job.serializers import JobSerializer, ChildAgeSerializer
from job.models.child_age import ChildAgeORM
from job.models.job_day_of_week import JobDayOfWeekORM

logger = logging.getLogger(__name__)
class JobRecords:

    """
    Kyle 2019-07-20

    @API: 구직등록 Query
    """
    @staticmethod
    def create(request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        else:
            return None

    """
    Kyle 2019-07-20
     
    @API: 구직상세 Query  
    """
    @staticmethod
    def get_job_detail(jobId):

        querySet = JobORM.objects.get(job_id=jobId)
        jobSerializer = JobSerializer(querySet)

        jobData = jobSerializer.data.copy()
        return jobData

    @staticmethod
    def get_all_child_age():
        return ChildAgeORM.objects.all()

    @staticmethod
    def get_all_day_of_week():
        return JobDayOfWeekORM.objects.all()

