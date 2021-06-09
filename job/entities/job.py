

class Job:

    def __init__(self, request):
        self.title = request.data['title']
        self.user_id = request.data['user_id']
        self.status = request.data['status']
        self.pay = request.data['pay']
        self.mobile = request.data['mobile']
        self.is_negotiation = request.data['is_negotiation']
        # 위치 테이블
        self.location_id = request.data['location_id']
        self.sub_location_id = request.data['sub_location_id']
        self.third_location_id = request.data['third_location_id']
        # 성별테이블
        self.worker_sex_id = request.data['worker_sex_id']
        # 희망 연령대 테이블
        self.worker_age_id = request.data['worker_age_id']
        # self.has_car = request.data['has_car']
        self.description = request.data['description']
        self.start_available_calling_time = request.data['start_available_calling_time']
        self.end_available_calling_time = request.data['end_available_calling_time']
        self.start_working_time = request.data['start_working_time']
        self.end_working_time = request.data['end_working_time']
        self.start_working_date = request.data['start_working_date']
        self.end_working_date = request.data['end_working_date']



