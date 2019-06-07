
from job.entities.job import Job
from job.models.job import JobORM
from job.serializers import JobSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from pprint import pprint, pformat

import logging



logger = logging.getLogger(__name__)
class JobRecords:

    @staticmethod
    def create(request):
        # job = Job(request)
        serializer = JobSerializer(data=request.POST)
        if serializer.is_valid():
            return serializer.save()


        # out = Product(reference, price, 0, 0)
        # ProductORM.objects.create(reference=reference, price=price)


        # return jobObject
