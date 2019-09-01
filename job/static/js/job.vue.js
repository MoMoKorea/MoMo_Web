
    Vue.prototype.$http = axios
    const baseUri = "http://127.0.0.1:8000/"

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
        selectedChildAgeId: 1,

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
        }



      },

      methods: {
//        selectChildAge: function (event) {
//          this.child_age = event.target.id
//        }
        onAfterPage: function(page) {
            this.currentPage = page + 1
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


        }


      }
    })



