
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
        }


      }
    })



