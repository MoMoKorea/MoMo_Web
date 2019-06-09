from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .queries import JobRecords
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):


    if request.method == 'POST':

        # 스크립트쪽에서 한번 하겠지만 한번 더 한다.
        # TODO 0. 벨리데이션 체크

        # 1. DB에 데이터를 저장한다.
        jobSerializer = JobRecords.create(request)
        #TODO 레코드용 테이블을 추가한다.

        # 2. 화면에 등록 성공/실패여부를 노출한다.
        if (jobSerializer):
            return Response({'data': 'success'})
        else:
            return HttpResponse('none')

        #TODO 리다이렉트는 스크립트에서 팝업을 뛰워주고 이동한다.

    elif request.method == 'GET':
        return render(request, template_name='test.html', context={'title': '타이틀입니다.'})