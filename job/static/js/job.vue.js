

    var app = new Vue({
      el: '#body',
      delimiters: ['[[', ']]'],

      data: {
        title: "title",
        child_age: 1,
        pay: '',
        isNegotiation: false,
        startWorkingDate: '',
        startWorkingTime: '',
        endWorkingTime: '',
        dayOfWeek: '',
        selectedDayOfWeek: '',
        childAgeList: '',

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



