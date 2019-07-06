from django.forms.models import model_to_dict

class JobRepository:

    def process_job_detail(self, jobData):

        jobDetail = {}

        # 근무주소 작업필요
        # 근무시작일 1 가공 예시 19/03/12
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
        jobDetail['worker_age'] = str(jobData['worker_age_from']) + " ~ " + str(jobData['worker_age_to']) + "대"
        jobDetail['worker_sex'] = jobData['worker_sex']
        jobDetail['car_preference'] = jobData['car_preference']
        jobDetail['documents'] = '' # TODO
        jobDetail['child_age'] = jobData['child_age']


        day_of_weeks = []
        for item in jobData["day_of_weeks"]:
            day_of_weeks.append(model_to_dict(item.day_of_week_id))

        jobDetail['working_day_of_weeks'] = day_of_weeks

        return jobDetail

