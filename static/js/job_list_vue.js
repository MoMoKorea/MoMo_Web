

var listVue = new Vue({
    el: '#content',
    delimiters: ['[[', ']]'],
    data: {
        totalPage: 1,
        currentPage: 1,
        isPaging: false,
        jobList: [],
        user: {}
    },
    methods: {

        onLoadMoreScroll: function() {

            var windowHeight = $(window).height();
            var scrollYOffset = 200

            $(window).scroll(function () {
                var documentHeight = $(document).height();
                var scrollHeight = documentHeight - windowHeight

                // 스크롤길이가 200 이상일때
                if (scrollHeight >= 200) {

                   var scrollY = $(document).scrollTop();
                   console.log(scrollY)
                   // 스크롤길이가 200 정도 남았고, 마지막페이지가 아니며, 페이징중이 아니라면 추가로 로드한다.
                   if (scrollY > (scrollHeight - 200) && listVue.isLoadMore() && !listVue.isPaging) {

                        listVue.isPaging = true
                        listVue.$http.get(baseUri +"job", {
                            params: {
                                page: ++listVue.currentPage
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

        onToolbarScrollHeight: function() {
            var windowHeight = $(window).height();

            $(window).scroll(function () {
                var documentHeight = $(document).height();
                var scrollHeight = documentHeight - windowHeight

               var scrollY = $(document).scrollTop();
                console.log(scrollY)
            });

        }



    },
    updated () {
        // 스크롤 리스너 연결
        this.onLoadMoreScroll()
        // toolbar 계산용 스크롤 리스너
//        this.onToolbarScrollHeight()
    }



})