
//    Vue.prototype.$http = axios
//    const baseUri = "http://127.0.0.1:8000/"

    var app = new Vue({
      el: '#content',
      delimiters: ['[[', ']]'],

      data: {
        job: {},
        workingDayOfWeeks: [],
        hasContactNumber: false,
        contactNumber: '',
      },

      watch: {
        pay: function() {

        }
      },

      methods: {

        showContactModal: function() {

            if (this.hasContactNumber) {
                $("#contactModal").toggle()
            }
            else {
                $("#requiredContactNumberModal").toggle()
            }
            $(".modal_background").toggle()

        },
        // 연락처 정보 업데이트
        updateContactNumber: function() {

            if (this.contactNumber.length == 0) return

            //TODO :: user contactnumber update api
            alert('저장완료')
            location.reload()

        }

      }
    })



