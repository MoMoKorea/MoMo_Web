from user.queries import UserRecords
from .queries import JobRecords
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseBadRequest
import json

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

@api_view(["POST"])
def update_contact_number(request):

    print(request.user)

    data = request.data["params"]
    # 연락처를 DB에 저장한다.
    user = UserRecords.update(request.user.id, data)

    if user is not None:
        # 성공했으면 return
        response = {
            "contactNumber": user["phone_number"]
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return HttpResponseBadRequest()



