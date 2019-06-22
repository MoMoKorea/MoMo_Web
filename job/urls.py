from django.urls import path
from . import views

urlpatterns = [
    # 공고 등록
    path('register', views.register),
    # 공고 상세
    path('detail/<int:jobId>', views.get_detail),
]
