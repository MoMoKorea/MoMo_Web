

class JobRepository:

    def process_job_detail(self, jobData):

        jobDetail = {}

        # (job)
        # 판매자 이름 1
        # 제목 1
        #
        # 시급 1
        # 아이나이 작업필요
        # 상세정보 1
        #
        # 근무시간 1
        # 근무주소 1 가공
        # 근무시작일 1 가공
        #
        # 근무요일 작업필요
        #
        # 희망 연령 1
        # 희망 성별 1
        # 차량소지 1
        # 제출서류 작업필요

        # TODO fake data
        jobDetail['user'] = {}
        jobDetail['user']['id'] = 1
        jobDetail['user']['username'] = '카일'
        # TODO fake data

        jobDetail['title'] = jobData['title']
        jobDetail['pay'] = jobData['pay']
        jobDetail['description'] = jobData['description']
        jobDetail['working_time'] = str(jobData['start_working_time']) + " ~ " + str(jobData['end_working_time'])
        jobDetail['working_location'] = '' #TODO
        jobDetail['working_date'] = jobData['start_working_date'] #TODO 포맷
        jobDetail['working_days'] = '' #TODO
        jobDetail['worker_age'] = str(jobData['worker_age_from']) + " ~ " + str(jobData['worker_age_to']) + "대"
        jobDetail['worker_sex'] = jobData['worker_sex']
        jobDetail['car_preference'] = jobData['car_preference']
        jobDetail['documents'] = '' # TODO
        jobDetail['child_age'] = '' # TODO

        return jobDetail

