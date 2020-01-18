from django.urls import path, include
from . import views, apis

urlpatterns = [
    # 공고 등록
    path('regist', views.register, name="regist"),
    # 공고 상세
    path('detail/<int:jobId>', views.get_detail, name="get_detail"),
    # 공고 리스트
    path('', views.get_list, name="job_list"),

    path('api/', include([
        path('root-location', apis.get_root_location),
        path('second-location', apis.get_second_location),
        path('third-location', apis.get_third_location),
    ])),
]
