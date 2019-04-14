from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint, pformat
from job.models.job import Job
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def register(request):

    # pprint(request.POST['title'])

    if request.method == 'POST':
        newJob = Job()
        newJob.title = request.POST['title']
        newJob.user_id = request.POST['user_id']
        newJob.status = request.POST['status']
        newJob.pay = request.POST['pay']
        newJob.mobile = request.POST['mobile']
        newJob.is_negotiation = request.POST['is_negotiation']
        # 위치 테이블
        newJob.location_id = request.POST['location_id']
        newJob.sub_location_id = request.POST['sub_location_id']
        newJob.third_location_id = request.POST['third_location_id']
        # 성별테이블
        newJob.worker_sex_id = request.POST['worker_sex_id']
        # 희망 연령대 테이블
        newJob.worker_age_id = request.POST['worker_age_id']
        newJob.has_car = request.POST['has_car']
        newJob.description = request.POST['description']
        newJob.start_available_calling_time = request.POST['start_available_calling_time']
        newJob.end_available_calling_time = request.POST['end_available_calling_time']
        newJob.start_working_time = request.POST['start_working_time']
        newJob.end_working_time = request.POST['end_working_time']
        newJob.start_working_date = request.POST['start_working_date']
        newJob.end_working_date = request.POST['end_working_date']

        newJob.save()
        return HttpResponse('ok')
    else:
        return render(request, 'home.html')