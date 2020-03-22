from django.urls import path
from . import views as momoView
from job.urls import views as jobView


urlpatterns = [
    path('', jobView.get_list),
    path('home', momoView.home),
]
