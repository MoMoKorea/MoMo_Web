from .queries import JobRecords
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from pprint import pprint

@api_view(["GET"])
def get_root_location(request):

    rootLocation = list(JobRecords.get_all_root_location().values())

    data = {}
    data['rootLocations'] = rootLocation

    return HttpResponse(json.dumps(data), content_type="application/json")


@api_view(["GET"])
def get_second_location(request):

    parent_id = request.query_params['parent_id']
    locationList = list(JobRecords.get_second_location(parent_id).values())

    data = {}
    data['secondLocations'] = locationList

    return HttpResponse(json.dumps(data), content_type="application/json")


@api_view(["GET"])
def get_third_location(request):

    parent_id = request.query_params['parent_id']
    locationList = list(JobRecords.get_third_location(parent_id).values())

    data = {}
    data['thirdLocations'] = locationList

    return HttpResponse(json.dumps(data), content_type="application/json")
