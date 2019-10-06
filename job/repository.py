from django.forms.models import model_to_dict
import json

class JobRepository:

    def process_job_detail(self, jobData):

        jobDetail = {}

        # 근무시작일 1 가공 예시 19/03/12

        # TODO fake data
        jobDetail['user'] = {}
        jobDetail['user']['id'] = 1
        jobDetail['user']['username'] = '카일'
        # TODO fake data

        jobDetail['title'] = jobData['title']
        jobDetail['pay'] = jobData['pay']
        jobDetail['description'] = jobData['description']
        jobDetail['working_time'] = str(jobData['start_working_time']) + " ~ " + str(jobData['end_working_time'])
        jobDetail['working_location'] = model_to_dict(jobData['root_location'])["name"] + " " + model_to_dict(jobData['sub_location'])['name']
        jobDetail['working_date'] = jobData['start_working_date'] #TODO 포맷
        jobDetail['worker_age'] = str(jobData['worker_age_from']) + " ~ " + str(jobData['worker_age_to']) + "대"
        jobDetail['worker_sex'] = jobData['worker_sex']
        jobDetail['car_preference'] = jobData['car_preference']
        jobDetail['child_age'] = jobData['child_age']


        # 근무요일
        custom_day_of_weeks = []
        for item in jobData["all_day_of_week"]:
            customItem = model_to_dict(item)
            customItem['selected'] = False
            for selectedItem in jobData['day_of_weeks']:
                selectedItemDict = model_to_dict(selectedItem.day_of_week_id)
                if customItem['job_day_of_week_id'] == selectedItemDict['job_day_of_week_id']:
                    customItem['selected'] = True
                    break
            custom_day_of_weeks.append(customItem)




        jobDetail['working_day_of_weeks'] = json.dumps(custom_day_of_weeks)


        # 제출서류
        documents = []
        documents_string = ""
        for item in jobData["documents"]:
            documents.append(model_to_dict(item.require_document_id))
            documents.append(model_to_dict(item.require_document_id))

        for index, item in enumerate(documents):
            if index > 0:
                documents_string += ", "

            documents_string += item["document"]

        jobDetail['documents'] = documents_string




        return jobDetail

