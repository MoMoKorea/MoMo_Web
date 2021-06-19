import json
import logging
from pprint import pprint

from django.contrib.auth.models import AnonymousUser
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.functional import SimpleLazyObject
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.views import View


from .queries import JobRecords
from .repository import JobRepository

logger = logging.getLogger(__name__)
jobRepository = JobRepository()

"""
Kyle 2019-06-15

@API Job 등록 API
"""
@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):


    if request.method == 'POST':

        pprint(request.data['params'])

        # 스크립트쪽에서 한번 하겠지만 한번 더 한다.
        # TODO 0. 벨리데이션 체크

        # 1. DB에 데이터를 저장한다.
        jobSerializer = JobRecords.create(request.data['params'])
        # TODO 레코드용 테이블을 추가한다.

        # 2. 화면에 등록 성공/실패여부를 노출한다.
        # TODO 리다이렉트는 스크립트에서 팝업을 뛰워주고 이동한다.
        # 성공
        if (jobSerializer):
            # test
            return Response({'data': 'success'})
        # 실패
        else:
            return HttpResponse('none')


    elif request.method == 'GET':

        # 1. 근무요일, 유아 나이정보, 선호성별, 선호 연령대, 차량 소지여부, 제출서류
        childAgeList = JobRecords.get_all_child_age()
        dayOfWeekList = JobRecords.get_all_day_of_week()
        preferredSexList = JobRecords.get_all_preferred_sex()
        preferredAgeList = JobRecords.get_all_preferred_age()
        preferredCarList = JobRecords.get_all_preferred_car()
        requiredDocumentList = JobRecords.get_all_required_document()

        data = {
            "childAgeList": json.dumps(list(childAgeList.values())),
            "dayOfWeekList": json.dumps(list(dayOfWeekList.values())),
            "preferredSexList": json.dumps(list(preferredSexList.values())),
            "preferredAgeList": json.dumps(list(preferredAgeList.values())),
            "preferredCarList": json.dumps(list(preferredCarList.values())),
            "requiredDocumentList": json.dumps(list(requiredDocumentList.values())),
        }


        return render(request, template_name='regist/regist.html', context={'title': '타이틀입니다.', 'data': data,})


"""
Kyle 2019-06-15

@API: job 상세
"""
@api_view(['GET'])
def get_detail(request, jobId):

    # 0. 유효하지않은 jobId면 없는페이지로 돌린다
    # 1. jobId로 정보들을 불러오고 가공한다.
    jobDetail = jobRepository.process_job_detail(jobId)

    # 2. 화면으로 가공한 정보를 넘긴다.
    return render(request, template_name='detail/detail.html', context={'data': json.dumps(jobDetail, cls=DjangoJSONEncoder)})

"""
Kyle 2019-10-06

@API: job 리스트
"""
@api_view(['GET'])
def get_list(request):
    # 1. 리스트 데이터들을 불러온다.
    # request.GET.get('page') 가 NoneType이면 1을 반환 아니면 넘어온 page를 반환
    page = 1 if request.GET.get('page') is None else int(request.GET.get('page'))
    # TODO: user 계정에 선택된 지역 id값을 추가해야한다.
    # TODO: 계정에서 가져온 지역id로 지역이름도 가져와서 셋팅을 해준다.
    selectedLocationId = 41 if request.GET.get('location_id') is None else int(request.GET.get('location_id'))
    selectedLocation = jobRepository.get_selected_location(selectedLocationId)
    jobList = jobRepository.process_job_list(page, selectedLocationId)
    location = jobRepository.get_location_list()

    # rest api 요청일경우에는 json형식으로 내려준다
    if request.META.get('HTTP_ACCEPT').find('json') != -1:
        return HttpResponse(json.dumps(jobList, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        params = {
            'data': json.dumps(jobList, cls=DjangoJSONEncoder),
            'locations': json.dumps(location, cls=DjangoJSONEncoder),
            'selectedLocation': json.dumps(selectedLocation, cls=DjangoJSONEncoder),
        }

        return render(request, template_name='list/list.html', context=params)

"""
Joe 2021-06-19

@API: job 리스트 > class기반 뷰 
"""
class get_list(View):
    def get(self, request, *args, **kwargs):
        # 1. 리스트 데이터들을 불러온다.
        # request.GET.get('page') 가 NoneType이면 1을 반환 아니면 넘어온 page를 반환
        page = 1 if request.GET.get('page') is None else int(request.GET.get('page'))
        # TODO: user 계정에 선택된 지역 id값을 추가해야한다.
        # TODO: 계정에서 가져온 지역id로 지역이름도 가져와서 셋팅을 해준다.
        selectedLocationId = 41 if request.GET.get('location_id') is None else int(request.GET.get('location_id'))
        selectedLocation = jobRepository.get_selected_location(selectedLocationId)
        jobList = jobRepository.process_job_list(page, selectedLocationId)
        location = jobRepository.get_location_list()

        # rest api 요청일경우에는 json형식으로 내려준다
        if request.META.get('HTTP_ACCEPT').find('json') != -1:
            return HttpResponse(json.dumps(jobList, cls=DjangoJSONEncoder), content_type="application/json")
        else:
            params = {
                'data': json.dumps(jobList, cls=DjangoJSONEncoder),
                'locations': json.dumps(location, cls=DjangoJSONEncoder),
                'selectedLocation': json.dumps(selectedLocation, cls=DjangoJSONEncoder),
            }
            return render(request, template_name='list/list.html', context=params)