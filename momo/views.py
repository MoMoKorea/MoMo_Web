from django.shortcuts import render, redirect
from django.urls import reverse

# ---------------------------------------------------------------------------------------


def home(request):
    # return render(request, 'empty.html')
    # return render(request, 'errors.html')
    return render(request, 'mypage/mypage.html')
    # return render(request, 'mypage/help.html')
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
