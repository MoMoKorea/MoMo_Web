from django.contrib.auth.models import User

## html
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

## auth
from django.contrib.auth.mixins import LoginRequiredMixin

## error/exceptions
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

 ## ......................................................................................................... ##

## (domain)/user/
def default_page(request):
    return render(request, 'user/default_page.html')

## (domain)/user/emailConf
def emailConf(request):
    return render(request, 'user/emailConfirm.html')

 ## ......................................................................................................... ##

## (domain)/user/test
class sign_up(View):
    '''
    회원 가입
    '''
    def get(self, request, *args, **kwargs):
        return render(request, 'user/signup.html')
    def post(self, request, *args, **kwargs):
        condition = False ## 제대로 됐는지 여부 체크해주기
        response = HttpResponse("Failed Sign Up!") ## 사인업 실패시 반응 저장 HttpResponse로 저장함

        createID = request.POST['username'] ## username 이름으로 포스트방식으로 넘어온 인자를 createID에 저장
        createEmail = request.POST['email'] ## email 받는 라인
        createPSW = request.POST['psw']  ## psw 이름으로 포스트 방식으로 넘어온 인자를 createPSW에 저장
        pswRe = request.POST['psw-repeat']
        createName = request.POST['username'] ## 사용자명

        ## 비밀번호 일치여부 확인
        if createPSW != pswRe :
            condition = True
            return HttpResponse("비밀번호가 일치하지 않습니다.")

        ## 이메일 형식 체크
        if '@' not in createEmail :
            condition = True
            return HttpResponse("잘못된 이메일 형식입니다.")
        elif '.' not in createEmail :
            condition = True
            return HttpResponse("잘못된 이메일 형식입니다.")

        ## Fail Check
        if condition :
            return HttpResponse("Failed Signup") ##response
        else :
            user = User.objects.create_user(createID, createEmail, createPSW)
            user.save()
            response = HttpResponse("Succeeded Sign Up")
            formMessage = [ createID, createEmail, createPSW ]
            return HttpResponse(formMessage) ##response

## (domain)/user/login
class login(View):
    '''
    로그인
    '''
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html')
    def post(self, request, *args, **kwargs):

        User.objects.get(email = request.POST['email'].lower()).username

        if not request.user.is_authenticated :
            return HttpResponse("잘못된 정보에요. 로그인 정보를 한번 더 확인해주세요.")
        else :
            username = User.objects.get(email = request.POST['email'].lower()).username
            loginFeild = [username, request.POST['psw'] ] ## 0: id , 1 : password # request.POST['username']
            user = authenticate(username=username, password=request.POST['psw'])
            login(request, user)

            # username = User.objects.get(email= request.POST['email'].lower()).username
            # pws = request.POST['psw']
            #  loginFeild = [username, psw] ## 0: id , 1 : password
            return HttpResponse(loginFeild)

## (domain)/user/logout
class logout(View):
    '''
    로그 아웃
    '''
    def get(self, request, *args, **kwargs):
        return render(request, 'user/logout.html')
    def post(self, request, *args, **kwargs):
        return HttpResponse("로그아웃되었습니다.")


## (domain)/user/lostPsw
class lostPsw(View):
    '''
    비밀번호 찾기
    '''
    def get(self, request, *args, **kwargs):
        return render(request, 'user/lostPsw.html')

'''
class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
'''

## ............................................. 과 정 ...................................................... ##
