
    var app = new Vue({
      el: '#content',
      delimiters: ['[[', ']]'],

      data: {
        job: {},
        workingDayOfWeeks: [],
        hasContactNumber: false,
        contactNumber: '',
        user: {}
      },

      watch: {

        job: function() {

        },
      },

      methods: {

        // 연락하기 클릭시 하단 다이얼로그
        showContactModal: function() {

            // 미 로그인 유저라면 로그인 화면으로 이동
            if (app.user == null) {
                $(location).attr('href', (baseUrl + "user/login"))
                return
            }

            // modal & background toggle
            if (isEmpty(app.user.phone_number)) $("#requiredContactNumberModal").toggle()
            else $("#contactModal").toggle()
            $(".job_detail_modal_background").toggle()
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

        },
        // 여백 클릭시 modal 종료
        dismissModal: function() {
            $("#contactModal").hide()
            $("#requiredContactNumberModal").hide()
            $(".job_detail_modal_background").hide()
        },
        // 전화연결
        onCall: function() {

            if (this.user.id == this.job.user.id) {
                alert("자신에게 연락할 수 없습니다.")
                return
            }

            if (!isEmpty(app.job.user.phone_number)) {
               window.location.href = 'tel:' + app.job.user.phone_number
            }
            else {
               alert("연락처를 찾을 수 없습니다.")
            }
        }

      }
    })



