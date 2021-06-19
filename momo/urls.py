from django.urls import path

from . import views as momoView
from job.urls import views as jobView


urlpatterns = [
    # path('', jobView.get_list),
    path('', jobView.get_list.as_view()),
    path('home/', momoView.home),
    path('test/', momoView.test_current_datetime), # test
    path('test_class/', momoView.cur_time.as_view()), # test
]
