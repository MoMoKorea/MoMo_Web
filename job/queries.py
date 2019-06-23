import logging
from pprint import pprint

from job.models.job import JobORM
from job.serializers import JobSerializer

logger = logging.getLogger(__name__)
class JobRecords:

    @staticmethod
    def create(request):
        # job = Job(request)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        else:
            return None


        # out = Product(reference, price, 0, 0)
        # ProductORM.objects.create(reference=reference, price=price)


        # return jobObject

    @staticmethod
    def get_job_detail(jobId):

        querySet = JobORM.objects.get(id=jobId)
        job = JobSerializer(querySet)
        pprint(job.data)

        # 데이터 가공 필요
        # data = job.data.copy()
        # data['carPreference'] = data['carPreference']['value']

        return job.data.copy()
