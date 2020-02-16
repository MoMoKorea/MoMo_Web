from django.shortcuts import redirect
from django.urls import reverse
from momo_web.viewname import *
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder




class JobMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화


    def __call__(self, request):

        # 회원정보를 request에 json형식으로 추가한다.
        if request.user.is_authenticated:
            userModel = json.dumps(model_to_dict(request.user), cls=DjangoJSONEncoder)
        else:
            userModel = None

        request.userModel = userModel


        # 지정한 path랑 일치한다면 로직을 체크한다.
        if request.path == reverse(JobViewname.VIEW_JOB_REGIST):

            if request.user.is_authenticated:
                # 인증된 회원이라면 다음 프로세스로 이동한다.
                response = self.get_response(request)
                return response
            else:
                # 인증되지 않은 회원이라면 로그인페이지로 이동한다.
                return redirect(reverse(UserViewname.VIEW_USER_LOGIN))
        else:
            # 뷰가 호출된 뒤에 실행될 코드들
            response = self.get_response(request)
            return response
