from django.urls import path, include
from . import views, apis
from momo_web.viewname import JobViewname


urlpatterns = [
    # 공고 리스트
    path('', views.get_list, name=JobViewname.VIEW_JOB_LIST),
    # 공고 등록
    path('regist', views.register, name=JobViewname.VIEW_JOB_REGIST),
    # 공고 상세
    path('detail/<int:jobId>', views.get_detail, name=JobViewname.VIEW_JOB_DETAIL),

    path('api/', include([
        path('root-location', apis.get_root_location),
        path('second-location', apis.get_second_location),
        path('third-location', apis.get_third_location),
    ])),
]
