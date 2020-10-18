

var listVue = new Vue({
    el: '#content',
    delimiters: ['[[', ']]'],
    data: {
        totalPage: 1,
        currentPage: 1,
        isPaging: false,
        jobList: [],
        user: {},
        locations: [],
        selectedLocation: {},
    },
    methods: {

        // 페이징 가능여부
        isLoadMore: function() {
            return this.totalPage > this.currentPage
        },
        // 등록하기 클릭
        onRegistClick: function() {
            window.location.href = "/job/regist"
        },

        // 지역 클릭 리스너
        onLocationClick: function(location) {
            // 지역 리스트 모달을 닫는다.
            if ($(".modal_top,.modal_bottom,.modal,.modal_background").is(':visible') == true) {
                $(".modal_top,.modal_bottom,.modal,.modal_background").fadeToggle( "fast" )
            }
            else if ($(".headlocal_body").is(':visible') == true) {
                $(".headlocal_body").animate({height:'toggle'},150)
                $(".headlocal_background").fadeToggle( "fast" )
                $("#toolbar").hide()
            }

            // 화면에 나오는 데이터를 지운다.
            listVue.jobList = []
            // 지역 id로 데이터를 불러온다.
            listVue.currentPage = 0
            listVue.selectedLocation = location
            listVue.getJobList()
            // 스크롤을 최상단으로 올린다.

        },

        getJobList: function() {

            listVue.$http.get("/job", {
                                params: {
                                    page: ++listVue.currentPage,
                                    location_id: listVue.selectedLocation.job_location_id
                                }
                            })
                            .then((result) => {
                                var jobList = result.data['jobList']
                                for(var i = 0; i < jobList.length; i++) {
                                    // 원본데이터 변경을 방지하기 위해 새로운 변수에 담는다.
                                    jobList[i].payWithComma = numberWithCommas(jobList[i].pay)
                                }
                                listVue.isPaging = false
                                listVue.jobList = listVue.jobList.concat(jobList)
                            })
        }



    },
})