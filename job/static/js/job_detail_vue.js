
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

        job: function() {

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

            app.$http.post("/job/api/updateContactNumber", {
                                params: {phone_number: app.contactNumber}
                            })
                            .then((result) => {

                                // 에러 리스폰스 테스트
                                if (result != null) {
                                    app.contactNumber = result.contactNumber
                                    app.hasContactNumber = true
                                    alert('저장완료')
                                    location.reload()
                                }
                            })

        }
        // 금액 단위 변환

      }
    })



