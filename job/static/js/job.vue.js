
window.onload = function() {

    var app = new Vue({
      el: '#body',
      delimiters: ['[[', ']]'],

      data: {
        title: '',
        child_age: 1,
        pay: '',
        isNegotiation: false,
        startWorkingDate: '',
        startWorkingTime: '',
        endWorkingTime: '',
        dayOfWeek: ['월','화','수','목','금','토','일'],
        selectedDayOfWeek: [],

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
}
