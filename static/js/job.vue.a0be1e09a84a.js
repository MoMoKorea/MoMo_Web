

    var app = new Vue({
      el: '#content',
      delimiters: ['[[', ']]'],

      data: {
        title: "",
        pay: '',
        isNegotiation: false,
        startWorkingDate: '',
        startWorkingTime: '',
        endWorkingTime: '',
        dayOfWeek: '',
        dayOfWeekList: '',
        selectedDayOfWeekId: [ ],
        childAgeList: '',
        selectedChildAgeId: 1,
        currentPage: 1,
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



