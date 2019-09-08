
    Vue.prototype.$http = axios
    const baseUri = "http://127.0.0.1:8000/"
    var validateChildIds = new Array()
    var validateDayOfWeekIds = new Array()
    var validate = new Array()

    var app = new Vue({
      el: '#content',
      delimiters: ['[[', ']]'],

      data: {

        // common
        currentPage: 1,

        // page 1
        title: "",
        pay: '',
        isNegotiation: false,
        startWorkingDate: '',
        startWorkingTime: '',
        endWorkingTime: '',
        dayOfWeekList: '',
        selectedDayOfWeekId: [ ],
        childAgeList: '',
        selectedChildAgeId: '',

        // page 2
        startAvailableCallingTime: 0,
        endAvailableCallingTime: 0,
        mobile: '',
        rootLocationList: [],
        secondLocationList: [],
        thirdLocationList: [],
        selectedRootLocationId: 0,
        selectedSecondLocationId: 0,
        selectedThirdLocationId: 0,

        // page 3
        preferredCarList: '',
        preferredSexList: '',
        preferredAgeList: '',
        selectedPreferredSexId: 1,
        selectedPreferredCarId: 1,
        requiredDocumentList: '',
        selectedRequiredDocumentId: [],

        // page 4
        description: '',
      },

      watch: {

        // 시급 예외처리
        pay: function (val) {
           console.log(val)
        },

        // 페이지 변경될때 벨리데이션 체크하기
        currentPage: function(val) {
           console.log(val)
           if (val == 2) {
             this.getRootLocation()
           }
        },

        // 1차 지역선택 후 2차 지역 select
        selectedRootLocationId: function(val) {
            if (val > 0) {

                this.$http.get(baseUri + "job/api/second-location", {
                    params: {
                        parent_id: val
                    }
                })
                .then((result) => {
                this.secondLocationList = result.data.secondLocations
                })

            }
        },

        // 2차 지역선택 후 3차 지역 select
        selectedSecondLocationId: function(val) {
            if (val > 0) {

                this.$http.get(baseUri + "job/api/third-location", {
                    params: {
                        parent_id: val
                    }
                })
                .then((result) => {
                this.thirdLocationList = result.data.thirdLocations
                })

            }
        },
        childAgeList: function() {

            this.childAgeList.forEach(function(item) {
                validateChildIds.push(item.child_age_id)
            })
        },
        dayOfWeekList: function() {

            this.dayOfWeekList.forEach(function(item) {
                validateDayOfWeekIds.push(item.job_day_of_week_id)
            })
        }

      },

      methods: {
//        selectChildAge: function (event) {
//          this.child_age = event.target.id
//        }
        onAfterPage: function(page) {

            // 1. validation 체크
            this.checkPageValidate(page)

            // 2. validation 항목이 존재할경우 경고메시지 show
            if (validate.length > 0) {
                alert(validate)
            }
            // 3. validation 항목이 없을경우 페이지 이동
            else {
                this.currentPage = page + 1
            }

        },
        onBeforePage: function(page) {
            this.currentPage = page - 1
        },
        getRootLocation: function() {
            if(this.rootLocationList.length != 0) return

              this.$http.get(baseUri + "job/api/root-location")
              .then((result) => {
                this.rootLocationList = result.data.rootLocations
              })
        },
        onRegist: function() {

            // 1. 페이지 체크
            if (this.currentPage != 4) return
            // 2. 벨리데이션 체크

            // 3. 데이터 가공
            var data = this.$data

            var params = {
                user_id: 72738,
                title: data.title,
                pay: data.pay,
                is_negotiation: data.isNegotiation,
                location_id: data.selectedRootLocationId,
                sub_location_id: data.selectedSecondLocationId,
                third_location_id: data.selectedThirdLocationId,
                description: data.description,
                start_available_calling_time: data.startAvailableCallingTime,
                end_available_calling_time: data.endAvailableCallingTime,
                start_working_time: data.startWorkingTime,
                end_working_time: data.endWorkingTime,
                start_working_date: data.startWorkingDate,
                worker_sex_id: data.selectedPreferredSexId,
                worker_age_from_id: 1,
                worker_age_to_id: 3,
                car_preference_id: data.selectedPreferredCarId,
                child_age_id: data.selectedChildAgeId,
                selectedDayOfWeeks: data.selectedDayOfWeekId,
                selectedRequiredDocuments: data.selectedRequiredDocumentId
            };


            this.$http.post(baseUri + "job/regist", { params })
              .then((result) => {
                console.log(result)
              })

        },
         // 벨리데이션 체크용 함수
        checkPageValidate: function(page) {

            validate = []

            if (page == 1) {

                // 제목
                if (isEmpty(this.title)) {
                    validate.push("title")
                }
                else{
                    // 글자수 체크
                }

                // 영아정보
                if (isEmpty(this.selectedChildAgeId)) {
                    validate.push("child_age")
                }
                else { // 유효한 선택값인지 체크
                    if(validateChildIds.includes(this.selectedChildAgeId)) {
                        console.log("include")
                    }
                    else {
                        console.log("not include")
                    }
                }

                // 희망시급
                if (isEmpty(this.pay)) {
                    validate.push("pay")
                }
                else {
                    // 금액 체크
                }

                // 근무시작일
                if (isEmpty(this.startWorkingDate)) {
                    validate.push("start_working_time")
                }
                else {

                }


                // 근무요일
                if (isEmpty(this.selectedDayOfWeekId)) {
                    validate.push("day_of_week")
                }
                else {
                    // 유효한 요일 체크
                    this.selectedDayOfWeekId.forEach(function(selectedItem) {
                        if (validateDayOfWeekIds.includes(selectedItem)) {
                            console.log(selectedItem + "selectedDayOfWeekId include")
                        }
                        else {
                            console.log(selectedItem + "selectedDayOfWeekId not include")
                        }
                    })

                }

                // 근무 시작 시간
                if (isEmpty(this.startWorkingTime)) {
                    validate.push("start_working_time")
                }

                // 근무 시작 종료

                if (isEmpty(this.endWorkingTime)) {
                    validate.push("end_working_time")
                }

            }


            console.log(validate)


        }


      }
    })



