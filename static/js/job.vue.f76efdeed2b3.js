

    var app = new Vue({
      el: '#content',
      delimiters: ['[[', ']]'],

      data: {
        title: "title",
        pay: '',
        isNegotiation: false,
        startWorkingDate: '',
        startWorkingTime: '',
        endWorkingTime: '',
        dayOfWeek: '',
        selectedDayOfWeek: '',
        childAgeList: '',
        selectedChildAgeId: 1,
      },

      watch: {
        pay: function (val) {
           // 금액 예외처리
           console.log(val)
        }
      },

      methods: {
//        selectChildAge: function (event) {
//          this.child_age = event.target.id
//        }
      }
    })



