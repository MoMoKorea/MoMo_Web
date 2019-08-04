from django.urls import path, include
from . import views, apis

urlpatterns = [
    # 공고 등록
    path('regist', views.register),
    # 공고 상세
    path('detail/<int:jobId>', views.get_detail),

    path('api/', include([
        path('root-location', apis.get_root_location),
    ])),
]
