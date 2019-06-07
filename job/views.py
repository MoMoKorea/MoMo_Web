from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint, pformat
from job.models.job import JobORM
from job.entities.job import Job
from .queries import JobRecords
from rest_framework.parsers import JSONParser

import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def register(request):


    if request.method == 'POST':


        # 0. 벨리데이션 체크

        # 1. DB에 데이터를 저장한다.
        newJob = JobRecords.create(request)

        # 2. 화면에 등록 성공/실패여부를 노출한다.

        # if cart is None:
        #     return Response(display_cart_json(CartRecords.create(identifier)),status=HTTP_201_CREATED)


        return HttpResponse('ok')
    else:
        return render(request, 'home.html')