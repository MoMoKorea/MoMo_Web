from django.shortcuts import render, redirect
from django.urls import reverse

# ---------------------------------------------------------------------------------------


def home(request):
    # return render(request, 'empty.html')
    # return render(request, 'errors.html')
    # return render(request, 'mypage/mypage.html')
    return render(request, 'mypage/help.html')
    # return render(request, 'mypage/contact.html')
    # return render(request, 'mypage/user.html')
    # return render(request, 'account/verification_sent.html')
    # return render(request, 'account/email_account.html')
    # return render(request, 'account/password_reset.html')
    # return render(request, 'account/password_change.html')
    # return render(request, 'account/login.html')
    # return render(request, 'account/signup.html')
    # return render(request, 'account/test.html')
    # return render(request, 'home.html')



from django.views import View
from django.http import HttpResponse
import datetime


# 함수 기반 뷰
def test_current_datetime(request):
    now = datetime.datetime.now()
    day_time = str(now)[:19]
    html = f'''<html><body>지금은 {day_time} 입니다. </body></html>'''
    return HttpResponse(html)

# 클래스 기반 뷰
class cur_time(View):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        day_time = str(now)[:19]
        html = f'''<html><body>지금은 {day_time} 입니다. 이것은 Class-Based View </body></html>'''
        return HttpResponse(html)