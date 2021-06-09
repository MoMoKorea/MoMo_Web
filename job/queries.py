import logging, json
from pprint import pprint

from job.models import JobRequireDocumentMappingORM, JobAgeMappingORM
from job.models.job import JobORM
from job.serializers import JobSerializer, ChildAgeSerializer
from job.models.child_age import ChildAgeORM
from job.models.job_day_of_week import JobDayOfWeekORM
from job.models.job_sex import JobSexORM
from job.models.job_car_preference import JobCarPreferenceORM
from job.models.job_age import JobAgeORM
from job.models.job_require_document import JobRequireDocumentORM
from .models.job_location import JobLocationORM
from .models.job_day_of_week_mapping import JobDayOfWeekMappingORM
from django.forms.models import model_to_dict


logger = logging.getLogger(__name__)


class JobRecords:
    """
    Kyle 2019-07-20

    @API: 구직등록 Query
    """

    @staticmethod
    def create(data):
        serializer = JobSerializer(data=data)
        pprint(serializer.is_valid())
        if serializer.is_valid():
            job = serializer.save()

            # 근무요일 save
            for dayId in data["selectedDayOfWeeks"]:
                selectedDayOfWeek = JobDayOfWeekORM(dayId)
                JobDayOfWeekMappingORM.objects.create(job_id=job, day_of_week_id=selectedDayOfWeek)

            # 제출문서 save
            for documentId in data["selectedRequiredDocuments"]:
                selectedDocument = JobRequireDocumentORM(documentId)
                JobRequireDocumentMappingORM.objects.create(job_id=job, require_document_id=selectedDocument)

            # 선호 연령 save
            for workerAge in data["selectedWorkerAge"]:
                selectedWorkerAge = JobAgeORM(workerAge)
                JobAgeMappingORM.objects.create(job_id=job, age_id=selectedWorkerAge)


            return serializer
        else:
            pprint("err_message=" + str(serializer.error_messages))
            return None

    """
    Kyle 2019-07-20
     
    @API: 구직상세 Query  
    """

    @staticmethod
    def get_job_detail(jobId):
        return JobORM.get_detail().get(job_id=jobId)

    """
    Kyle 2019-10-06

    @API: 구직 리스트  
    """
    @staticmethod
    def get_job_list(locationId):
        return JobORM.get_main_list().order_by('-job_id').filter(second_location_id=locationId)


    """
    Kyle 2019-07-20

    @API: 자녀 나이 리스트 Query  
    """

    @staticmethod
    def get_all_child_age():
        return ChildAgeORM.objects.all()

    """
    Kyle 2019-07-20

    @API: 희망 근무요일 리스트 Query  
    """

    @staticmethod
    def get_all_day_of_week():
        return JobDayOfWeekORM.objects.all()

    """
    Kyle 2019-08-02

    @API: 희망 근무자 성별 리스트 Query  
    """

    @staticmethod
    def get_all_preferred_sex():
        return JobSexORM.objects.all()


    @staticmethod
    def get_all_preferred_age():
        return JobAgeORM.objects.all()


    @staticmethod
    def get_all_required_document():
        return JobRequireDocumentORM.objects.all()


    @staticmethod
    def get_all_preferred_car():
        return JobCarPreferenceORM.objects.all()

    @staticmethod
    def get_all_root_location():
        return JobLocationORM.objects.filter(depth=1, status=1)

    @staticmethod
    def get_second_location(parent_id):
        return JobLocationORM.objects.filter(parent_location_id=parent_id, depth=2, status=1)

    @staticmethod
    def get_second_location_by_id(location_id):
        return JobLocationORM.objects.filter(job_location_id=location_id, depth=2, status=1)

    @staticmethod
    def get_third_location(parent_id):
        return JobLocationORM.objects.filter(parent_location_id=parent_id, depth=3, status=1)
