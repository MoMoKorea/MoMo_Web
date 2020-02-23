

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

        // 페이징 스크롤 리스너
        onLoadMoreScroll: function() {

            var windowHeight = $(window).height();
            var scrollYOffset = 200

            $(window).scroll(function () {
                var documentHeight = $(document).height();
                var scrollHeight = documentHeight - windowHeight

                // 스크롤길이가 200 이상일때
                if (scrollHeight >= 200) {

                   var scrollY = $(document).scrollTop();
                   if (scrollY >= 140) {
                      $("#toolbar").show()
                   }
                   else {
                      $("#toolbar").hide()
                   }

                   // 스크롤길이가 200 정도 남았고, 마지막페이지가 아니며, 페이징중이 아니라면 추가로 로드한다.
                   if (scrollY > (scrollHeight - 200) && listVue.isLoadMore() && !listVue.isPaging) {

                        listVue.isPaging = true
                        listVue.getJobList()
                   }
               }
            });

        },

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

            listVue.$http.get("http://" + baseUri +"/job", {
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
    updated () {
        // 스크롤 리스너 연결
        this.onLoadMoreScroll()
    }



})