from django.urls import path, include
from .views import *

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', default_page),

    ## signUp
    path('signup/', sign_up.as_view()),

    ## logIn/Out
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),

    ## lostPsw
    path('lostPsw/', lostPsw.as_view()),

    ## email confirmation
    path('emailConf/', emailConf),
]
