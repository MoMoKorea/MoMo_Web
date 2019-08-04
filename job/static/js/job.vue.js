

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
        pay: function (val) {
           // 금액 예외처리
           console.log(val)
        },

        currentPage: function(val) {
            // 페이지 변경될때 벨리데이션 체크하기
           console.log(val)
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
        }
      }
    })



