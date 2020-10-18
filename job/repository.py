from django.forms.models import model_to_dict
from pprint import pprint
from .queries import JobRecords
from django.core.paginator import Paginator


class JobRepository:

    @classmethod
    def process_job_detail(self, job_id):

        jobDetail = {}
        # query
        querySet = JobRecords.get_job_detail(job_id)
        allDayOfWeeks = JobRecords.get_all_day_of_week()


        jobDetail['user'] = model_to_dict(querySet.user)
        jobDetail['title'] = querySet.title
        jobDetail['pay'] = querySet.pay
        jobDetail['description'] = querySet.description
        jobDetail['working_time'] = str(querySet.start_working_time) + " ~ " + str(querySet.end_working_time)
        jobDetail['working_location'] = querySet.root_location.name + " " + querySet.second_location.name
        jobDetail['working_date'] = querySet.start_working_date #TODO 포맷
        jobDetail['worker_sex'] = querySet.worker_sex.sex
        jobDetail['car_preference'] = querySet.car_preference.value
        jobDetail['child_age'] = querySet.child_age.age
        jobDetail['working_day_of_weeks'] = self.get_working_day_of_weeks(querySet.day_of_weeks.all(), allDayOfWeeks)


        # # 제출서류
        documents = []
        documents_string = ""
        for item in list(querySet.documents.all()):
            documents.append(item.document)

        for index, item in enumerate(documents):
            if index > 0:
                documents_string += ", "

            documents_string += item

        jobDetail['documents'] = documents_string

        # 희망연령
        selectedWorkAge = []
        selectedWorkAgeString = ""
        for item in list(querySet.worker_age.all()):
            selectedWorkAge.append(item.age)

        for index, item in enumerate(selectedWorkAge):
            if index > 0:
                selectedWorkAgeString += ", "

            selectedWorkAgeString += str(item)

        jobDetail['worker_age'] = selectedWorkAgeString



        return jobDetail

    @classmethod
    def get_working_day_of_weeks(self, selectedDayOfWeeks, allDayOfWeek):
        # 근무요일
        customDayOfWeeks = []
        for item in list(allDayOfWeek):
            # dictionary 타입으로 변경후에 모델을 수정한다.
            customItem = model_to_dict(item)
            customItem['selected'] = False
            for selectedItem in list(selectedDayOfWeeks):
                if customItem['job_day_of_week_id'] == selectedItem.job_day_of_week_id:
                    customItem['selected'] = True
                    break
            customDayOfWeeks.append(customItem)


        return customDayOfWeeks



    @classmethod
    def process_job_list(self, page, selectedLocationId):

        # query
        querySet = JobRecords.get_job_list(selectedLocationId)
        # 15개씩 끊어서 아이템을 페이징한다.
        paginator = Paginator(querySet, 15)
        # paginator에서 해당 페이지의 아이템을 가져온다.
        pagingItems = paginator.get_page(page)

        #TODO :: vue에서 오브젝트로 대채한다.
        allDayOfWeeks = JobRecords.get_all_day_of_week()

        jobList = []


        for item in pagingItems:
            newItem = model_to_dict(item)
            newItem['root_location'] = model_to_dict(item.root_location)
            newItem['second_location'] = model_to_dict(item.second_location)
            newItem['working_day_of_weeks'] = self.get_working_day_of_weeks(item.day_of_weeks.all(), allDayOfWeeks)
            newItem['child_age'] = model_to_dict(item.child_age)
            newItem['day_of_weeks'] = []
            newItem['documents'] = []
            newItem['worker_age'] = []
            jobList.append(newItem)

        return {
            'totalPage': paginator.num_pages,
            'jobList': jobList
        }

    @classmethod
    def get_location_list(self):

        # 1차 지역들을 가져온다.
        locationList = list(JobRecords.get_all_root_location().values())

        for root in locationList:
            root['secondLocations'] = list(JobRecords.get_second_location(root["job_location_id"]).values())

        return locationList

    @classmethod
    def get_selected_location(self, selectedLocationId):
        # user가 선택한 지역을 가져온다.
        return model_to_dict(JobRecords.get_second_location_by_id(selectedLocationId)[0])


