from .queries import JobRecords
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json


@api_view(["GET"])
def get_root_location(request):

    rootLocation = list(JobRecords.get_all_root_location().values())

    data = {}
    data['rootLocation'] = rootLocation

    return HttpResponse(json.dumps(data), content_type="application/json")

