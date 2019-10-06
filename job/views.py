from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .queries import JobRecords
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .repository import JobRepository
from pprint import pprint
from django.forms.models import model_to_dict


import json


import logging

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

    # 1. jobId로 정보들을 불러온다.
    jobData = JobRecords.get_job_detail(jobId)
    # pprint(jobData)
    # pprint(model_to_dict(jobData['day_of_weeks'][0]))
    # 2. 필요한 정보를 가공한다.
    jobDetail = jobRepository.process_job_detail(jobData)
    pprint(jobDetail)
    # 3. 화면으로 가공한 정보를 넘긴다.
    return render(request, template_name='detail/detail.html', context={'data': jobDetail})

"""
Kyle 2019-10-06

@API: job 리스트
"""
def get_list(request):

    # 1. 리스트 데이터들을 불러온다.
    jobList = JobRecords.get_job_list()


    return render(request, template_name='list/list.html', context={'data': json.dumps(jobList)})